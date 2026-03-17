import pandas as pd

def calculate_player_score(df):
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

    try:
        df = df.copy()
        df['Score'] = (df['Gols'] * 4) + (df['Assistencias'] * 3)
        return df

    except Exception as e:
        print(f"Erro ao calcular as pontuações: {e}")
        return None
    
def top_players(df, n=10):
    """
    Retorna os top n jogadores com base na pontuação calculada.
    """

    try:

        if 'Score' not in df.columns:
            raise ValueError("A coluna 'Score' não existe no DataFrame")

        top_df = (
            df.sort_values(by='Score', ascending=False)
              .head(n)
              .reset_index(drop=True)
        )

        return top_df

    except Exception as e:
        print(f"Erro ao obter os top jogadores: {e}")
        return None
    
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

    try:
        df = df.copy()
        df['Efficiency'] = df['Gols'] / df['Minutos_Jogados']
        return df

    except Exception as e:
        print(f"Erro ao calcular a eficiência: {e}")
        return None
    
def normalize_columns(df):
    """
    Normaliza colunas numéricas do DataFrame utilizando Min-Max Scaling.

    As colunas normalizadas são:
    - Gols
    - Assistencias
    - Minutos_Jogados

    A normalização segue a fórmula:
        (x - min) / (max - min)

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados dos jogadores.

    Returns
    -------
    pandas.DataFrame
        DataFrame com colunas normalizadas adicionadas:
        - Gols_norm
        - Assistencias_norm
        - Minutos_norm
    """

    try:
        df = df.copy()

        # --- GOLS ---
        min_gols = df["Gols"].min()
        max_gols = df["Gols"].max()

        if max_gols != min_gols:
            df["Gols_norm"] = (df["Gols"] - min_gols) / (max_gols - min_gols)
        else:
            df["Gols_norm"] = 0

        # --- ASSISTÊNCIAS ---
        min_assists = df["Assistencias"].min()
        max_assists = df["Assistencias"].max()

        if max_assists != min_assists:
            df["Assistencias_norm"] = (df["Assistencias"] - min_assists) / (max_assists - min_assists)
        else:
            df["Assistencias_norm"] = 0

        # --- MINUTOS JOGADOS ---
        min_minutos = df["Minutos_Jogados"].min()
        max_minutos = df["Minutos_Jogados"].max()

        if max_minutos != min_minutos:
            df["Minutos_norm"] = (df["Minutos_Jogados"] - min_minutos) / (max_minutos - min_minutos)
        else:
            df["Minutos_norm"] = 0

        return df

    except Exception as e:
        print(f"Erro ao normalizar colunas: {e}")
        return None