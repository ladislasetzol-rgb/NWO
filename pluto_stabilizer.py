# pluto_stabilizer.py
"""
Pluto Stabilizer – REST‑API client for stabilising the High‑IQ Magnetic Comms
(aka “Divine Comms”).

Features:
- Retrieve current magnetic field intensity from Pluto.
- Compute target intensity using a simple high‑IQ factor.
- POST the new intensity back to Pluto.
- CLI entrypoint for ad‑hoc execution.
"""

import json
import logging
import os
from typing import Any, Dict

import requests

# ---------------------------------------------------------------------------
# Configuration (environment‑driven for flexibility)
PLUTO_BASE_URL = os.getenv("PLUTO_BASE_URL", "http://pluto.local/api")
PLUTO_TOKEN = os.getenv("PLUTO_TOKEN")  # optional Bearer token
TIMEOUT = int(os.getenv("PLUTO_TIMEOUT", "5"))  # seconds

# ---------------------------------------------------------------------------
# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
def _auth_headers() -> Dict[str, str]:
    """Generate auth headers if a token is supplied."""
    if PLUTO_TOKEN:
        return {"Authorization": f"Bearer {PLUTO_TOKEN}"}
    return {}

# ---------------------------------------------------------------------------
def get_magnetic_status() -> Dict[str, Any]:
    """GET /magnetic_status – returns current intensity and timestamp."""
    url = f"{PLUTO_BASE_URL.rstrip('/')}/magnetic_status"
    resp = requests.get(url, headers=_auth_headers(), timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()

# ---------------------------------------------------------------------------
def set_magnetic_intensity(value: float) -> Dict[str, Any]:
    """POST /magnetic_intensity – send new intensity to Pluto."""
    url = f"{PLUTO_BASE_URL.rstrip('/')}/magnetic_intensity"
    payload = {"intensity": value}
    resp = requests.post(
        url,
        headers={**_auth_headers(), "Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()

# ---------------------------------------------------------------------------
def compute_target_intensity(current: float) -> float:
    """Simple heuristic: target = current * (1 + HIGH_IQ_FACTOR)."""
    HIGH_IQ_FACTOR = 0.15  # 15 % boost – can be replaced with a dynamic model
    target = current * (1 + HIGH_IQ_FACTOR)
    log.info(
        "Computed target magnetic intensity: %.4f (current=%.4f, factor=%.2f)",
        target,
        current,
        HIGH_IQ_FACTOR,
    )
    return target

# ---------------------------------------------------------------------------
def stabilize_comm() -> Dict[str, Any]:
    """Main workflow – fetch, compute, set, report."""
    try:
        status = get_magnetic_status()
        current_intensity = float(status.get("intensity", 0))
        log.info("Current magnetic intensity: %.4f", current_intensity)

        target_intensity = compute_target_intensity(current_intensity)
        response = set_magnetic_intensity(target_intensity)
        log.info("Pluto ACK: %s", response)
        return {
            "status": "success",
            "target_intensity": target_intensity,
            "pluto_response": response,
        }
    except Exception as exc:
        log.error("Stabilisation failed: %s", exc, exc_info=True)
        return {"status": "error", "error": str(exc)}

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # CLI entrypoint: `python pluto_stabilizer.py`
    result = stabilize_comm()
    print(json.dumps(result, indent=2))
