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
    

