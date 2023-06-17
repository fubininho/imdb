import pytest

from imdb.filme.models import Filme, Avaliacao
from imdb.usuario.models import Usuario

@pytest.fixture(scope='module')
def new_filme():
    filme = Filme('Teste', '123456', 'Teste', 'Teste')
    return filme

@pytest.fixture(scope='module')
def new_avaliacao():
    avaliacao = Avaliacao("Titulo","Corpo",5,"1","1")
    return avaliacao

@pytest.fixture(scope="module")
def new_usuario():
    usuario = Usuario("teste@teste.teste","teste","teste","user")
    return usuario
