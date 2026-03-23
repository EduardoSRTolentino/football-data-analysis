import matplotlib.pyplot as plt
from src.metrics import top_players

def plot_top_players(df, n=10, by="Advanced_Score", save_path: str = None):
    """
    Plota os top N jogadores com base em uma métrica escolhida.
    """
    top_df = top_players(df, n, by)

    if top_df is None:
        return

    plt.barh(top_df['Nome_Jogador'], top_df[by])
    plt.xlabel(by)
    plt.ylabel('Jogadores')
    plt.title(f'Top Jogadores por {by}')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    else:
        plt.show()

    plt.close()  # limpa o gráfico da memória


def plot_goals_vs_assists(df, save_path: str = None):
    plt.scatter(df["Assistencias"], df["Gols"], alpha=0.7)

    for row in df.itertuples():
        plt.text(
            row.Assistencias + 0.1,
            row.Gols + 0.1,
            row.Nome_Jogador,
            fontsize=8
        )

    plt.xlabel("Assistências")
    plt.ylabel("Gols")
    plt.title("Relação entre Gols e Assistências")
    plt.grid(True)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    else:
        plt.show()

    plt.close()