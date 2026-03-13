import matplotlib.pyplot as plt
from src.metrics import top_players

def plot_top_players(df, n=10):

    top_df = top_players(df, n)

    plt.barh(top_df['Nome_Jogador'], top_df['Score'])

    plt.xlabel('Pontuação')
    plt.ylabel('Jogadores')
    plt.title('Top Jogadores por Performance')

    plt.show()