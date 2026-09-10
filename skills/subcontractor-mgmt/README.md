# Subcontractor Management Helper

Track vendor capacity, identify scheduling conflicts, and recommend optimal subcontractor assignments.

## Overview

This skill helps project managers and operations teams make smart subcontractor assignment decisions. It identifies available vendors, flags scheduling conflicts, and recommends the best contractor for each job based on capacity, quality, and timeline fit.

**Perfect for:**
- Assigning trades to new projects
- Managing concurrent projects and vendor capacity
- Identifying scheduling conflicts early
- Ensuring quality and reliability through vendor selection
- Optimizing crew utilization across portfolio

## When to Use

✅ Use when:
- You need to assign a trade to a new project
- You're managing multiple concurrent projects
- You need to identify vendor conflicts or bottlenecks
- You want to optimize crew utilization
- You're planning a new project and estimating team needs

## How to Use

### 1. Activate the Skill
```bash
/subcontractor-mgmt
```

### 2. Provide Your Vendor Roster
List your available subcontractors:
- Foundation works: ABC Site Prep, XYZ Concrete
- Framing: BuildFast Framing
- Electrical: ElectroWorks
- HVAC: Cool Systems

### 3. Provide Active Project Timeline
```
Current projects:
- Project A: July 1 - October 15 (needs foundation + framing)
- Project B: August 1 - December 31 (needs electrical + HVAC)
- Project C: August 15 - ? (new, needs site work)
```

### 4. Ask for Assignment Recommendation
```
Project C needs site prep starting August 15. Who should we use?
```

### 5. Get Recommendation
Claude will provide:
- **Recommended vendor** – Best fit with reasoning
- **Alternatives** – Backup options
- **Timeline** – When they're available
- **Conflicts** – Any scheduling issues
- **Risks** – Capacity concerns or performance notes

---

**Skill Version**: 1.0.0  
**Last Updated**: 2026-09-10
