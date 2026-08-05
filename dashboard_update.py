import json
import os

SIGNAL_FILE = "signals.json"

def update_dashboard(data=None):
    try:
        if data is not None:
            with open(SIGNAL_FILE, "w") as f:
                json.dump(data, f, indent=4)
            return data

        if os.path.exists(SIGNAL_FILE):
            with open(SIGNAL_FILE, "r") as f:
                return json.load(f)

        return {
            "pair": "ETH/USD",
            "signal": "WAIT",
            "confidence": 0,
            "time": "Starting",
            "message": "Waiting for market data"
        }

    except Exception as e:
        print("Dashboard error:", e)
        return {
            "pair": "ETH/USD",
            "signal": "WAIT",
            "confidence": 0,
            "time": "Error",
            "message": str(e)
        }
