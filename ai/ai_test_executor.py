import os
import subprocess
import google.generativeai as genai
from ai_test_fixer import fix_broken_test
from ai_test_generator import generate_test_code
from datetime import datetime
import json

ROBOT_TEST_PATH = "tests/login.robot"
ROBOT_OUTPUT_XML = "logs/output.xml"


def run_robot():
    """Executa os testes com Robot Framework."""
    result = subprocess.run(
        [
            "robot",
            f"--output={ROBOT_OUTPUT_XML}",
            "--log", "logs/log.html",
            "--report", "logs/report.html",
            ROBOT_TEST_PATH
        ],
        capture_output=True,
        text=True,
        shell=True
    )

    output = result.stdout + result.stderr
    print("\n🛠 Testes executados! Saída:\n", output)

    if result.returncode != 0:
        print("\n❌ Testes falharam!")
        return extract_robot_failures()
    else:
        print("\n✅ Todos os testes passaram com sucesso!")
        return []

def extract_test_case_code(robot_file, test_name):
    """Extrai o código do caso de teste pelo nome a partir do arquivo .robot."""
    code_lines = []
    with open(robot_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    inside = False
    for line in lines:
        # Identifica início do bloco de teste
        if line.strip().lower().startswith(test_name.lower()):
            inside = True
            code_lines.append(line.rstrip())
            continue
        # Identifica início de um novo teste ou seção
        if inside and (line.strip().startswith("***") or (line and not line.startswith("    ") and not line.startswith("\t"))):
            break
        if inside:
            code_lines.append(line.rstrip())
    return "\n".join(code_lines)


def extract_robot_failures():
    from robot.api import ExecutionResult

    result = ExecutionResult(ROBOT_OUTPUT_XML)
    result.configure(stat_config={'suite_stat_level': 2})

    failed_tests = []
    # Tenta buscar tanto suites quanto testes diretamente na suite raiz
    suites_to_check = result.suite.suites or [result.suite]
    for suite in suites_to_check:
        for test in suite.tests:
            if test.status == 'FAIL':
                test_code = extract_test_case_code(ROBOT_TEST_PATH, test.name)
                failed_tests.append({
                    "code": test_code,
                    "error": test.message,
                    "name": test.name
                })
    return failed_tests


def execute_autonomous_robot_tests():
    print("\n🚀 Iniciando testes com Robot Framework...")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n⚠️ GEMINI_API_KEY não está definida! Saindo do script.")
        return

    genai.configure(api_key=api_key)
    failed_tests = run_robot()

    corrections = []
    for test in failed_tests:
        print(f"\n🔧 Corrigindo Teste com erro:\n{test['code']}\nErro: {test['error']}")
        fix = fix_broken_test(test['code'], test['error'])  # fix agora é um dicionário
        print(f"Correção Sugerida:\n{fix['code']}\nExplicação:\n{fix['explanation']}")
        corrections.append({
            "original_code": test['code'],
            "error": test['error'],
            "fixed_code": fix['code'],
            "explanation": fix['explanation']
    })

    print("\n📝 Gerando Novo Teste...")
    new_test = generate_test_code("Gerar todos os testes possiveis para login")
    print(f"Novo Caso de Teste:\n{new_test}")

    # Salva o log estruturado
    save_dashboard_log(failed_tests, corrections, new_test)


def save_dashboard_log(failed_tests, corrections, new_test):
    from datetime import datetime
    import json
    import os

    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(log_dir, f"dashboard_log_{timestamp}.json")

    log_data = {
        "failed_tests": failed_tests,
        "corrections": corrections,
        "new_tests": [new_test] if new_test else []
    }

    # Salva o log estruturado (para histórico)
    with open(log_file_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)

    # Salva as correções no fixer_log.json
    with open(os.path.join(log_dir, "fixer_log.json"), "w", encoding="utf-8") as f:
        json.dump([
            {
                "name": c.get("original_code", "Teste"),
                "code": c.get("fixed_code", ""),
                "explanation": f"Erro: {c.get('error', '')}"
            } for c in corrections
        ], f, indent=2, ensure_ascii=False)

    # Salva o novo teste sugerido no generator_log.json
    with open(os.path.join(log_dir, "generator_log.json"), "w", encoding="utf-8") as f:
        json.dump([
            {
                "title": "Novo Teste Sugerido",
                "code": new_test if isinstance(new_test, str) else new_test.get("test_code", ""),
                "description": ""
            }
        ] if new_test else [], f, indent=2, ensure_ascii=False)

    print(f"\n🧾 Logs salvos para o dashboard e para o Streamlit.")


if __name__ == "__main__":
    execute_autonomous_robot_tests()