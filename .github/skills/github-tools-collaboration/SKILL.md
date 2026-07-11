---
name: GitHub Tools Collaboration v2
description: Owner-controlled, local-first collaboration for human, AI, and automation contributors.
---

# GitHub Tools Collaboration v2 — Local-First, Owner-Controlled

## Purpose

GitHub is used as a review and source-control record. It does not replace the repository owner's local development, CI, infrastructure, or authority.

The repository owner controls policies, credentials, CI providers, data sharing, approvals, and merges. Agents and automation are contributors with limited permissions, not autonomous owners.

## Local-First Policy

- Local CI is the primary validation authority.
- Cloud CI and hosted scanners are optional and require explicit owner approval.
- Core validation must work offline or with locally controlled tools whenever practical.
- No policy may require GitHub Actions, SaaS scanners, hosted SBOM services, telemetry, or third-party artifact upload unless the owner enables it in a reviewed change.
- No source code, prompts, logs, test artifacts, secrets, or build outputs may be exported to a third party automatically.
- A contributor must not change CI providers, required checks, network access, or data-export behavior without an owner-approved PR.
- PRs must distinguish local checks from optional cloud checks.
- Locally produced, reproducible validation evidence is acceptable when cloud services are unavailable.
- The policy defines required outcomes, not a vendor-specific implementation.

## Explicit Controls

- All material decisions and approvals must be recorded in repository artifacts such as commits, PRs, reviews, or ADRs.
- Every merge to a protected branch must include a documented rollback path.
- Protected branches require explicit human approval; AI and bot identities cannot self-merge.
- No hidden service, credential, network callback, telemetry collector, or automatic remote upload may be introduced by this policy.

## Contributor Identity

Every human, AI, and automation contributor must have a distinct repository identity and declared permissions. Anonymous or shared bot identities are not permitted for accountable changes.

Example:

```yaml
id: copilot-github
 type: ai
 role: Coding
 provider: GitHub Copilot
permissions:
  create_branch: true
  commit: true
  open_pr: true
  review: true
  merge: false
  delete_branch: false
status: active
```

Maintain identities in `CONTRIBUTORS.ai.yaml`. Public-key fields are declarative metadata until the repository owner configures actual signing and verification infrastructure; placeholders must not be treated as verified keys.

## Branch Convention

Never write directly to a protected default branch. Use a dedicated branch named:

```text
<type>/<contributor>/<issue-or-scope>
```

Allowed types: `feat`, `fix`, `security`, `docs`, `refactor`, `research`, and `collab`.

Examples:

- `collab/github-services`
- `feat/copilot/identity-vault`
- `security/dependabot/dependency-update`

## Workflow

1. Issue or task
2. Dedicated branch
3. Implementation
4. Local CI validation
5. Pull request
6. Required review
7. Human approval
8. Merge by an authorized human or explicitly authorized mechanism
9. Audit and rollback record

## Commit Requirements

Use `type(scope): description`, for example:

- `feat(gateway): add JWT validation middleware`
- `fix(trust): quarantine invalid CA fingerprints`
- `docs(policy): document local CI requirements`

Commits must identify the contributor, summarize changes, report tests actually run, state security impact, and identify a rollback path. Never claim tests or scans that were not executed.

## Provenance and Decision Records

Each PR should include `docs/templates/provenance.yaml` or equivalent metadata identifying:

- creator
- reviewers
- validator
- human approver
- source branch and commits
- local checks and optional cloud checks
- integrity digest, if configured

Significant architectural or security decisions should use an ADR in `docs/adr/`, recording context, alternatives, selected solution, rationale, risks, and approval.

## Review Matrix

| Reviewer | Responsibility |
|---|---|
| Architect | Architecture and boundaries |
| Coding | Implementation and tests |
| Security | Secrets, cryptography, dependencies, and supply chain |
| Judge | Quality and risk synthesis |
| Human owner | Final authority and merge approval |

No contributor may be the sole approver of its own work. Security review is required for security-sensitive changes.

## Local Security Gate

The owner may implement these gates with local tools:

1. Secret scan
2. Dependency scan
3. SBOM generation
4. License check
5. PQC validation when applicable
6. Unit tests
7. Integration tests
8. Threat-model review
9. Human approval

A failing required local gate blocks merge. The exact tools and commands belong to the repository owner and must not be silently changed by an agent.

## Attribution and Audit

Record meaningful actions through repository-visible commits, PRs, reviews, ADRs, and audit artifacts. Records should include timestamp, contributor, branch, commit, action, result, and digest when configured.

Line-level or function-level attribution is optional unless required by the owner; ordinary Git history remains the default source of authorship. Do not imply cryptographic verification where only metadata exists.

## Rollback Certificate

Every protected-branch merge should record:

```yaml
rollback:
  merged_commit: ""
  previous_commit: ""
  migration_required: false
  database_impact: none
  risk: low
  rollback_steps: []
```

## Risk Assessment

PRs should assess security, architecture, tests, complexity, dependencies, secrets, supply chain, and documentation. Scores are advisory unless the owner explicitly makes them merge gates.

## AI and Automation Rules

Every AI or automation contributor must explain changes, state assumptions and uncertainty, report only tests actually run, identify external references, respect permissions, and never bypass review or self-approve a merge.

## Repository Memory

Issues, PRs, ADRs, tests, reviews, provenance, and rollback records provide the repository's durable engineering context. This does not authorize external synchronization or cloud storage.

## Required PR Sections

```md
## Summary
## Motivation
## Security Impact
## Local Validation
## Optional Cloud Validation
## Provenance
## Risk Assessment
## Rollback
## Required Reviewers
```

## Goal

Provide transparent, reviewable, owner-controlled collaboration without forced cloud dependencies, hidden execution, automatic data export, or autonomous merge authority.
