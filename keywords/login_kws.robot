*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Abrir Navegador
    [Arguments]    ${url}
    Open Browser    ${url}    chrome
    Maximize Browser Window

Fechar Navegador
    Close Browser

Dado que estou na página de login
    Go to   ${url}
    Page Should Contain Element    id=login

Quando eu insiro o username
    [Arguments]    ${username}
    Input Text    id=username    ${username}

E eu insiro a senha
    [Arguments]    ${senha}
    Input Text    id=password    ${senha}

E clico no botão de login
    Click Button    xpath=//button[@type="submit"]
    Sleep    1s

Então eu devo ser redirecionado para o dashboard
    Location Should Contain    secure

Então deve retornar o erro
    [Arguments]    ${mensagem_erro}
    Element Should Be Visible    id=flash
    SeleniumLibrary.Element Should Contain    id=flash    ${mensagem_erro}
