import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_get_producers_max_min_interval():
    response = client.get("/producers_max_min_interval")

    # Verifica se o serviço está online
    assert response.status_code == 200
    data = response.json()

    # Verifica se as chaves "min" e "max" estão presentes no objeto JSON de resposta
    assert "min" in data
    assert "max" in data

    # Verifica se os valores dos intervalos, anos anteriores e anos seguintes são inteiros
    for producer in data["max"] + data["min"]:
        assert isinstance(producer["interval"], int)
        assert isinstance(producer["previousWin"], int)
        assert isinstance(producer["followingWin"], int)

    # Verifica se os valores estão ordenados corretamente
    max_intervals = [p["interval"] for p in data["max"]]
    min_intervals = [p["interval"] for p in data["min"]]
    assert max_intervals == sorted(max_intervals, reverse=True)
    assert min_intervals == sorted(min_intervals)

    # Verifica se os produtores com os intervalos mínimos e máximos são únicos
    max_producers = [p["producer"] for p in data["max"]]
    min_producers = [p["producer"] for p in data["min"]]
    assert len(set(max_producers)) == len(max_producers)
    assert len(set(min_producers)) == len(min_producers)

    # verifica que realmente o max e o min estão coesos
    max_interval = response.json()["max"][0]["interval"]
    min_interval = response.json()["min"][0]["interval"]
    assert max_interval > min_interval
