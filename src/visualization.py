import matplotlib.pyplot as plt
from src.metrics import top_players

def plot_top_players(df, n=10):
    """
    Gera um gráfico de barras horizontais com os top N jogadores
    com base na pontuação (Score).

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados dos jogadores, incluindo a coluna 'Score'.

    n : int, optional
        Número de jogadores a serem exibidos no gráfico (default é 10).

    Returns
    -------
    None
        A função apenas exibe o gráfico.
    """

    top_df = top_players(df, n)

    if top_df is None:
        print("Erro: não foi possível obter os top jogadores.")
        return

    plt.barh(top_df['Nome_Jogador'], top_df['Score'])

    plt.xlabel('Pontuação')
    plt.ylabel('Jogadores')
    plt.title('Top Jogadores por Performance')

    plt.tight_layout()
    plt.show()


def plot_goals_vs_assists(df):
    """
    Gera um gráfico de dispersão (scatter plot) mostrando a relação
    entre gols e assistências dos jogadores.

    Cada ponto representa um jogador, e seu nome é exibido no gráfico.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados dos jogadores. Deve possuir as
        colunas 'Gols', 'Assistencias' e 'Nome_Jogador'.

    Returns
    -------
    None
        A função apenas exibe o gráfico.
    """

    plt.scatter(df["Assistencias"], df["Gols"], alpha=0.7)

    for i, jogador in df.iterrows():
        plt.text(
            jogador["Assistencias"] + 0.1,
            jogador["Gols"] + 0.1,
            jogador["Nome_Jogador"],
            fontsize=8
        )

    plt.xlabel("Assistências")
    plt.ylabel("Gols")
    plt.title("Relação entre Gols e Assistências")

    plt.grid(True)
    plt.tight_layout()
    plt.show()