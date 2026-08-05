@app.route("/")
def dashboard():
    signal = get_signal()

    return render_template(
        "index.html",
        data={
            "pair": signal.get("pair", "ETH/USD"),
            "signal": signal.get("signal", "WAIT"),
            "confidence": signal.get("confidence", "0"),
            "time": signal.get("time", "Starting"),
            "message": signal.get("message", signal.get("reason", "No signal"))
        }
    )
