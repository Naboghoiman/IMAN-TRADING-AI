from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

SIGNAL_FILE = "signals.json"

def get_signal():
    if os.path.exists(SIGNAL_FILE):
        with open(SIGNAL_FILE, "r") as f:
            return json.load(f)

    return {
        "pair": "ETH/USD",
        "signal": "WAIT",
        "confidence": "0%",
        "time": str(datetime.now()),
        "message": "No signal yet"
    }

@app.route("/")
def dashboard():
    return render_template("index.html", data=get_signal())

@app.route("/api/signal")
def api_signal():
    return jsonify(get_signal())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
