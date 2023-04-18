from api.models import Base, Movie, Producer
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from typing import List
from api.utils import create_dict

DB_FILE = 'data/database.db'
engine = create_engine(f'sqlite:///{DB_FILE}')

db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
       Inicia o banco de dados com os dados contidos no arquivo CSV movielist.csv.
       Se o banco de dados já estiver preenchido, não faz nada.
    """
    CSV_FILE = 'data/movielist.csv'
    Base.metadata.create_all(bind=engine)
    with db_session() as session:
        try:
            if session.query(Movie).count():
                return
        except:
            pass
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            year = int(row['year'])
            title = row['title']
            if not title:
                continue
            studios = row['studios']
            winner = row['winner'].lower() == 'yes'
            producers = row['producers'].replace(' and ', ',').replace(',,', ',').split(',')
            movie = Movie(year=year, title=title, studios=studios, winner=winner)
            for name in producers:
                name = name.strip()
                if name:
                    try:
                        producer = session.query(Producer).filter_by(name=name).first()
                        if not producer:
                            producer = Producer(name=name)
                    except Exception:
                        producer = Producer(name=name)
                    movie.producers.append(producer)
            session.add(movie)
            session.commit()


def get_all_producers(populate: bool) -> List[Producer]:
    """
        Retorna uma lista de todos os produtores presentes no banco de dados.

        Args:
            populate (bool): Se True, os filmes de cada produtor serão carregados juntamente com as informações dos produtores.

        Returns:
            List[Producer]: lista de produtores. Se populate for True, cada produtor terá seus filmes carregados no atributo 'movies'.
    """
    with db_session() as session:
        if populate:
            producers = session.query(Producer).options(joinedload(Producer.movies)).all()
        else:
            producers = session.query(Producer).all()
        return producers


def get_producers_awards_interval_max_min() -> List[dict]:
    """
       Retorna uma lista com os produtores que tiveram o maior e o menor intervalo
       de anos entre dois prêmios consecutivos.

       Returns:
           List[dict]: lista contendo os dicionários com informações dos produtores
               com o maior e o menor intervalo de anos entre prêmios consecutivos
    """
    producers = get_all_producers(True)
    max_interval = 0
    max_interval_producers = []
    min_interval = float('inf')
    min_interval_producers = []
    for producer in producers:
        if len(producer.movies) < 2:
            continue
        prev_win = None
        for movie in producer.movies:
            if movie.winner:
                if prev_win is not None:
                    interval = movie.year - prev_win
                    if interval > max_interval:
                        max_interval = interval
                        max_interval_producers = [create_dict(producer.name, interval, prev_win, movie.year)]
                    elif interval == max_interval:
                        max_interval_producers.append(create_dict(producer.name, interval, prev_win, movie.year))
                    if interval < min_interval:
                        min_interval = interval
                        min_interval_producers = [create_dict(producer.name, interval, prev_win, movie.year)]
                    elif interval == min_interval:
                        min_interval_producers.append(create_dict(producer.name, interval, prev_win, movie.year))
                prev_win = movie.year
    result = {}
    if max_interval_producers:
        result['max'] = max_interval_producers
    if min_interval_producers:
        result['min'] = min_interval_producers
    return result
