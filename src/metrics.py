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