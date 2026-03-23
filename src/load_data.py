import pandas as pd
from src.logger import get_logger

logger = get_logger(__name__)

def load_players_data(path: str):
    try:
        df = pd.read_csv(path)
        logger.info(f"Dataset carregado com sucesso: {path} ({len(df)} jogadores)")
        return df
    except FileNotFoundError:
        logger.error(f"Arquivo não encontrado: {path}")
        return None
    except Exception as e:
        logger.error(f"Erro inesperado ao carregar dados: {e}", exc_info=True)
        return None