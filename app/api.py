from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/predictions")
def predictions():
    return pd.read_csv("outputs/daily_predictions.csv").to_dict("records")
