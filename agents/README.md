# High-level agent responsibilities

These descriptions communicate the public architecture without publishing proprietary prompts, detailed rules, mappings, scoring, or implementation.

| Agent or service | Public responsibility | Authority boundary |
| --- | --- | --- |
| Event router | Routes normalized events to the appropriate control workflow | Cannot make accounting conclusions or post |
| Revenue and cashiering | Connects receipt source, tender, deposit batch, bank evidence, and owning fund | Cannot infer fund ownership from tender alone |
| Bank and card reconciliation | Tests validated bank/card evidence against accounting activity | Cannot treat a poorly extracted bank line as valid evidence |
| Cash integrity | Surfaces missing, duplicated, delayed, or unusual cash activity | Creates exceptions, not silent corrections |
| Restricted funds | Tests purpose, period, project, budget, and governing authority | Cash movement or an account label cannot establish eligibility |
| Interfund | Separates recognition, reciprocal balances, settlement, and financing | Does not collapse distinct economic events |
| Payroll and position funding | Tests payroll populations, allocations, and funding evidence | Human review remains required for unsupported allocations |
| Grants and SEFA | Connects awards, eligibility, expenditures, evidence, and draft SEFA support | A cash receipt alone cannot establish recognition or SEFA inclusion |
| Reporting and disclosures | Assembles controlled reporting and disclosure support | Does not replace management judgment or the independent audit |
| Evidence lineage | Preserves source, authority, Economic Event ID, approval, and reporting history | Historical events are append-only |
| Verification router | Sends facts and judgments to the required municipal role | Role and responsibility govern authority, not system access alone |
| Controlled posting service | Executes only separately authorized, scope-limited actions | No self-approval or unrestricted write access |

