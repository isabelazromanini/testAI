*** Settings ***
Library    SeleniumLibrary
Resource   ../keywords/login_kws.robot
Suite Setup    Abrir Navegador  ${URL}  
Suite Teardown    Fechar Navegador

*** Variables ***
${URL}        https://the-internet.herokuapp.com/login
${USERNAME_VALIDO}    tomsmith
${SENHA_VALIDA}    SuperSecretPassword!
${USERNAME_INVALIDO}    testeteste
${MSG_ERRO_USERNAME_INVALIDO}    teste

*** Test Cases ***
Login Bem-Sucedido
    Dado que estou na página de login
    Quando eu insiro o username    ${USERNAME_VALIDO}
    E eu insiro a senha            ${SENHA_VALIDA}
    E clico no botão de login
    Então eu devo ser redirecionado para o dashboard

Login Username Inválido
    Dado que estou na página de login
    Quando eu insiro o username    ${USERNAME_INVALIDO}
    E eu insiro a senha            ${SENHA_VALIDA}
    E clico no botão de login
    Então deve retornar o erro     ${MSG_ERRO_USERNAME_INVALIDO}