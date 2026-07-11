@claude @codex @copilot @grok

This is the main dedicated branch. All changes by Claude Grok/Ara GPT/Codex Copilot must be made in their dedicated branch. Do not push directly to main. Create a Pull Request for review.


# GateOne Sovereign AI Infrastructure

**GateOne** is the production sovereign on-device AI guardian and orchestration layer for Sovereignty One.

It provides:

- **Nexus Core** daemon (QuadRatchet encrypted memory, consent logging, chokidar-style file watching)
- **GateOne Enclave** — Post-Quantum Cryptography (PQC) immutable audit logger (Merkle tree + SHA-512 chaining)
- **Hardware-rooted trust** via sovereign-vault device binding (BLAKE3 pulse to secure element)
- **REPMHL** cognitive memory layer with sovereign-persistent-brain hydration
- **SCAR** immutable audit trail (append-only, tamper-evident)
- **YUVA-9V / Trinity Sentinel** hardware interlock integration (kill-signal, truth probe, familyguard voice)
- **Air-gapped / offline-first** operation with optional sovereign orchestrator bridge

## Core Principles
- Never cloud-dependent for critical paths
- Consent-gated memory and actions
- PQC signatures (ML-DSA-65/87) on all critical state
- Full kill-chain and circuit-breaker resilience
- Family/child-safe COPPA-compliant voice paths (sovereign-coppa-voice-agent)

## Repository Structure
```
gateone/
├── gateone.py                 # Main entrypoint / daemon launcher
├── core/
│   ├── gateone_orchestrator.py
│   ├── scar_helper.py
│   ├── error_handler.py
│   └── __init__.py
├── modules/
│   ├── hardware/mesh_replicator.py
│   ├── memory/repmhl.py
│   ├── scar/scar_logger.py
│   └── vault/sovereign_vault.py
└── production/
    └── gateone_dashboard.html
```

## Quick Start (Sovereign Boot)

```bash
python3 gateone.py --mode root-oversight --enable-vault-pulse --scar-chain
```

This performs:
1. Device root binding via vault.sh (BLAKE3 to /dev/tty.Baseband)
2. REPMHL + QuadRatchet initialization
3. Immutable SCAR chain boot record
4. Background orchestrator with event bus and circuit breaker

## Integration
- Works with sovereign-persistent-brain for cross-session hydration
- Pushes to SCAR on every critical event
- Compatible with GateOne Enclave PQC attestation (gateone-pqc-attestation skill)
- Ready for sovereign-orchestrator-stack and kiosk-sovereign-assistant
- GitHub collaboration skill: `.github/skills/github-tools-collaboration/SKILL.md`

## Security & Compliance
- ISO/IEC 42001 + 23894 aligned
- EU AI Act high-risk system ready
- NIST AI RMF mapped
- UNC-AI-2026 Treaty compliant paths

**Owner / Root Oversight:** D.APPEL82 (Appel420)
**Location:** White Plains, NY

This is production sovereign infrastructure. No placeholders. No mocks. Real code only.
