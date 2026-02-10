import joblib
import numpy as np
import pandas as pd
from model.confidence import confidence_interval
from ev.calculator import expected_value
from features.league_encoder import encode_league
from database import conn

MODEL_PATH = "model/btts_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def fetch_upcoming_matches():
    q = """
    SELECT DISTINCT match_id, league, home, away
    FROM odds
    WHERE DATE(ts) = DATE('now')
    """
    return pd.read_sql(q, conn)

def build_feature_vector(match):
    # Pull recent stats
    q = """
    SELECT home_goals, away_goals, btts
    FROM matches
    WHERE home = ? OR away = ?
    ORDER BY date DESC LIMIT 10
    """
    data = pd.read_sql(q, conn, params=(match.home, match.away))

    if len(data) < 5:
        return None

    features = {
        "home_avg_scored": data.home_goals.mean(),
        "away_avg_scored": data.away_goals.mean(),
        "btts_rate": data.btts.mean(),
        "league_code": encode_league(match.league)
    }

    return np.array(list(features.values())).reshape(1, -1)

def predict_today():
    model = load_model()
    matches = fetch_upcoming_matches()
    results = []

    for _, m in matches.iterrows():
        X = build_feature_vector(m)
        if X is None:
            continue

        prob = model.predict_proba(X)[:,1]
        mean, ci = confidence_interval(prob)

        odds_q = """
        SELECT AVG(btts_yes) as odds
        FROM odds WHERE match_id=?
        """
        odds = pd.read_sql(odds_q, conn, params=(m.match_id,)).odds.iloc[0]
        ev = expected_value(mean, odds)

        results.append({
            "match": f"{m.home} vs {m.away}",
            "league": m.league,
            "probability": round(mean, 3),
            "confidence_low": round(ci[0], 3),
            "confidence_high": round(ci[1], 3),
            "odds": round(odds, 2),
            "ev": round(ev, 3)
        })

    df = pd.DataFrame(results)
    df.to_csv("outputs/daily_predictions.csv", index=False)
    return results
