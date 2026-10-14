"""
Integration for bundled custom power plans (.pow files exported via
`powercfg -export`). Unlike the NVIDIA Inspector integration, we don't need
a separate third-party tool for this - `powercfg` is built into Windows.
"""

import os
import subprocess
from core.paths import resource_path

PLANS_DIR = resource_path("data", "power_plans")

# Importing with an explicit GUID keeps it stable across imports, so we can
# always activate it afterward without having to parse powercfg's output
# to discover a freshly-assigned random GUID.
BUNDLED_PLANS = {
    "Bungus Power Plan": {
        "file": os.path.join(PLANS_DIR, "BungusPower.pow"),
        "guid": "bda12514-291a-40f4-8a13-907de7fe25c7",
    },
}


def is_available(name: str) -> bool:
    plan = BUNDLED_PLANS.get(name)
    return bool(plan) and os.path.exists(plan["file"])


def apply_plan(name: str):
    """Imports (if needed) and activates a bundled power plan. Returns (success, message)."""
    plan = BUNDLED_PLANS.get(name)
    if not plan:
        return False, f"Unknown power plan '{name}'."
    if not os.path.exists(plan["file"]):
        return False, f"'{os.path.basename(plan['file'])}' is missing from the app's data folder."

    try:
        import_result = subprocess.run(
            f'powercfg -import "{plan["file"]}" {plan["guid"]}',
            shell=True, capture_output=True, text=True, timeout=15,
        )
        # powercfg -import can harmlessly "fail" if the scheme with this GUID
        # already exists from a previous import - that's fine, just activate it.
        activate_result = subprocess.run(
            f'powercfg -setactive {plan["guid"]}',
            shell=True, capture_output=True, text=True, timeout=15,
        )
        if activate_result.returncode == 0:
            return True, f"'{name}' is now your active power plan."
        msg = activate_result.stderr.strip() or import_result.stderr.strip() or "powercfg reported an error."
        return False, msg
    except Exception as e:
        return False, str(e)
