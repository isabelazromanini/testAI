import os
import streamlit as st
import json
from datetime import datetime
import pandas as pd

LOG_DIR = "logs/"

def read_log_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def list_log_files():
    files = [f for f in os.listdir(LOG_DIR) if os.path.isfile(os.path.join(LOG_DIR, f)) and f.endswith('.json')]
    return sorted(files, reverse=True)

def display_log_statistics(log_data):
    failed_tests = len(log_data.get("failed_tests", []))
    corrections = len(log_data.get("corrections", []))
    new_tests = len(log_data.get("new_tests", []))

    st.sidebar.header("📊 Estatísticas")
    st.sidebar.write(f"❌ Testes Falhos: {failed_tests}")
    st.sidebar.write(f"🔧 Correções Feitas: {corrections}")
    st.sidebar.write(f"📝 Novos Testes Gerados: {new_tests}")

def display_failed_tests(log_data):
    st.header("❌ Testes Falhos")
    failed_tests = log_data.get("failed_tests", [])

    for test in failed_tests:
        st.subheader("Código do Teste:")
        st.code(test['code'], language='python')
        st.subheader("Erro Encontrado:")
        st.text(test['error'])

def display_corrections(log_data):
    st.header("🔧 Correções Feitas")
    corrections = log_data.get("corrections", [])

    for correction in corrections:
        st.subheader("📂 Código Original:")
        st.code(correction['original_code'], language='python')
        st.subheader("⚠️ Erro:")
        st.text(correction['error'])
        st.subheader("✅ Código Corrigido:")
        st.code(correction['fixed_code'], language='python')

def display_new_tests(log_data):
    st.header("📝 Novos Testes Gerados")
    new_tests = log_data.get("new_tests", [])

    for test in new_tests:
        st.subheader("Descrição do Teste:")
        st.text(test['description'])
        st.subheader("Código Gerado:")
        st.code(test['test_code'], language='python')

def main():
    st.set_page_config(page_title="Dashboard de Testes Automatizados com IA", layout="wide")
    st.title("📈 Dashboard de Testes Automatizados com IA")

    log_files = list_log_files()

    if log_files:
        selected_log = st.selectbox("📂 Selecione um log para visualizar", log_files)
        log_data = read_log_file(os.path.join(LOG_DIR, selected_log))

        display_log_statistics(log_data)
        display_failed_tests(log_data)
        display_corrections(log_data)
        display_new_tests(log_data)
    else:
        st.write("🚫 Nenhum log encontrado.")

if __name__ == "__main__":
    main()
