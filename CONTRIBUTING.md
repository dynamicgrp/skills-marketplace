# Adding a Skill

## One plugin, many skills

Everything lives inside a single plugin, `dynamic-skills`. That is deliberate. The company installs once, and every skill we add afterwards reaches people through `/plugin marketplace update skills-marketplace` with no second install and no new command to circulate.

So a new skill is a new folder inside the existing plugin, never a new plugin. Only split out a second plugin if a set of skills is genuinely for one team and would be noise for everyone else, and raise that before building it.

## Where skills live

```
plugins/dynamic-skills/skills/<your-skill-name>/
├── SKILL.md          # required
├── examples/         # optional
└── references/       # optional — files Claude reads on demand
```

Folder name must be kebab-case and must match the `name` in the frontmatter.

## Writing SKILL.md

```markdown
---
name: your-skill-name
description: What it does, in one clause. Use when the user asks to <trigger>, <trigger>, or <trigger>.
---

# Your Skill Name

## Your Expertise
What you know about this domain, specific to Dynamic Group.

## How to Use This Skill
What information to ask the user for.

## Analysis Process
Step-by-step what you do.

## Output Format
How you structure the response.

## Important Guidelines
Key principles, assumptions, and tradeoffs to surface.
```

### The description field is the whole ballgame

Claude decides whether to load your skill by reading `description` and nothing else. A vague description means the skill never fires.

**Bad** — never triggers:
```yaml
description: Helps with construction projects.
```

**Good** — fires on real questions:
```yaml
description: Analyze construction project schedules and recommend acceleration. Use when the user asks to analyze a project schedule, find the critical path, identify bottlenecks, compress a timeline, or assess whether a deadline is achievable.
```

Write it in third person, name the concrete situations, and include the words people actually use. Don't put `author` or `version` in skill frontmatter — those live in `plugin.json`.

## Test before you PR

```bash
git clone https://github.com/dynamicgrp/skills-marketplace.git
cd skills-marketplace
```

In Claude Code, add your local checkout as a marketplace and install from it:

```
/plugin marketplace add ./skills-marketplace
/plugin install dynamic-skills@skills-marketplace
```

Then ask a question your skill should catch and confirm it fires. Ask a question it *shouldn't* catch and confirm it stays quiet — over-triggering is as bad as under-triggering.

## The version is handled for you

CI bumps the plugin version on your pull request when your change would otherwise reach nobody. You do not need to touch `marketplace.json` or `plugin.json`.

This matters because Claude caches an installed plugin by version. A new skill pushed without a bump reaches only people installing fresh, and everyone already set up keeps the old set with no error and no sign anything is missing. That is a bad failure to leave to human memory, so it is automated.

Bump the minor or major version by hand only when you want to signal something deliberate. CI leaves your value alone if you have already moved it past main.

## Check before you push

```bash
python3 .github/scripts/sync_skills.py --check
```

This runs exactly what CI runs. It catches the failures that are otherwise silent: frontmatter that does not parse, a `name` that does not match the directory, a description too vague to trigger on, `version` or `author` left in the frontmatter where they do not belong, a stub body, and any skill missing from the README table.

A skill that fails these installs cleanly and then never fires, which is why they are errors rather than warnings.


## Open the PR

Say what the skill does, what questions should trigger it, and what you tested.

## Quality bar

- One job per skill. If it does three things, it's three skills.
- Specific to how Dynamic Group actually works — disaster recovery, workforce housing, modular, government contracting.
- State limitations. What it won't do matters as much as what it will.
- Surface tradeoffs rather than giving a single confident answer.
