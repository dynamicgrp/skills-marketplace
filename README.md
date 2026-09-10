# Dynamic Group Skills Marketplace

Internal Claude skills for Dynamic Group construction operations, project delivery, and business development.

This is a **Claude Code plugin marketplace**. You add it once by URL and the skills show up inside Claude — no cloning, no copying files, no manual updates.

## Install

Run these two commands in Claude Code:

```
/plugin marketplace add dynamicgrp/skills-marketplace
/plugin install construction-tools@dynamic-group
```

That's it. Restart Claude Code and the skills are live.

To browse before installing, run `/plugin` with nothing after it and tab over to **Marketplaces**.

### Adding it without typing commands

Put this in `~/.claude/settings.json` for yourself, or commit it as `.claude/settings.json` in a team repo:

```json
{
  "extraKnownMarketplaces": {
    "dynamic-group": {
      "source": { "source": "github", "repo": "dynamicgrp/skills-marketplace" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "construction-tools@dynamic-group": true }
}
```

This registers the marketplace automatically. Each person still runs `/plugin install construction-tools@dynamic-group` once, because the plugin lives in an external repo.

## What's included

The `construction-tools` plugin bundles six skills. Claude invokes them automatically when your question matches — you never call them by name.

| Skill | Fires when you ask about |
|---|---|
| **construction-timeline** | Project schedules, critical path, bottlenecks, schedule compression, whether a deadline is achievable, float and slack, schedule risk |
| **project-bid-analyzer** | RFQs and RFPs, scope gaps, compliance and contract risk (prevailing wage, bonding, liquidated damages), whether a budget or timeline is realistic, go/no-go bid decisions |
| **subcontractor-mgmt** | Which sub to assign, crew and trade availability, scheduling conflicts across concurrent projects, crew capacity allocation |
| **change-order-analyzer** | Whether a change is compensable or in-scope, change order pricing, time impact, notice deadlines, responding to a denial, documenting a claim |
| **field-report-analyzer** | Daily reports and field logs, manpower trends, which trades are slipping, recurring site issues, what's really driving delays, what to raise with a super |
| **draw-request-builder** | Pay applications and draws, percent complete by line, schedule of values, lien waiver backup, retainage, why a draw was rejected or short-paid |

### Try it

Ask normally — no slash command:

> We're 3 months into a 60-unit modular job in NC and the customer moved the deadline up to 12 months. Factory is at capacity. What's realistic?

> Owner's rep verbally told us to relocate the utility run two weeks ago. We already did the work. Can we bill it?

> Here are six weeks of daily reports. Electrical headcount keeps dropping and I don't know why.

> Draw 7 got kicked back by the lender and they won't say what's wrong. Here's the package.

## Updating

```
/plugin marketplace update dynamic-group
```

Skills are improved in place, so pull periodically.

## Contributing a skill

See [CONTRIBUTING.md](CONTRIBUTING.md). Add a folder under `plugins/construction-tools/skills/`, write a `SKILL.md` with a trigger-rich `description`, bump the version in both manifests, open a PR.

## Access

This repo is private. `/plugin marketplace add` uses each person's own git auth, so teammates need read access on `dynamicgrp/skills-marketplace` or the add fails silently for them.

---

**Marketplace**: `dynamic-group` · **Plugin**: `construction-tools` v1.1.0 · 6 skills
