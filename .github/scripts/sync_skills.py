#!/usr/bin/env python3
"""Validate the skills in this marketplace and keep the manifests in step.

Two jobs:

1. Validate every SKILL.md. A skill with broken frontmatter, or with a
   description too vague to trigger on, installs cleanly and then never
   fires. That failure is silent, which is why it is checked here.

2. Bump the plugin version when a change would otherwise reach nobody.
   Claude caches an installed plugin by version, so a new skill pushed
   without a version bump does not reach anyone who already installed.
   Forgetting it is easy and the symptom is invisible, so CI does it.

Run before opening a PR:
    python3 .github/scripts/sync_skills.py --check

CI runs it without --check on pull requests, which lets it write the bump.
"""

import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PLUGIN = "dynamic-skills"
SKILLS_DIR = ROOT / "plugins" / PLUGIN / "skills"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PLUGIN_JSON = ROOT / "plugins" / PLUGIN / ".claude-plugin" / "plugin.json"
README = ROOT / "README.md"

# A description shorter than this cannot carry enough trigger detail to fire
# reliably. The number is a floor, not a target.
MIN_DESCRIPTION = 120


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None, text
    fields = dict(re.findall(r"^([A-Za-z_]+):\s*(.+)$", match.group(1), re.M))
    return fields, text


def validate_skills():
    errors = []
    if not SKILLS_DIR.is_dir():
        return [f"no skills directory at {SKILLS_DIR.relative_to(ROOT)}"], []

    dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not dirs:
        errors.append("no skills found")

    names = []
    for d in dirs:
        rel = d.relative_to(ROOT)
        skill_file = d / "SKILL.md"

        if not skill_file.exists():
            errors.append(f"{rel}: no SKILL.md")
            continue

        fields, text = read_frontmatter(skill_file)
        if fields is None:
            errors.append(f"{rel}: frontmatter missing or malformed, needs a --- block at the top")
            continue

        name = fields.get("name", "")
        description = fields.get("description", "")

        if name != d.name:
            errors.append(f"{rel}: frontmatter name is '{name}', must match the directory name '{d.name}'")
        if not re.fullmatch(r"[a-z0-9-]+", d.name):
            errors.append(f"{rel}: directory name must be kebab-case")
        if not description:
            errors.append(f"{rel}: no description, so Claude has nothing to decide on and the skill will never fire")
        elif len(description) < MIN_DESCRIPTION:
            errors.append(
                f"{rel}: description is {len(description)} characters, under the {MIN_DESCRIPTION} floor. "
                "Name the concrete situations it should fire on."
            )
        elif "use when" not in description.lower():
            errors.append(
                f"{rel}: description has no 'Use when ...' clause. Without one it triggers unpredictably."
            )

        stray = sorted(set(fields) - {"name", "description"})
        if stray:
            errors.append(
                f"{rel}: frontmatter carries {', '.join(stray)}. Only name and description belong here; "
                "version and author live in plugin.json."
            )

        if len(text) < 800:
            errors.append(f"{rel}: body is very short, {len(text)} characters. A stub skill is worse than no skill.")

        names.append(d.name)

    duplicates = {n for n in names if names.count(n) > 1}
    for n in sorted(duplicates):
        errors.append(f"duplicate skill name: {n}")

    return errors, names


def check_readme(names):
    if not README.exists():
        return ["no README.md"]
    text = README.read_text(encoding="utf-8")
    missing = [n for n in names if f"`{n}`" not in text]
    return [
        f"README does not mention `{n}`. Every skill needs a row so people know it exists."
        for n in missing
    ]


def main_version():
    """The plugin version currently on main, or None if it cannot be read."""
    try:
        blob = subprocess.run(
            ["git", "show", "origin/main:.claude-plugin/marketplace.json"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
        return json.loads(blob)["plugins"][0]["version"]
    except Exception:
        return None


def touches_shipped_content():
    """True when this branch changes something that actually reaches users.

    A version bump is only warranted when the plugin or its manifests moved.
    Editing CI, docs or the setup guide ships nothing, so it should not bump.
    """
    try:
        diff = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.split()
    except Exception:
        return True  # cannot tell, so assume it matters
    if not diff:
        diff = subprocess.run(
            ["git", "diff", "--name-only", "origin/main"],
            cwd=ROOT, capture_output=True, text=True,
        ).stdout.split()
    return any(f.startswith(("plugins/", ".claude-plugin/")) for f in diff)


def parse(version):
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        return None
    return tuple(int(p) for p in parts)


def sync_versions(write):
    """Make both manifests agree, and bump if this change would ship to nobody."""
    notes, errors = [], []

    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugin = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    current = marketplace["plugins"][0]["version"]

    if plugin["version"] != current:
        notes.append(f"plugin.json was {plugin['version']}, marketplace.json {current}; using {current}")

    parsed = parse(current)
    if parsed is None:
        return [], [f"version '{current}' is not MAJOR.MINOR.PATCH"]

    on_main = main_version()
    target = current
    if on_main is None:
        notes.append("no origin/main to compare against, leaving the version alone")
    elif on_main == current and not touches_shipped_content():
        notes.append("nothing under plugins/ or .claude-plugin/ changed, so no bump is needed")
    elif on_main == current:
        major, minor, patch = parsed
        target = f"{major}.{minor}.{patch + 1}"
        notes.append(
            f"version still {current}, same as main, so this change would not reach anyone already "
            f"installed. Bumping to {target}."
        )
    else:
        notes.append(f"version already moved from {on_main} to {current}, leaving it alone")

    changed = target != current or plugin["version"] != target

    if changed and write:
        marketplace["plugins"][0]["version"] = target
        marketplace.setdefault("metadata", {})["version"] = target
        plugin["version"] = target
        MARKETPLACE.write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf-8")
        PLUGIN_JSON.write_text(json.dumps(plugin, indent=2) + "\n", encoding="utf-8")
        notes.append(f"wrote {target} to both manifests")
    elif changed:
        errors.append(
            f"version needs to be {target} in both manifests. Run this script without --check, "
            "or set it by hand."
        )

    return notes, errors


def main():
    check_only = "--check" in sys.argv

    errors, names = validate_skills()
    errors += check_readme(names)

    if errors:
        print("Skills validation failed:\n")
        for e in errors:
            print(f"  - {e}")
        print(f"\n{len(errors)} problem(s). Nothing was changed.")
        return 1

    print(f"Validated {len(names)} skill(s): {', '.join(names)}")

    notes, version_errors = sync_versions(write=not check_only)
    for n in notes:
        print(f"  {n}")
    if version_errors:
        print()
        for e in version_errors:
            print(f"  - {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
