from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()  # carrega o .env automaticamente

class Settings:
    DATASET_PATH: str = os.getenv("DATASET_PATH", "dataset/players.csv")
    OUTPUT_PATH: str = os.getenv("OUTPUT_PATH", "output/top_players.csv")
    TOP_PLAYERS_LIMIT: int = int(os.getenv("TOP_PLAYERS_LIMIT", 10))

class Settings:
    ALLOWED_ORIGINS: list = os.getenv("ALLOWED_ORIGINS", "*").split(",")

settings = Settings()