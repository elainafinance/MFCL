# Data flow

![MFCL systems architecture](../demo/screenshots/systems-architecture.png)

1. Existing accounting, utility/cashiering, banking, payroll, grant/project, and document systems remain authoritative.
2. Controlled connectors ingest bounded source data and evidence.
3. Source activity is represented as normalized financial events with provenance.
4. The event router sends activity to specialist agents and deterministic controls.
5. Supported populations and exceptions move to required-role verification.
6. Approved items remain separate from the controlled posting boundary.
7. Independent re-verification supports close, reporting, SEFA, and audit preparation.

## Design principles

1. Existing systems remain authoritative.
2. Enrichment is additive; source facts are not silently overwritten.
3. Economic Event IDs connect transactions to evidence and approvals.
4. Accounting analysis, approval, posting, and verification are distinct states.
5. Unresolved evidence remains an exception rather than becoming an assumed conclusion.
