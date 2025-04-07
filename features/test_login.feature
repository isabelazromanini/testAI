Feature: Teste de Login
  Como um usuário
  Eu quero acessar a página de login
  Para poder autenticar minha conta

  Scenario: Login bem-sucedido
    Given que estou na página de login
    When eu insiro um email válido "testeisabelaromanini@teste.com" e a senha "Test@2123"
    And clico no botão de login
    Then eu devo ser redirecionado para o dashboard
  
  Scenario: Login email invalido
    Given que estou na página de login
    When eu insiro um email inválido "blablabla@teste.com" e a senha "Test@2123"
    And clico no botão de login
    Then deve retornar o erro "A user could not be found with this email address."
