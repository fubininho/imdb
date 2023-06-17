import pytest

from imdb.filme.models import Filme, Avaliacao

@pytest.fixture(scope='module')
def new_filme():
    filme = Filme('Teste', '123456', 'Teste', 'Teste')
    return filme
