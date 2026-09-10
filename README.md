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

To browse everything available first, run `/plugin` and pick **Browse marketplaces**.

## What's included

The `construction-tools` plugin bundles three skills. Claude invokes them automatically when your question matches — you don't have to call them by name.

| Skill | Invokes when you ask about |
|---|---|
| **construction-timeline** | Project schedules, critical path, bottlenecks, schedule compression, whether a deadline is achievable, float and slack, schedule risk |
| **project-bid-analyzer** | RFQs and RFPs, scope gaps, compliance and contract risk (prevailing wage, bonding, liquidated damages), whether a budget or timeline is realistic, go/no-go bid decisions |
| **subcontractor-mgmt** | Which sub to assign, crew and trade availability, scheduling conflicts across concurrent projects, crew capacity allocation |

### Try it

Once installed, just ask normally:

> We're 3 months into a 60-unit modular job in NC and the customer moved the deadline up to 12 months. Factory is at capacity. What's realistic?

> Here's the RFQ — 100 modular units, $12M, 9 months, prevailing wage, $2,500/day liquidated damages. Should we bid it?

> Project C needs site prep starting Aug 15. ABC Site Prep is free, XYZ is booked through September. Who do we use?

## Updating

When skills are improved, pull the latest:

```
/plugin marketplace update dynamic-group
```

## Contributing a skill

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: add a folder under `plugins/construction-tools/skills/`, write a `SKILL.md` with a trigger-rich `description`, open a PR.

---

**Marketplace**: `dynamic-group` · **Plugin**: `construction-tools` v1.0.0
