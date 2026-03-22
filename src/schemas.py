from pydantic import BaseModel

class Player(BaseModel):
    Nome_Jogador: str
    Gols: int
    Assistencias: int
    Minutos_Jogados: int
    Score: float
    Efficiency: float
    Advanced_Score: float