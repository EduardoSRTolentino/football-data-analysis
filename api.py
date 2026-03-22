from fastapi import FastAPI
from fastapi import HTTPException
from src.config import settings
from src.schemas import Player
from typing import List
from functools import lru_cache
from src.load_data import load_players_data
from src.metrics import (
    calculate_player_score,
    calculate_efficiency,
    normalize_columns,
    calculate_advanced_score,
    top_players
)

app = FastAPI()
VALID_METRICS = ["Score", "Advanced_Score", "Efficiency"]


@lru_cache()
def process_data():
    """
    Processa e cacheia os dados para evitar recomputação a cada requisição.
    Use /refresh para limpar o cache manualmente.
    """
    df = load_players_data(settings.DATASET_PATH)

    if df is None:
        return None

    df = calculate_player_score(df)
    df = calculate_efficiency(df)
    df = normalize_columns(df)
    df = calculate_advanced_score(df)

    return df


# 🔹 Rota inicial (teste)
@app.get("/")
def home():
    return {"message": "API de jogadores funcionando"}


# 🔹 Endpoint: listar jogadores
@app.get("/players", response_model=List[Player])
def get_players(
    limit: int = 10,
    min_gols: int = 0,
    min_assistencias: int = 0
):
    df = process_data()

    if df is None:
        return []

    # 🔥 filtros
    df = df[
        (df["Gols"] >= min_gols) &
        (df["Assistencias"] >= min_assistencias)
    ]

    df = df.sort_values("Advanced_Score", ascending=False)
    return df.head(limit).to_dict(orient="records")

@app.get("/top_players", response_model=List[Player])
def get_top_players(
    metric: str = "Advanced_Score",
    limit: int = 10,
    min_gols: int = 0
):
    df = process_data()

    if df is None:
        return []

    if metric not in VALID_METRICS:
        raise HTTPException(
            status_code=400,
            detail=f"Métrica inválida. Use: {VALID_METRICS}"
        )

    # 🔥 filtro antes do ranking
    df = df[df["Gols"] >= min_gols]

    top_df = top_players(df, n=limit, by=metric)

    return top_df.to_dict(orient="records")

@app.post("/refresh")
def refresh_data():
    process_data.cache_clear()
    return {"message": "Cache limpo com sucesso"}