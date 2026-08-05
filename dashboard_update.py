import json
import os
from datetime import datetime

SIGNAL_FILE = "signals.json"

def update_dashboard():
    try:
        if not os.path.exists(SIGNAL_FILE):
            return {
                "pair": "ETH/USD",
                "signal": "WAIT",
                "confidence": 0,
                "time": "Starting",
                "reason": "Waiting for market data"
            }

        with open(SIGNAL_FILE, "r") as f:
            data = json.load(f)

        return {
            "pair": data.get("pair", "ETH/USD"),
            "signal": data.get("signal", "WAIT"),
            "confidence": data.get("confidence", 0),
            "time": data.get(
                "time",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),
            "reason": data.get(
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


if __name__ == "__main__":
    print(update_dashboard())
