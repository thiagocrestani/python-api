from fastapi import APIRouter
from api.database import get_producers_awards_interval_max_min

router = APIRouter()
@router.get('/producers_max_min_interval')
def get_producers_max_min_interval():
    """
        Endpoint responsável por retornar o maior e o menor intervalo de anos em que produtores de filmes ganharam prêmios consecutivos.
        Retorna um dicionário com a lista de produtores que ganharam prêmios em um intervalo máximo e mínimo, juntamente com as informações sobre esses prêmios.

        Exemplo de resposta:

        {
            "max": [
                {
                    "producer": "Matthew Vaughn",
                    "interval": 13,
                    "previousWin": 2002,
                    "followingWin": 2015
                }
            ],
            "min": [
                {
                    "producer": "Joel Silver",
                    "interval": 1,
                    "previousWin": 1990,
                    "followingWin": 1991
                }
            ]
        }

        O campo "max" contém a lista de produtores com o maior intervalo entre seus prêmios consecutivos.
        O campo "min" contém a lista de produtores com o menor intervalo entre seus prêmios consecutivos.
    """
    result = get_producers_awards_interval_max_min()
    if result:
        return result
    else:
        return {'message': 'No data found.'}






