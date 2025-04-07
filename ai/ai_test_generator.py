import google.generativeai as genai
import os

def generate_test_code(test_description):
    """Gera código de teste automatizado com base na descrição fornecida."""

    # Captura a chave da API
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("🚨 GEMINI_API_KEY não está definida. Configure a variável de ambiente.")

    # Configuração do modelo
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Usa a versão mais recente

    # Formatar a solicitação para a IA
    prompt = f"""
    Você é um especialista em testes automatizados. Gere um código de teste automatizado em Python usando Pytest e Selenium.

    **Descrição do Teste:**
    {test_description}

    **Regras:**
    - Utilize o formato Gherkin conforme o exemplo abaixo:
    Feature: [Nome da funcionalidade]
    Como um usuário [ou papel específico]
    Eu quero [ação desejada]
    Para que [objetivo ou benefício]

    @TagRelevante
    Scenario: [Nome do Cenário]
      Given [Contexto inicial necessário]
      When [Ação realizada pelo usuário]
      And [Ação adicional, se necessário]
      Then [Resultado esperado]

    - Este projeto se trata de testes automatizados funcionais e está estruturado da seguinte forma:
    - Pasta `ai`: integração com o Gemini para corrigir erros e gerar novos cenários.
    - Pasta `features`: arquivos `.feature` com cenários escritos em Gherkin.
    - Pasta `pages`: métodos definidos para interação com elementos da interface (Page Object Model).
    - Pasta `tests`: implementação dos steps definidos no Gherkin e mapeamento para métodos da pasta `pages`.

    - Requisitos adicionais:
    - Testes devem cobrir **caminhos felizes, alternativos, negativos, segurança e performance**.
    - Utilize `WebDriverWait` com `expected_conditions` para interação com elementos.
    - O código deve ser robusto e seguir boas práticas de testes automatizados.
    - Relatórios devem ser gerados usando o Allure.
    - Sempre fornecer explicações claras e detalhadas das decisões implementadas.

    **Saída esperada:**
    1. Código do teste funcional.
    2. Explicação detalhada da lógica implementada e possíveis melhorias.
    """

    # Gerar o código do teste usando IA
    response = model.generate_content(prompt)
    return response.text

