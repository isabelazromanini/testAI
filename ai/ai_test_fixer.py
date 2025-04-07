import google.generativeai as genai
import os
from datetime import datetime

LOG_DIR = "logs/"

def ensure_log_dir():
    """Garante que o diretório de logs exista."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_correction(test_code, error_message, fixed_code):
    """Registra as correções feitas pela IA em um arquivo de log."""
    ensure_log_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = os.path.join(LOG_DIR, f"correction_{timestamp}.log")
    with open(log_filename, "w") as log_file:
        log_file.write("🔧 Correção de Teste\n")
        log_file.write(f"Data: {timestamp}\n\n")
        log_file.write("📂 Código Original:\n")
        log_file.write(test_code + "\n\n")
        log_file.write("⚠️ Erro:\n")
        log_file.write(error_message + "\n\n")
        log_file.write("✅ Código Corrigido:\n")
        log_file.write(fixed_code + "\n")

def fix_broken_test(test_code, error_message):
    # Captura a chave da API
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("🚨 GEMINI_API_KEY não está definida. Configure a variável de ambiente ou passe a chave diretamente.")
    
    # Configuração do modelo
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use a versão mais recente

    # Formatar a mensagem para fornecer um contexto melhor à IA
    prompt = f"""
    Você é um especialista em testes automatizados e correção de código Python com Selenium e Pytest.
    O seguinte teste apresentou um erro. Corrija o código e explique a solução de forma clara:

    **Código do Teste:**
    ```python
    {test_code}
    ```

    **Erro Encontrado:**
    ```
    {error_message}
    ```

    **Regras:**
    - Se for um problema de elemento não interagível, adicione `WebDriverWait` com `EC.visibility_of_element_located`.
    - Se for um erro de asserção, corrija o valor esperado.
    - Explique cada correção de forma objetiva.

    **Saída esperada:**
    1. Código corrigido.
    2. Explicação detalhada das correções.
    """

    # Gerar a resposta da IA
    response = model.generate_content(prompt)
    fixed_code = response.text

    # Registrar correção
    log_correction(test_code, error_message, fixed_code)
    return fixed_code
