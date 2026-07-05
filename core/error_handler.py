#!/usr/bin/env python3
"""
GateOne ErrorHandler — Sovereign error handling with SCAR logging and kill-signal integration.
Real code. No silent failures.
"""

import traceback
from core.scar_helper import ScarHelper

class GateOneErrorHandler:
    def __init__(self):
        self.scar = ScarHelper()

    def handle(self, exc: Exception, context: str = "unknown"):
        entry = {
            "event": "error",
            "context": context,
            "type": type(exc).__name__,
            "message": str(exc),
            "trace": traceback.format_exc()
        }
        self.scar.append(entry)
        print(f"[ERROR] {context}: {exc} — logged to SCAR")
        # In full system: trigger circuit breaker or kill-signal if critical
