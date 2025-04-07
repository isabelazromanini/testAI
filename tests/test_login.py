import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
import pytest
import time


# Inicializar o WebDriver como uma fixture do pytest
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())  # Garante que o ChromeDriver correto será baixado
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    #driver.quit()  # Fecha o navegador no final do teste

# Fixture para criar a instância da LoginPage
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@scenario("../features/test_login.feature", "Login bem-sucedido")
def test_login_bemsucedido():
    pass

@scenario("../features/test_login.feature", "Login email invalido")
def test_login_email_invalido():
    pass

@given("que estou na página de login")
def acessar_pagina_de_login(login_page):
    login_page.open()

@when('eu insiro um email válido "testeisabelaromanini@teste.com" e a senha "Test@2123"')
def inserir_credenciais(login_page):
    login_page.login("testeisabelaromanini@teste.com", "Test@2123")

@when("clico no botão de login")
def clicar_botao_login():
    time.sleep(5)  # Simulando o tempo de resposta

@then("eu devo ser redirecionado para o dashboard")
def verificar_dashboard(login_page):
    assert login_page.is_logged_in(), "Usuário não foi redirecionado corretamente"


@when('eu insiro um email inválido "blablabla@teste.com" e a senha "Test@2123"')
def inserir_credenciais(login_page):
    login_page.login("blablabla@teste.com", "Test@2123")

@then('deve retornar o erro "A user could not be found with this email address."')
def verificar_mensagem_erro(login_page):
    assert login_page.error_email_invalid(), "Mensagem de erro não foi exibida!"
