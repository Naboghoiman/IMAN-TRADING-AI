import json
from datetime import datetime


def update_dashboard(result):

    data = {
        "pair": "ETH/USD",
        "signal": result.get("SIGNAL", "WAIT"),
        "confidence": str(result.get("CONFIDENCE", 0)) + "%",
        "time": str(datetime.now()),
        "message": ", ".join(result.get("REASONS", []))
    }

    with open("signals.json", "w") as f:
        json.dump(data, f, indent=4)
