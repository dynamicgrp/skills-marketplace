# Contributing Guide

Thank you for contributing to the Dynamic Group Skills Marketplace!

## Creating a Skill

### 1. Use the Skill Template

Copy [docs/skill-template.md](docs/skill-template.md) and customize it:

```bash
cp docs/skill-template.md skills/your-skill-name/SKILL.md
```

### 2. Structure Your Skill Directory

```
skills/your-skill-name/
├── SKILL.md              # Claude Code skill definition (required)
├── README.md             # User-facing documentation (required)
├── metadata.json         # Skill metadata (required)
└── examples/
    └── example-usage.md  # Usage examples (recommended)
```

### 3. Write Documentation

- **SKILL.md**: Claude instructions (what the skill does)
- **README.md**: User guide with examples
- **metadata.json**: Tags, difficulty, version, author
- **examples/**: Real usage scenarios

### 4. Test Your Skill

Install locally and test with real data:

```bash
cp -r skills/your-skill-name ~/.claude/skills/
claude code /reload
/your-skill-name
```

### 5. Submit a Pull Request

1. Fork the repository
2. Add your skill folder
3. Update `skills-catalog.json`
4. Create a pull request with details

## Quality Standards

**Do's** ✅
- Be specific to Dynamic Group's needs
- Use real examples (anonymized)
- Keep it focused – one main task per skill
- Document edge cases and limitations
- Test thoroughly before submitting

**Don'ts** ❌
- Don't duplicate existing skills
- Don't be too generic
- Don't skip examples
- Don't forget limitations

---

**Version**: 1.0.0
