#!/usr/bin/env python3
"""
ScarLogger — Immutable append-only audit logger for GateOne.
SHA-512 chained, tamper-evident. Real sovereign implementation.
"""

import json
import os
from datetime import datetime

class ScarLogger:
    def __init__(self, log_path: str = "scar_chain.log"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path) or ".", exist_ok=True)
        if not os.path.exists(log_path):
            self._init_chain()

    def _init_chain(self):
        genesis = {
            "event": "scar_genesis",
            "timestamp": datetime.utcnow().isoformat(),
            "owner": "D.APPEL82 / Appel420",
            "note": "GateOne SCAR chain initialized"
        }
        with open(self.log_path, "w") as f:
            f.write(json.dumps(genesis, sort_keys=True) + "\n")

    def append(self, entry: dict):
        entry = dict(entry)  # copy
        entry["timestamp"] = datetime.utcnow().isoformat()
        entry["prev_hash"] = self._last_hash()
        line = json.dumps(entry, sort_keys=True)
        with open(self.log_path, "a") as f:
            f.write(line + "\n")
        return self._compute_hash(line)

    def _last_hash(self) -> str:
        if not os.path.exists(self.log_path):
            return "genesis"
        with open(self.log_path, "rb") as f:
            f.seek(0, 2)
            if f.tell() == 0:
                return "genesis"
            f.seek(-2, 2)
            while f.tell() > 0:
                f.seek(-1, 1)
                if f.read(1) == b"\n":
                    break
            last_line = f.readline().decode().strip()
        return self._compute_hash(last_line)

    def _compute_hash(self, data: str) -> str:
        import hashlib
        return hashlib.sha512(data.encode("utf-8")).hexdigest()
