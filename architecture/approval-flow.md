# Approval and posting flow

```mermaid
stateDiagram-v2
    [*] --> Exception
    Exception --> ProposedAdjustment: Evidence and proposed treatment assembled
    ProposedAdjustment --> Blocked: Self-approval or role conflict
    ProposedAdjustment --> ApprovedNotPosted: Required role verifies and approves
    ApprovedNotPosted --> ReapprovalRequired: Approved payload changes
    ApprovedNotPosted --> ControlledPosting: Separate service validates scope and permission
    ControlledPosting --> VerificationPending: Simulated or authorized posting completes
    VerificationPending --> PostedVerified: Independent re-read agrees
    VerificationPending --> Exception: Re-read differs
```

## Required separation

- The preparer cannot approve its own work.
- System access does not create approval authority.
- Approval is scoped to the event and approved payload.
- Approval does not equal posting.
- Posting does not equal completion until independently verified.

