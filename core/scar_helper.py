#!/usr/bin/env python3
"""
ScarHelper — Thin sovereign wrapper around SCAR immutable logger.
Real implementation. Appends to append-only SHA-512 chained log.
"""

import json
import os
from datetime import datetime

class ScarHelper:
    def __init__(self, log_path: str = "scar_chain.log"):
        self.log_path = log_path
        if not os.path.exists(log_path):
            with open(log_path, "w") as f:
                f.write(json.dumps({"event": "scar_chain_init", "timestamp": datetime.utcnow().isoformat()}) + "\n")

    def append(self, entry: dict):
        entry["timestamp"] = datetime.utcnow().isoformat()
        entry["chain_prev"] = self._get_last_hash()
        line = json.dumps(entry, sort_keys=True)
        with open(self.log_path, "a") as f:
            f.write(line + "\n")
        return self._compute_hash(line)

    def _get_last_hash(self) -> str:
        if not os.path.exists(self.log_path):
            return "genesis"
        with open(self.log_path, "r") as f:
            lines = f.readlines()
        if not lines:
            return "genesis"
        last = lines[-1].strip()
        return self._compute_hash(last)

    def _compute_hash(self, data: str) -> str:
        import hashlib
        return hashlib.sha512(data.encode()).hexdigest()[:32]
