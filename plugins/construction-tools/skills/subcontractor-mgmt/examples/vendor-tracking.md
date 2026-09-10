# Example: Multi-Project Vendor Assignment

## Scenario
Managing 3 concurrent projects needing electrical work simultaneously

## Input
```
/subcontractor-mgmt

Vendor Options:
- ElectroWorks: 2 crews, booked Jan-March, available April+
- PowerTech Electric: 1 crew, flexible, premium cost
- LocalShocks: 1 crew, Oct-Dec available

Project Timelines:
- Project A: Dec 1 - April 30 (electrical Jan-March)
- Project B: Jan 15 - May 31 (electrical Feb-April)
- Project C: Feb 1 - June 30 (electrical March-May)

Assignment needed for all three projects.
```

## Recommendation
- **Project A:** ElectroWorks (1 crew, Jan-March) ✓
- **Project B:** PowerTech Electric (1 crew, premium) ✓
- **Project C:** Wait for ElectroWorks to finish A

**Alternative:** Stagger one project slightly to reduce conflicts

---

See README.md for more examples.
