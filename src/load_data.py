import pandas as pd

def load_players_data(path):
    """
    Carrega o dataset de jogadores a partir de um arquivo CSV.

    Parameters
    ----------
    path : str
        Caminho do arquivo CSV.

    Returns
    -------
    pandas.DataFrame
        DataFrame com os dados dos jogadores.
    """

    try:
        df = pd.read_csv(path)
        return df

    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None