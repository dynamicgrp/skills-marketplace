# Dynamic Group Skills Marketplace

Shared Claude skills for Dynamic Group. One plugin, installed once, carrying every skill the company uses.

This is a **Claude Code plugin marketplace**. You add it once by URL and the skills work inside Claude, with no cloning and no manual updates. When we add a skill, it reaches everyone on their next update. Nobody installs anything again.

## Install

```
/plugin marketplace add dynamicgrp/skills-marketplace
/plugin install dynamic-skills@skills-marketplace
```

Restart Claude Code and it is live.

Teammates who want the click-through version, including the menu route and troubleshooting, should use the setup guide rather than this README.

### If you added this before

The marketplace and plugin have both been renamed. Remove the old entries and add them again. This is the last rename; the structure now absorbs new skills without changing either name.

```
/plugin uninstall dynamic-brand@dynamic-marketplace
/plugin marketplace remove dynamic-marketplace
/plugin marketplace add dynamicgrp/skills-marketplace
/plugin install dynamic-skills@skills-marketplace
```

Earlier names, all retired: marketplace `dynamic-group`, plugins `construction-tools` and `dynamic-brand`.

### Registering it automatically

Put this in `~/.claude/settings.json`, or commit it as `.claude/settings.json` in a shared repo:

```json
{
  "extraKnownMarketplaces": {
    "skills-marketplace": {
      "source": { "source": "github", "repo": "dynamicgrp/skills-marketplace" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "dynamic-skills@skills-marketplace": true }
}
```

This registers the marketplace. Each person still runs the install command once, because the plugin lives in an external repo.

## Skills in this plugin

| Skill | Fires when you ask about |
|---|---|
| `dynamic-brand` | Anything produced for Dynamic: proposals, reports, qualifications, client email, web pages, slides, social. Our colors, type scale, logo rules, layout motifs, list markers, voice and tone. Also answers direct questions about the standard, and reviews existing material against it. |
| `rfi-writer` | Drafting an RFI to an owner, architect or engineer. Unclear, conflicting or missing drawings and specs. Reviewing a received response for whether it actually answers. Tracking turnaround against contract response times. |

Skills are invoked automatically when a question matches. Nobody types a skill name.

## Updating

```
/plugin marketplace update skills-marketplace
```

Run this after we add or change a skill. There is no second install step.

## Adding a skill

Everything lives in one plugin so the company installs once. A new skill is a new folder inside it, not a new plugin.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process. In short: add `plugins/dynamic-skills/skills/<your-skill>/SKILL.md`, write a trigger-rich `description`, bump the version in both manifests, open a PR.

## Access

This repo is private. `/plugin marketplace add` uses each person's own git auth, so teammates need read access on `dynamicgrp/skills-marketplace` or the add fails silently for them.

---

**Marketplace**: `skills-marketplace` · **Plugin**: `dynamic-skills` v3.1.0
