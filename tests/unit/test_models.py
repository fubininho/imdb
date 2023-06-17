from imdb.filme.models import Filme, Avaliacao

def test_new_filme():
    """
    GIVEN a Filme model
    WHEN a new Filme is created
    THEN check the titulo, id_imdb, diretor, atores and avaliacoes fields are defined correctly
    """
    filme = Filme('Teste', '123456', 'Teste', 'Teste')
    assert filme.titulo == 'Teste'
    assert filme.id_imdb == '123456'
    assert filme.diretor == 'Teste'
    assert filme.atores == 'Teste'
    assert filme.avaliacoes == []

def test_new_filme_with_fixture(new_filme):
    """
    GIVEN a Filme model
    WHEN a new Filme is created
    THEN check the titulo, id_imdb, diretor, atores and avaliacoes fields are defined correctly
    """
    assert new_filme.titulo == 'Teste'
    assert new_filme.id_imdb == '123456'
    assert new_filme.diretor == 'Teste'
    assert new_filme.atores == 'Teste'
    assert new_filme.avaliacoes == []
