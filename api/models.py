
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# Tabela intermediária
movie_producer = Table('movie_producer', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('producer_id', Integer, ForeignKey('producers.id'))
)


class Movie(Base):
    """
        Classe que representa um filme.

        Atributos:
        ---------
        id : int
            Identificador único do filme.
        year : int
            Ano de lançamento do filme.
        title : str
            Título do filme.
        studios : str
            Estúdios responsáveis pela produção do filme.
        winner : bool
            Indica se o filme foi vencedor de algum prêmio.
        producers : list[Producer]
            Lista dos produtores responsáveis pela produção do filme.
    """
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    title = Column(String, unique=True)
    studios = Column(String)
    winner = Column(Boolean, default=False)
    producers = relationship("Producer", secondary=movie_producer, back_populates="movies")


class Producer(Base):
    """
        Classe que representa um produtor.

        Atributos:
        ---------
        id : int
            Identificador único do produtor.
        name : str
            Nome do produtor.
        movies : list[Movie]
            Lista dos filmes produzidos pelo produtor.
    """
    __tablename__ = "producers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    movies = relationship("Movie", secondary=movie_producer, back_populates="producers")