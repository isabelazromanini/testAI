import os
import json
import streamlit as st

LOG_DIR = "logs/"

def list_dashboard_logs():
    files = [f for f in os.listdir(LOG_DIR) if f.startswith("dashboard_log") and f.endswith(".json")]
    return sorted(files, reverse=True)

def parse_dashboard_log(json_path):
    with open(os.path.join(LOG_DIR, json_path), "r", encoding="utf-8") as f:
        return json.load(f)

def display_log_statistics(log_data):
    failed_tests = log_data.get("failed_tests", [])
    st.sidebar.header("\U0001F4CA Estatísticas")
    st.sidebar.write(f"❌ Testes Falhos: {len(failed_tests)}")

def display_failed_tests(log_data):
    failed_tests = log_data.get("failed_tests", [])
    st.header("❌ Testes Falhos")
    if failed_tests:
        for test in failed_tests:
            st.subheader(test.get("name", "Teste sem nome"))
            st.text(test.get("error", ""))
    else:
        st.info("Nenhum teste falho encontrado neste log.")

def display_fixer_suggestions(log_data):
    corrections = log_data.get("corrections", [])
    st.header("🛠️ Sugestões de Correção (Gemini)")
    if corrections:
        for fix in corrections:
            st.subheader(fix.get("name", "Teste"))
            st.code(fix.get("fixed_code", ""))
            st.text(fix.get("explanation", ""))
    else:
        st.info("Nenhuma sugestão de correção encontrada.")

def display_generated_tests(log_data):
    generated = log_data.get("new_tests", [])
    st.header("🧪 Novos Testes Sugeridos (Gemini)")
    if generated:
        for test in generated:
            st.code(test if isinstance(test, str) else test.get("test_code", ""))
    else:
        st.info("Nenhum teste sugerido encontrado.")

def main():
    st.set_page_config(page_title="Dashboard de Testes Robot Framework", layout="wide")
    st.title("\U0001F4C8 Dashboard de Testes Automatizados com Robot Framework")

    log_files = list_dashboard_logs()

    if log_files:
        selected_log = st.selectbox("\U0001F4C2 Selecione um log para visualizar", log_files)
        log_data = parse_dashboard_log(selected_log)

        display_log_statistics(log_data)
        display_failed_tests(log_data)
        display_fixer_suggestions(log_data)
        display_generated_tests(log_data)
    else:
        st.write("🚫 Nenhum log de dashboard encontrado em /logs")

if __name__ == "__main__":
    main()
