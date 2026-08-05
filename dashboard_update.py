import json
import os
from datetime import datetime

SIGNAL_FILE = "signals.json"

def update_dashboard(data=None):
    try:
        if data is not None:
            with open(SIGNAL_FILE, "w") as f:
                json.dump(data, f, indent=4)
            return data

        if not os.path.exists(SIGNAL_FILE):
            return {
                "pair": "ETH/USD",
                "signal": "WAIT",
                "confidence": 0,
                "time": "Starting",
                "reason": "Waiting for market data"
            }

        with open(SIGNAL_FILE, "r") as f:
            return json.load(f)

    except Exception as e:
        print("Dashboard error:", e)
        return {
            "pair": "ETH/USD",
            "signal": "WAIT",
            "confidence": 0,
            "time": "Error",
            "reason": str(e)
        }
