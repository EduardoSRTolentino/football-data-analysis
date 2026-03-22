from fastapi import FastAPI
from src.load_data import load_players_data
from src.metrics import (
    calculate_player_score,
    calculate_efficiency,
    normalize_columns,
    calculate_advanced_score,
    top_players
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API funcionando"}

def process_data():
    df = load_players_data("dataset/players.csv")
    df = calculate_player_score(df)
    df = calculate_efficiency(df)
    df = normalize_columns(df)
    df = calculate_advanced_score(df)
    return df

@app.get("/players")
def get_players():
    df = process_data()
    return df.to_dict(orient="records")