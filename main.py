from database import init_db
from model.predict import predict_today
from ev.calculator import expected_value
from alerts.telegram import send
import yaml

config = yaml.safe_load(open("config.yaml"))

def run_pipeline():
    init_db()
    predictions = predict_today()

    for p in predictions:
        ev = expected_value(p["prob"], p["odds"])
        if ev > config["min_ev"] and p["confidence"] > config["confidence_min"]:
            if config["telegram"]["enabled"]:
                send(
                    f"BTTS ALERT\n{p['match']}\nEV: {ev:.2f}",
                    config["telegram"]["bot_token"],
                    config["telegram"]["chat_id"]
                )
