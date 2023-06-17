import pytest

from imdb.filme.models import Filme, Avaliacao

@pytest.fixture(scope='module')
def new_filme():
    filme = Filme('Teste', '123456', 'Teste', 'Teste')
    return filme

@pytest.fixture(scope='module')
def new_avaliacao():
    avaliacao = Avaliacao("Titulo","Corpo",5,"1","1")
    return avaliacao
