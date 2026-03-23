import pandas as pd
from src.config import settings
from typing import Optional

def calculate_player_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a pontuação dos jogadores com base em suas estatísticas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados dos jogadores.

    Returns
    -------
    pandas.DataFrame
        DataFrame atualizado com a coluna 'Score'.
    """

    
    df = df.copy()
    df['Score'] = (df['Gols'] * 4) + (df['Assistencias'] * 3)
    return df
    
    
def top_players(df, n=10, by="Advanced_Score"):
    """
    Retorna os top N jogadores com base em uma métrica escolhida.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados dos jogadores.
    n : int, optional
        Número de jogadores a retornar (default é 10).
    by : str, optional
        Coluna usada para ordenação (default é 'Score').

    Returns
    -------
    pandas.DataFrame
        DataFrame com os top N jogadores ordenados.
    """

    
    if by not in df.columns:
        raise ValueError(f"A coluna '{by}' não existe no DataFrame")

    top_df = (
        df.sort_values(by=by, ascending=False)
            .head(n)
            .reset_index(drop=True)
    )

    return top_df
    
    
def calculate_efficiency(df):
    """
    Calcula a eficiência dos jogadores com base na relação entre gols
    marcados e minutos jogados.

    A eficiência é definida como:
        Efficiency = Gols / Minutos_Jogados

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados dos jogadores. Deve possuir as
        colunas 'Gols' e 'Minutos_Jogados'.

    Returns
    -------
    pandas.DataFrame
        DataFrame atualizado contendo uma nova coluna 'Efficiency',
        que representa a eficiência de cada jogador.

    Raises
    ------
    Exception
        Caso ocorra algum erro durante o cálculo da eficiência.
    """

    df = df.copy()
    df['Efficiency'] = df.apply(
        lambda row: row['Gols'] / row['Minutos_Jogados']
        if row['Minutos_Jogados'] > 0 else 0.0,
        axis=1
    )
    return df

def _minmax_normalize(series: pd.Series) -> pd.Series:
    min_val, max_val = series.min(), series.max()
    if max_val == min_val:
        return pd.Series(0.0, index=series.index)
    return (series - min_val) / (max_val - min_val)
    
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    cols_to_normalize = {
        "Gols": "Gols_norm",
        "Assistencias": "Assistencias_norm",
        "Minutos_Jogados": "Minutos_norm",
    }
    for source_col, target_col in cols_to_normalize.items():
        df[target_col] = _minmax_normalize(df[source_col])
    return df

    
def calculate_advanced_score(df):
    """
    Calcula um score avançado dos jogadores com base em métricas normalizadas.

    A fórmula utilizada é:
        Advanced_Score =
            (Gols_norm * 0.5) +
            (Assistencias_norm * 0.3) +
            (Efficiency * 0.2)

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contendo as colunas normalizadas e a eficiência.

    Returns
    -------
    pandas.DataFrame
        DataFrame com a coluna 'Advanced_Score' adicionada.
    """

    
    df = df.copy()

     # validações
    required_columns = ["Gols_norm", "Assistencias_norm", "Efficiency_norm"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"A coluna '{col}' não existe no DataFrame")

    # cálculo do score
    df["Advanced_Score"] = (
        (df["Gols_norm"] * 0.5) +
        (df["Assistencias_norm"] * 0.3) +
        (df["Efficiency_norm"] * 0.2)
    )

    return df

def save_top_players(df, path=settings.OUTPUT_PATH, n=settings.TOP_PLAYERS_LIMIT):
    """
    Salva os top N jogadores em um arquivo CSV.
    """

    top_df = top_players(df, n, by="Advanced_Score")

    if top_df is None:
        return

    top_df.to_csv(path, index=False)
    print(f"Arquivo salvo em: {path}")

