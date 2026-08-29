# Specialist-agent map

```mermaid
flowchart LR
    R[Event router] --> REV[Revenue and cashiering]
    R --> BANK[Bank and card reconciliation]
    R --> CASH[Cash integrity]
    R --> REST[Restricted funds]
    R --> IF[Interfund]
    R --> PAY[Payroll]
    R --> GR[Grants and SEFA]
    R --> REP[Reporting and disclosures]
    REV --> E[Evidence lineage]
    BANK --> E
    CASH --> E
    REST --> E
    IF --> E
    PAY --> E
    GR --> E
    REP --> E
    E --> V[Verification and reviewer routing]
    V --> P[Controlled posting service]
    P --> IV[Independent verification]
```

Agents have bounded responsibilities. They can identify exceptions, assemble evidence, and propose treatment. They cannot manufacture authority, approve their own work, or bypass controlled posting and verification gates.

