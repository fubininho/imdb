from imdb.filme.models import Avaliacao

def test_media_avaliacao_filme():
    avaliacao_0 = Avaliacao("Titulo","Corpo",4,"2","1")
    avaliacao_1 = Avaliacao("Titulo","Corpo",4,"2","1")
    assert (avaliacao_0.estrelas + avaliacao_1.estrelas)/2 == 4

def test_media_avaliacao_filme_with_fixture(new_avaliacao, avaliacao_0, avaliacao_1):
    assert (avaliacao_0.estrelas + avaliacao_1.estrelas)/2 == 4
    assert new_avaliacao.estrelas == 5
