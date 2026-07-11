---
name: GitHub Tools Collaboration
description: Controlled multi-agent software collaboration using GitHub branches, commits, reviews, and audit trails.
---

# GitHub Tools Collaboration

## Purpose
Enable controlled multi-agent software collaboration using GitHub as the source of truth. All agents, automation, and human contributors operate through accountable branches, commits, reviews, and audit trails.

## Core Principles

### Branch Isolation
- Never push directly to main.
- Every agent must work from a dedicated branch.
- Branch names must identify ownership and purpose.

### Pull Request Workflow
1. Issue / Task
2. Create Branch
3. Implement Change
4. Run CI Validation
5. Create Pull Request
6. Review
7. Merge
8. Audit Record

### Agent Accountability
Every contributor must provide:
- Branch identity
- Commit history
- Change summary
- Test results
- Security impact
- Rollback path

### Required Commit Style
Use: `type(scope): description`

Examples:
- `feat(gateway): add JWT validation middleware`
- `fix(trust): quarantine invalid CA fingerprints`
- `test(attestation): add PQC verification tests`
- `security(policy): enforce RBAC boundary checks`

### GitHub Tool Permissions
Allowed operations:
- Read repositories
- Inspect branches
- Read issues
- Create branches
- Modify files on feature branches
- Create pull requests
- Comment on reviews
- Run CI workflows
- Inspect security findings

Restricted operations:
- Direct main branch writes
- Destructive repository changes
- Removing audit history
- Bypassing required reviews

### Collaboration Roles
- **Architect Agent**: system design, interfaces, dependency decisions, security boundaries
- **Coding Agent**: implementation, tests, documentation, commit hygiene, security
- **Security Agent**: vulnerability review, cryptographic validation, supply-chain checks
- **Judge Agent**: final quality review, risk scoring, merge recommendation

## Required PR Template
```md
## Summary
What changed?

## Motivation
Why is this required?

## Security Impact
Does this affect:
- Authentication
- Authorization
- Cryptography
- Data handling
- Supply chain

## Testing
Tests executed:

## Rollback
How to revert safely:

## Reviewers
Required:
- Human owner
- Security review
- CI approval
```

## Audit Requirements
Every meaningful action should produce:
- timestamp
- actor
- branch
- commit
- action
- result
- hash

Example:
```json
{
  "actor": "agent-codex",
  "action": "pull_request_created",
  "branch": "feat/gateone-ai-control-plane",
  "status": "pending_review",
  "integrity": "sha512"
}
```

## Goal
Maintain a transparent, reversible, multi-agent engineering environment where every change is attributable, reviewable, and recoverable.
