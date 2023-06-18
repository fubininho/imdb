import pylenium.driver as pylenium
import pytest
import time

def test_create_user(py: pylenium.Pylenium):
    py.visit('http://127.0.0.1:5000/')

    sign_up = py.get('a[href="/usuario/cadastrar_usuario"]')
    sign_up.click()

    email = py.getx("//*[text()='Email:']").parent().get('input')
    email.clear()
    random_email = py.fake.email()
    email.type(random_email)

    password = py.getx("//*[text()='Senha:']").parent().get('input')
    password.clear()
    password.type('123456')

    username = py.getx("//*[text()='Username:']").parent().get('input')
    username.clear()
    random_username = py.fake.user_name()
    username.type(random_username)

    #clicks in submit
    submit = py.get('input[type="submit"]')
    submit.click()

    assert py.contains('Seja bem vindo!')

    sign_in = py.get('a[href="/login"]')
    sign_in.click()

    email = py.getx("//*[text()='Email:']").parent().get('input')
    email.clear()
    email.type(random_email)

    password = py.getx("//*[text()='Senha:']").parent().get('input')
    password.clear()
    password.type('123456')

    #clicks in submit
    submit = py.get('input[type="submit"]')
    submit.click()

    assert py.contains(f'Bem vindo, {random_username}!')


def test_create_user_with_wrong_password(py: pylenium.Pylenium):
    py.visit('http://127.0.0.1:5000/')
    sign_up = py.get('a[href="/usuario/cadastrar_usuario"]')
    sign_up.click()

    email = py.getx("//*[text()='Email:']").parent().get('input')
    email.clear()
    random_email = py.fake.email()
    email.type(random_email)

    password = py.getx("//*[text()='Senha:']").parent().get('input')
    password.clear()
    password.type('123456')

    username = py.getx("//*[text()='Username:']").parent().get('input')
    username.clear()
    random_username = py.fake.user_name()
    username.type(random_username)

    #clicks in submit

    submit = py.get('input[type="submit"]')
    submit.click()

    assert py.contains('Seja bem vindo!')

    sign_in = py.get('a[href="/login"]')

    sign_in.click()

    email = py.getx("//*[text()='Email:']").parent().get('input')
    email.clear()
    email.type(random_email)

    password = py.getx("//*[text()='Senha:']").parent().get('input')
    password.clear()
    password.type('1234567')

    #clicks in submit
    submit = py.get('input[type="submit"]')

    submit.click()

    assert py.contains('O usuário ou senha são inválidos')
