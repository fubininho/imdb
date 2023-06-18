from imdb.filme.models import Avaliacao
from imdb import db


def test_media_avaliacao_filme():
    avaliacao_0 = Avaliacao("Titulo", "Corpo", 4, "2", "1")
    avaliacao_1 = Avaliacao("Titulo", "Corpo", 4, "2", "1")
    assert (avaliacao_0.estrelas + avaliacao_1.estrelas)/2 == 4


def test_media_avaliacao_filme_with_fixture(new_avaliacao, avaliacao_0, avaliacao_1):
    assert (avaliacao_0.estrelas + avaliacao_1.estrelas)/2 == 4
    assert new_avaliacao.estrelas == 5


def teste_maior_avaliacao_filme():
    avaliacao_0 = Avaliacao("Titulo", "Corpo", 4, "1", "1")
    avaliacao_1 = Avaliacao("Titulo", "Corpo", 2, "1", "1")
    avaliacao_2 = Avaliacao("Titulo", "Corpo", 1, "1", "1")
    assert(max(avaliacao_0.estrelas, avaliacao_1.estrelas, avaliacao_2.estrelas) == 4)


def test_maior_avaliacao_filme_with_fixture(new_avaliacao, avaliacao_0, avaliacao_1):
    assert(max(avaliacao_0.estrelas, avaliacao_1.estrelas,
           new_avaliacao.estrelas) == 5)


def test_menor_avaliacao_filme():
    avaliacao_0 = Avaliacao("Titulo", "Corpo", 4, "1", "1")
    avaliacao_1 = Avaliacao("Titulo", "Corpo", 2, "1", "1")
    avaliacao_2 = Avaliacao("Titulo", "Corpo", 1, "1", "1")
    assert(min(avaliacao_0.estrelas, avaliacao_1.estrelas, avaliacao_2.estrelas) == 1)


def test_menor_avaliacao_filme_with_fixture(new_avaliacao, avaliacao_0, avaliacao_1):
    assert(min(avaliacao_0.estrelas, avaliacao_1.estrelas,
           new_avaliacao.estrelas) == 4)
