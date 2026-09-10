# Setup Guide - Deploy to GitHub

This repository is ready to go! It's already been pushed to GitHub at:

**https://github.com/dynamicgrp/skills-marketplace**

## Next Steps

### 1. Test Locally

Copy skills to your Claude Code directory:

**macOS/Linux:**
```bash
cp -r skills/* ~/.claude/skills/
claude code /reload
```

**Windows:**
```powershell
Copy-Item -Path skills/* -Destination $env:USERPROFILE\.claude\skills\ -Recurse
claude code /reload
```

### 2. Verify Installation

List installed skills:
```bash
claude code /skills
```

### 3. Test a Skill

```bash
/construction-timeline
# Then describe a project schedule to analyze
```

### 4. Share With Team

Send the repository link to your team:
- [README.md](README.md) – Overview
- [INSTALLATION.md](INSTALLATION.md) – Setup instructions
- [CONTRIBUTING.md](CONTRIBUTING.md) – How to create skills

### 5. Monitor & Iterate

- Collect feedback from team
- Fix issues and improve documentation
- Accept skill contributions via pull requests
- Archive old skills when needed

---

**Repository**: https://github.com/dynamicgrp/skills-marketplace  
**Status**: Active and ready for team use
