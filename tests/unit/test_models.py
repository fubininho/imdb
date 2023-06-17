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

def test_new_avaliacao():
    avaliacao = Avaliacao("Titulo","Corpo",5,"1","1")
    assert avaliacao.titulo == "Titulo"
    assert avaliacao.corpo == "Corpo"
    assert avaliacao.estrelas == 5
    assert avaliacao.id_filme == "1"
    assert avaliacao.id_usuario == "1"

def test_new_avaliacao_with_fixture(new_avaliacao):
    assert new_avaliacao.titulo == "Titulo"
    assert new_avaliacao.corpo == "Corpo"
    assert new_avaliacao.estrelas == 5
    assert new_avaliacao.id_filme == "1"
    assert new_avaliacao.id_usuario == "1"
