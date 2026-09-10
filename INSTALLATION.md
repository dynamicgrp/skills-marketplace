# Installation Guide

How to install and use skills from the Dynamic Group Skills Marketplace in Claude Code.

## Prerequisites

- Claude Code installed and configured
- Git installed (to clone this repository)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/dynamicgrp/skills-marketplace.git
cd skills-marketplace
```

### 2. Copy Skills to Claude Code

**macOS/Linux:**
```bash
cp -r skills/* ~/.claude/skills/
```

**Windows (PowerShell):**
```powershell
Copy-Item -Path skills/* -Destination $env:USERPROFILE\.claude\skills\ -Recurse
```

### 3. Reload Claude Code

```bash
claude code /reload
```

### 4. Verify Installation

List installed skills:
```bash
claude code /skills
```

You should see:
- construction-timeline
- project-bid-analyzer
- subcontractor-mgmt

## Using a Skill

Invoke skills using slash commands:

```bash
/construction-timeline
```

Then interact with Claude as normal.

---

**Version**: 1.0.0
