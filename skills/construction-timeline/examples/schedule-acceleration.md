# Example: Disaster Recovery Housing - Schedule Compression

## Scenario
75-unit disaster recovery housing project in Florida with customer deadline: September 30, 2026 (10 months from start). Current schedule shows 12 months.

## Input
```
/construction-timeline

Project: 75-unit disaster recovery housing, Florida
Customer Deadline: September 30, 2026 (10 months)
Current Schedule: 12 months
Gap: 2 months behind deadline

Activities:
- Permitting: 4 months
- Site prep: 2 months (parallel to permitting)
- Material delivery: 2 months
- Foundation work: 3 months
- Installation: 2 months
- Final inspections: 1 month
```

## Analysis
Critical path: Permitting → Foundation → Installation → Inspections (12 months total)

**Bottleneck:** Permitting (4 months) - hard to accelerate

**Strategies:**
1. Conditional material pre-orders (save 3-4 weeks)
2. Expedited FEMA review (save 2-4 weeks)
3. Extended work windows (save 2 weeks)

**Recommendation:** Implement Strategy 1 + 3 for realistic 10.5-month timeline

---

See README.md for more examples.
