import sys
import os
import pytest
import subprocess
import re
import google.generativeai as genai
from ai_test_fixer import fix_broken_test
from ai_test_generator import generate_test_code

def save_fixed_test(file_path, fixed_code):
    """Salva o código corrigido diretamente no arquivo original."""
    with open(file_path, "w") as file:
        file.write(fixed_code)

def run_pytest():
    """Executa os testes e captura falhas reais."""
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()

    result = subprocess.run(
        ["pytest", "-q", "--tb=short", "--disable-warnings", "tests/test_login.py"],
        capture_output=True, text=True, env=env, shell=True
    )

    output = result.stdout + result.stderr
    print("\n🛠 Testes Executados! Saída:\n", output)

    if result.returncode != 0:
        print("\n❌ Testes falharam!")
        return extract_failed_tests(output)
    else:
        print("\n✅ Todos os testes passaram com sucesso!")
        return []

def extract_failed_tests(output):
    """Extrai a saída completa do pytest."""
    full_output = output.strip()
    failed_tests = [{"code": "pytest_output", "error": full_output}]
    return failed_tests

def execute_autonomous_tests():
    """Executa testes, identifica falhas, corrige e salva as atualizações."""
    print("\n🚀 Iniciando testes autônomos...")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n⚠️ GEMINI_API_KEY não está definida! Saindo do script.")
        return

    genai.configure(api_key=api_key)
    failed_tests = run_pytest()

    if failed_tests:
        for test in failed_tests:
            print(f"\n🔧 Corrigindo Teste com erro:\n{test['code']}\nErro: {test['error']}")
            fixed_code = fix_broken_test(test['code'], test['error'])
            print(f"Correção Sugerida:\n{fixed_code}")

            # Salvar teste corrigido
            file_path = "tests/test_login.py"
            save_fixed_test(file_path, fixed_code)
            print(f"\n💾 Correção salva em: {file_path}")

        print("\n📝 Gerando Novo Teste...")
        new_test = generate_test_code("Verificar se o login retorna erro email invalido.")
        print(f"Novo Caso de Teste:\n{new_test}")
    else:
        print("\n✅ Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    execute_autonomous_tests()
