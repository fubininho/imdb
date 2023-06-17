from imdb.filme.models import Avaliacao
from imdb import db

def test_media_avaliacao_filme():
    avaliacao_0 = Avaliacao("Titulo","Corpo",4,"2","1")
    avaliacao_1 = Avaliacao("Titulo","Corpo",4,"2","1")
    assert (avaliacao_0.estrelas + avaliacao_1.estrelas)/2 == 4

def test_media_avaliacao_filme_with_fixture(new_avaliacao, avaliacao_0, avaliacao_1):
    assert (avaliacao_0.estrelas + avaliacao_1.estrelas)/2 == 4
    assert new_avaliacao.estrelas == 5

def test_total_avaliacao():
    # cria avaliacoes
    num_avaliacoes = Avaliacao.query.count()
    avaliacao_0 = Avaliacao("Titulo","Corpo",4,"2","1")
    avaliacao_1 = Avaliacao("Titulo","Corpo",4,"2","1")
    db.session.add(avaliacao_0)
    db.session.add(avaliacao_1)
    db.session.commit()
    # checa se o total de avaliacoes aumentou
    assert Avaliacao.query.count() == num_avaliacoes + 2
    # remove avaliacoes
    db.session.delete(avaliacao_0)
    db.session.delete(avaliacao_1)
    db.session.commit()
    # checa se o total de avaliacoes voltou ao normal
    assert Avaliacao.query.count() == num_avaliacoes
