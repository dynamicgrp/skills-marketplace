# Dynamic Group Skills Marketplace

Internal Claude skills for Dynamic Group.

This is a **Claude Code plugin marketplace**. You add it once by URL and the skills work inside Claude, with no cloning and no manual updates.

## Install

```
/plugin marketplace add dynamicgrp/skills-marketplace
/plugin install dynamic-brand@dynamic-marketplace
```

Restart Claude Code and it is live.

### If you added this before

The marketplace was previously named `dynamic-group` and the plugin `construction-tools`. Both have changed, so remove the old entries and add them again:

```
/plugin uninstall construction-tools@dynamic-group
/plugin marketplace remove dynamic-group
/plugin marketplace add dynamicgrp/skills-marketplace
/plugin install dynamic-brand@dynamic-marketplace
```

### Adding it without typing commands

Put this in `~/.claude/settings.json`, or commit it as `.claude/settings.json` in a team repo:

```json
{
  "extraKnownMarketplaces": {
    "dynamic-marketplace": {
      "source": { "source": "github", "repo": "dynamicgrp/skills-marketplace" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "dynamic-brand@dynamic-marketplace": true }
}
```

This registers the marketplace automatically. Each person still runs the install command once, because the plugin lives in an external repo.

## What it does

The `dynamic-brand` skill carries the Dynamic Group Brand Guide, September 2026. Claude applies it without being asked whenever it produces something for Dynamic: a proposal, report, qualifications package, client email, web page, slide or social post.

It covers:

| Area | What it settles |
|---|---|
| Color | Dynamic Orange `#F26F21`, Dynamic Charcoal `#54565A`, the accents, inks, surfaces and line weights. No blues, no purples, no gradients but the cover scrim. |
| Typography | Barlow Semi Condensed for headings and chrome, ALL CAPS. Source Sans 3 for body. The full nine step scale with sizes and casing. |
| Voice | First person plural. Dynamic Group then Dynamic. Never the firm or its. Client addressed by title. No em dashes, no emoji, no exclamation points. |
| Logo | Lockup and cube, sizing, clear space, placement, and the four things never to do to it. |
| Layout | 816 by 1056px page, the orange rule motifs, padding, radius, borders and shadows. |
| Lists | Four markers, one per page, and what each is for. |
| Imagery | Documentary site and crew photography, caption format, cover scrim treatment. |

Two bundled references Claude reads when the task needs them: `tokens.css` with every value as CSS custom properties and the components built, and `document-patterns.md` with cover, divider, content and table structures plus the ReportLab and font sourcing notes.

### Try it

Ask normally. No slash command.

> Draft the cover letter for the Seminole housing RFQ.

> Build me an HTML page template for a qualifications package.

> What is our orange?

> Review this paragraph against our brand standards.

## Updating

```
/plugin marketplace update dynamic-marketplace
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Access

This repo is private. `/plugin marketplace add` uses each person's own git auth, so teammates need read access on `dynamicgrp/skills-marketplace` or the add fails silently for them.

---

**Marketplace**: `dynamic-marketplace` · **Plugin**: `dynamic-brand` v2.0.0
