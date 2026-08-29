# Public release validation

Release date: 2026-08-29

## Reused completed validation

The public HTML was previously checked for:

- 20 navigation targets and 20 corresponding workspaces;
- unique interface IDs and resolved script-to-interface references;
- role separation and self-approval blocking states;
- approval-versus-posting separation and dry-run-only behavior;
- bank/card, SPLOST, interfund, SEFA, and evidence-lineage interactions;
- embedded JavaScript syntax;
- standalone operation with no required external assets;
- absence of identified private municipality names and internal filesystem paths.

## GitHub package controls

- The City of Pinehaven and all transaction examples are fictional.
- The PDF is the existing public synthetic case study and was not rewritten.
- Screenshots are rendered from the same public synthetic PDF.
- No QuickBooks company file, bank statement, accounting export, private workpaper, source manifest, private test fixture, credential, prompt, proprietary schema, matching threshold, or posting implementation is included.
- The root `index.html` remains a presentation-only simulation and cannot access or modify an ERP.

Run the public package check from the repository root:

```text
python tools/validate_public_package.py
```

The latest saved result is in `VALIDATION_RESULTS.txt`.

## Limitations

This repository demonstrates architecture and control concepts. It is not an audit, assurance report, legal opinion, peer review, security certification, or production-ready accounting system.
