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

## Bump the version

Teammates get a cached copy until the version changes, so this step is what actually ships your work.

Edit both files so existing users get the update instead of a cached copy:

- `.claude-plugin/marketplace.json` → `plugins[0].version`
- `plugins/dynamic-skills/.claude-plugin/plugin.json` → `version`

## Open the PR

Say what the skill does, what questions should trigger it, and what you tested.

## Quality bar

- One job per skill. If it does three things, it's three skills.
- Specific to how Dynamic Group actually works — disaster recovery, workforce housing, modular, government contracting.
- State limitations. What it won't do matters as much as what it will.
- Surface tradeoffs rather than giving a single confident answer.
