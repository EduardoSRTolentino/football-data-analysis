from src.load_data import load_players_data
from src.metrics import calculate_player_score
from src.visualization import plot_top_players
from src.visualization import plot_goals_vs_assists

def main():

    df = load_players_data("dataset/players.csv")

    df = calculate_player_score(df)

    plot_top_players(df)
    plot_goals_vs_assists(df)

if __name__ == "__main__":
    main()