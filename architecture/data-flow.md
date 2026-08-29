# Data flow

```mermaid
flowchart TD
    subgraph Sources[Existing municipal systems]
      ERP[Accounting / legacy ERP]
      UTIL[Utility billing and cashiering]
      BANK[Bank and card evidence]
      PAY[Payroll]
      GRANT[Grants and projects]
      DOCS[Authorities and documents]
    end

    Sources --> INGEST[Controlled connectors and ingestion]
    INGEST --> EVENTS[Normalized financial events]
    EVENTS --> REGISTRY[Evidence and authority registry]
    EVENTS --> ROUTER[Specialist-agent routing]
    REGISTRY --> ROUTER
    ROUTER --> CONTROLS[Deterministic accounting and policy controls]
    CONTROLS --> PASS[Supported population]
    CONTROLS --> EXCEPTION[Exception and proposal queue]
    PASS --> HUMAN[Required-role verification]
    EXCEPTION --> HUMAN
    HUMAN --> POSTING[Separate controlled posting boundary]
    POSTING --> VERIFY[Independent re-verification]
    VERIFY --> OUTPUT[Close, reporting, SEFA and audit support]
```

## Design principles

1. Existing systems remain authoritative.
2. Enrichment is additive; source facts are not silently overwritten.
3. Economic Event IDs connect transactions to evidence and approvals.
4. Accounting analysis, approval, posting, and verification are distinct states.
5. Unresolved evidence remains an exception rather than becoming an assumed conclusion.

