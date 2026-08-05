import json
import os
from datetime import datetime

SIGNAL_FILE = "signals.json"

def update_dashboard(data=None):
    try:
        if data is not None:
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
            signal = json.load(f)

        return {
            "pair": signal.get("pair", "ETH/USD"),
            "signal": signal.get("signal", "WAIT"),
            "confidence": signal.get("confidence", 0),
            "time": signal.get(
                "time",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),
            "reason": signal.get(
                "reason",
                "No analysis available"
            )
        }

    except Exception as e:
        print("Dashboard error:", e)
        return {
            "pair": "ETH/USD",
            "signal": "WAIT",
            "confidence": 0,
            "time": "Error",
            "reason": str(e)
        }
