import pandas as pd
import pytest
from src.metrics import (
    calculate_player_score,
    calculate_efficiency,
    normalize_columns,
    calculate_advanced_score,
)

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "Nome_Jogador": ["Jogador A", "Jogador B"],
        "Gols": [10, 0],
        "Assistencias": [5, 3],
        "Minutos_Jogados": [1000, 0],  # 0 minutos → edge case
    })

def test_calculate_player_score(sample_df):
    result = calculate_player_score(sample_df)
    assert result["Score"].iloc[0] == (10 * 4) + (5 * 3)  # 55

def test_efficiency_does_not_produce_inf(sample_df):
    result = calculate_efficiency(sample_df)
    assert not result["Efficiency"].isin([float("inf")]).any()
    assert not result["Efficiency"].isna().any()

def test_normalize_columns_range(sample_df):
    result = normalize_columns(sample_df)
    assert result["Gols_norm"].between(0, 1).all()
    assert result["Assistencias_norm"].between(0, 1).all()