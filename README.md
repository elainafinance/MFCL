# Municipal Finance Control Layer

**Modernizing municipal finance without replacing the systems already in place.**

> **MFCL is not an autonomous accounting bot. It is a governed control layer that uses specialized agents to identify issues earlier while preserving source authority and human approval.**

MFCL connects existing accounting/ERP, utility billing and cashiering, banking, payroll, grants and projects, and supporting documents into one controlled municipal finance layer.

[Open the interactive Pinehaven demo](https://elainafinance.github.io/MFCL/) | [Read the LinkedIn case study](./case-study/Municipal_Finance_Control_Layer_LinkedIn_Case_Study.pdf)

## The problem

Small governments often operate across disconnected systems, spreadsheets, bank records, paper documents, and institutional knowledge. The accounting system remains authoritative, but it may not contain the complete context needed to reconcile cash, protect restricted funds, support grants, resolve interfund activity, or prepare for audit.

MFCL adds a governed layer around those existing systems. It connects evidence, applies repeatable controls, routes exceptions, and preserves human responsibility.

## The control boundary

**AI interprets context. Controls decide. People authorize.**

- AI-assisted services interpret documents, propose classifications, and assemble review packages.
- Deterministic controls perform accounting math, reconciliation, duplicate detection, restriction tests, and approval validation.
- Authorized municipal personnel verify facts, exercise judgment, approve actions, and accept management responsibility.
- Approval is separate from posting. Independent verification is required before an item is considered complete.

## Architecture at a glance

![MFCL systems architecture](./demo/screenshots/systems-architecture.png)

Existing municipal systems → controlled ingestion → normalized financial events → specialized agents and deterministic controls → required-role verification → segregation-of-duties check → controlled posting → independent re-verification → reporting, close, SEFA, and audit support.

The source systems remain the systems of record. MFCL preserves source identity, effective dates, evidence lineage, approval history, and the distinction between a proposed action, an approved action, and a verified posting.

## Public demonstration

The repository uses the fictional **City of Pinehaven** and synthetic transactions. The interactive demo shows:

- existing and legacy ERP integration;
- revenue and cashiering controls;
- bank and card reconciliation dispositions;
- restricted-fund and SPLOST purpose testing;
- reciprocal interfund recognition and settlement;
- grants, federal awards, and draft SEFA lineage;
- role-based approval and segregation of duties;
- Economic Event ID evidence lineage;
- reporting and audit-readiness concepts.

The demo is presentation-only. It contains no real municipal data, production credentials, proprietary prompts, private schemas, matching thresholds, security implementation, or posting capability.

## Validation context

The architecture was functionally tested with QuickBooks Desktop 2022 in a controlled, non-live environment. The public demo is sanitized and synthetic; it is not an audit, assurance report, legal opinion, security certification, or production accounting system.

No replacement ERP is required to use the architecture concept.

## Repository guide

- [`architecture/`](./architecture/) — Public system flow, agent map, and approval flow
- [`agents/`](./agents/) — High-level specialist-agent responsibilities
- [`controls/`](./controls/) — Human-in-the-loop, source authority, scope, validation, and exception controls
- [`demo/`](./demo/) — Pinehaven demonstration guide and public screenshots
- [`case-study/`](./case-study/) — Synthetic before-to-outcome case study and LinkedIn PDF
- [`VALIDATION.md`](./VALIDATION.md) — Public release checks and limitations
- [`PUBLISHING.md`](./PUBLISHING.md) — Free GitHub Pages and LinkedIn publishing steps

## Intellectual-property boundary

This public repository demonstrates the system's purpose, governance, control architecture, and user experience. It intentionally excludes proprietary prompts, algorithms, detailed rules, schemas, mappings, thresholds, posting/security implementation, and private validation data.

Concept, architecture, and case study by **Elaina Lockhart**.
