@echo off
set PYTHONDONTWRITEBYTECODE=1

:: Executa o script principal com Robot Framework via Python
python ai\ai_test_executor.py

:: Executa o dashboard do Streamlit
echo.
echo Iniciando o dashboard do Streamlit...
streamlit run ai/ai_dashboard.py

:: Aviso final
echo.
echo Relatorio disponivel em: reports\log.html
pause