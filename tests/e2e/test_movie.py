import pylenium.driver as pylenium
import pytest
import time

def test_create_movie(py: pylenium.Pylenium):
    py.visit('http://127.0.0.1:5000/login')

    email = py.getx("//*[text()='Email:']").parent().get('input')
    email.clear()
    email.type('admin@admin.com')

    password = py.getx("//*[text()='Senha:']").parent().get('input')
    password.clear()
    password.type('admin')

    #clicks in submit
    submit = py.get('input[type="submit"]')
    submit.click()

    assert py.contains('Bem vindo, admin!')


    sign_up = py.get('a[href="/filme/adicionar/"]')
    sign_up.click()

    title = py.getx("//*[text()='Titulo:']").parent().get('input')
    title.clear()
    random_movie = py.fake.name()
    title.type(random_movie)

    id_imdb = py.getx("//*[text()='Id no IMDB:']").parent().get('input')
    id_imdb.clear()
    random_id = py.fake.user_name()
    id_imdb.type(random_id)

    director = py.getx("//*[text()='Diretor:']").parent().get('input')
    director.clear()
    director.type('Neymar Jr.')

    cast = py.getx("//*[text()='Elenco:']").parent().get('textarea')
    cast.clear()
    cast.type('Tirica, Gabriel Coutinho e Edu')

    #clicks in submit
    submit = py.get('input[type="submit"]')
    submit.click()

    assert py.contains('sucesso')


def test_evaluate_movie(py: pylenium.Pylenium):
    py.visit('http://127.0.0.1:5000/login')

    email = py.getx("//*[text()='Email:']").parent().get('input')
    email.clear()
    email.type('admin@admin.com')

    password = py.getx("//*[text()='Senha:']").parent().get('input')
    password.clear()
    password.type('admin')

    #clicks in submit
    submit = py.get('input[type="submit"]')
    submit.click()

    assert py.contains('Bem vindo, admin!')

    movies = py.get('a[href="/filme/"]')
    movies.click()

    evaluateTitanic = py.get('a[href="/filme/2/avaliar"]')
    evaluateTitanic.click()

    rating3stars = py.get('input[value="3"]')
    rating3stars.click()

    titulo = py.getx("//*[text()='Titulo:']").parent().get('input')
    titulo.clear()
    random_movie = py.fake.name()
    titulo.type(random_movie)

    comentario = py.getx("//*[text()='Corpo:']").parent().get('textarea')
    comentario.clear()
    comentario.type('Filme muito bom, recomendo!')

    #clicks in submit
    submit = py.get('input[type="submit"]')
    submit.click()

    assert py.contains('sucesso')


def test_search_movie(py: pylenium.Pylenium):
    py.visit('http://127.0.0.1:5000/filme/')

    search = py.get('input[name="busca"]')
    search.clear()
    search.type('Titanic')

    submit = py.get('button[type="submit"]')
    submit.click()

    assert py.contains('Titanic')
    
    table = py.get('table')
    rows = table.find('tr')
    assert len(rows) == 2



