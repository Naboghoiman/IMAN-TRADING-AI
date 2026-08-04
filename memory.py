import json
from datetime import datetime

FILE = "history.json"


def save_prediction(signal, confidence, price):
    data = {
        "time": str(datetime.now()),
        "signal": signal,
        "confidence": confidence,
        "price": price,
        "result": "PENDING"
    }

    try:
        with open(FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(data)

    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)


def get_accuracy():

    try:
        with open(FILE, "r") as f:
            history = json.load(f)

        completed = [
            x for x in history
            if x["result"] != "PENDING"
        ]

        if len(completed) == 0:
            return 0

        wins = len([
            x for x in completed
            if x["result"] == "WIN"
        ])

        return round((wins / len(completed)) * 100, 2)

    except:
        return 0
