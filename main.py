from src.load_data import load_players_data
from src.metrics import (
    calculate_player_score,
    calculate_efficiency,
    normalize_columns,
    calculate_advanced_score
)
from src.visualization import plot_top_players, plot_goals_vs_assists
from src.metrics import save_top_players 

def main():

    # 1. carregar dados
    df = load_players_data("dataset/players.csv")

    if df is None:
        print("Erro ao carregar os dados.")
        return

    # 2. métricas básicas
    df = calculate_player_score(df)

    # 3. eficiência
    df = calculate_efficiency(df)

    # 4. normalização
    df = normalize_columns(df)

    # 5. score avançado
    df = calculate_advanced_score(df)

    if df is None:
        print("Erro ao processar os dados.")
        return

    # 6. visualizações
    plot_top_players(df, by="Advanced_Score", save_path="output/top_players.png")
    plot_goals_vs_assists(df, save_path="output/goals_vs_assists.png")

    # 7. salvar resultado (opcional mas MUITO importante)
    save_top_players(df)

if __name__ == "__main__":
    main()