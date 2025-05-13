import google.generativeai as genai
import os

def generate_test_code(test_description):
    """Gera código de teste em Robot Framework com base na descrição fornecida."""
    # Captura a chave da API
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("🚨 GEMINI_API_KEY não está definida. Configure a variável de ambiente.")

    # Configuração do modelo
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    # Prompt adaptado para Robot Framework
    prompt = f"""
    Você é um especialista em automação de testes utilizando Robot Framework, SeleniumLibrary, BDD e Inteligência Artificial.  
    A seguir está a descrição detalhada do projeto e sua estrutura, para que todo novo teste gerado já esteja corretamente inserido no contexto:


    **Descrição do Teste:**
    {test_description}

    ## **Formato esperado do novo teste**

    Ao gerar um novo teste, respeite exatamente esta estrutura:

    **Formato esperado:**
    *** Keywords ***
    [Defina palavras-chave reutilizáveis, se necessário.]
    - O teste deve ser executável com SeleniumLibrary.
    - Utilize palavras-chave que já existem na pasta `keywords` sempre que possível.
    - Utilize boas práticas do Robot Framework, sem usar Python diretamente.
    - Respeite a indentação e estrutura.
    - O arquivo gerado deve ser compatível para ser salvo na pasta `/tests` do projeto, com extensão `.robot`.
    - Após o código do teste, inclua uma explicação sucinta da lógica implementada.

    ---

    **Exemplo básico:**

    *** Test Cases *** Login com Sucesso Given que o usuário está na página de login When preenche o campo email com "user@exemplo.com" And preenche o campo senha com "senha123" And clica no botão de login Then o sistema exibe a mensagem "Bem-vindo"

    *** Keywords *** Usuário está na página de login Open Browser https://site.com/login chrome Maximize Browser Window
    *(Utilize este exemplo apenas como referência de formato. Use o máximo de contexto e riqueza nos passos.)*

    ---

    ## **IMPORTANTE**
    - Só gere o conteúdo do novo teste `.robot` + explicação, nada mais.
    - Utilize palavras-chave de negócio (alta legibilidade).
    - O teste precisa funcionar integrado com a estrutura do projeto, utilizando as pastas e convenções já existentes.

    ---

    **Caso precise definir uma nova keyword, coloque na seção `*** Keywords ***` do próprio arquivo. Se possível, aproveite keywords já existentes na pasta `/keywords`.**

    ---
    """

    response = model.generate_content(prompt)
    return response.text