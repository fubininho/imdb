from imdb.usuario.models import Usuario


def test_new_usuario():
    usuario = Usuario("teste@teste.teste", "teste", "teste", "user")
    assert usuario.email == "teste@teste.teste"
    assert usuario.username == "teste"
    assert usuario.funcao == "user"


def test_new_usuario_with_fixture(new_usuario):
    assert new_usuario.email == "teste@teste.teste"
    assert new_usuario.username == "teste"
    assert new_usuario.funcao == "user"


def test_checa_senha():
    usuario = Usuario('teste@senha.com', 'senha_teste',
                      'usuario_teste', 'user')
    assert usuario.checa_senha('senha_teste') == True


def test_checa_senha_with_fixture(new_usuario):
    assert new_usuario.checa_senha('teste') == True


def test_senha_errada(new_usuario):
    assert new_usuario.checa_senha('testes') == False
