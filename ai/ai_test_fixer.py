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
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write("🔧 Correção de Teste\n")
        log_file.write(f"Data: {timestamp}\n\n")
        log_file.write("📂 Código Original:\n")
        log_file.write(test_code + "\n\n")
        log_file.write("⚠️ Erro:\n")
        log_file.write(error_message + "\n\n")
        log_file.write("✅ Código Corrigido:\n")
        log_file.write(fixed_code + "\n")

def fix_broken_test(test_code, error_message):
    """Corrige testes do Robot Framework usando IA."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("🚨 GEMINI_API_KEY não está definida. Configure a variável de ambiente ou passe a chave diretamente.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    prompt = f"""
    Você é um especialista em testes automatizados escritos em Robot Framework.
    O seguinte teste apresentou um erro. Corrija o código de teste e explique a solução de forma clara.

    **Código do Teste:**
    ```robot
    {test_code}
    ```

    **Erro Encontrado:**
    ```
    {error_message}
    ```

    **Regras:**
    - Use estrutura do Robot Framework (Gherkin-style se aplicável).
    - Mantenha as boas práticas de indentação.
    - Corrija as palavras-chave incorretas ou parâmetros inválidos.
    - Retorne a versão corrigida.

    **Saída esperada:**
    1. Código corrigido.
    2. Explicação da correção.
    """
    response = model.generate_content(prompt)
    response_text = response.text.strip()

    # Tenta separar "Código Corrigido" e "Explicação"
    if "Explicação:" in response_text:
        parts = response_text.split("Explicação:", 1)
        codigo_corrigido = parts[0].strip()
        explicacao = parts[1].strip()
    else:
        codigo_corrigido = response_text
        explicacao = ""

    log_correction(test_code, error_message, codigo_corrigido)

    # Agora retorna DICIONÁRIO com os campos SEPARADOS
    return {
        "code": codigo_corrigido,
        "explanation": explicacao
    }