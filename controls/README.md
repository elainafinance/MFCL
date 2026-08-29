# Governance and controls

## Source authority

Existing accounting, utility, banking, payroll, grant, and document systems remain authoritative for their source facts. MFCL adds controlled relationships and conclusions without silently rewriting those facts.

## Human-in-the-loop authority

AI-assisted services may interpret, organize, and propose. Deterministic controls calculate and test. Authorized municipal personnel verify facts, exercise accounting judgment, approve actions, and accept management responsibility.

## Segregation of duties

- No preparer or accounting agent may approve its own proposal.
- Approval authority follows assigned role and responsibility.
- Approval is separate from posting.
- Independent verification is required after a posting action.

## Scope boundaries

- Source-book identity and accounting period are preserved.
- Restricted-fund purpose is tested against governing authority.
- Recognition, settlement, financing, and reporting adjustments remain distinct.
- Later evidence cannot silently rewrite a prior period.

## Validation and confidence

Evidence validity and accounting-match confidence are separate. For example, a bank line must be validated before it can enter the matching process. An uncertain extraction cannot become a confident accounting conclusion.

## Exception handling

Missing evidence, ambiguity, policy conflicts, wrong roles, changed payloads, unsupported eligibility, and reconciliation differences remain visible exceptions. MFCL does not turn an unresolved issue into an assumed answer.

## Public state model

| State | Meaning |
| --- | --- |
| `AUTO_CLEARED` | Supported deterministic controls passed |
| `EXCEPTION` | Review or evidence is required |
| `PROPOSED_ADJUSTMENT` | A non-posting treatment has been assembled |
| `APPROVED_NOT_POSTED` | An authorized human approved; nothing has posted yet |
| `POSTED_VERIFIED` | A controlled posting was independently re-read and verified |

