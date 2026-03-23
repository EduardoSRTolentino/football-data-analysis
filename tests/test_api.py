from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_get_players_invalid_limit():
    response = client.get("/players?limit=-1")
    assert response.status_code == 422

def test_top_players_invalid_metric():
    response = client.get("/top_players?metric=INVALIDO")
    assert response.status_code == 400