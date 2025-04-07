@echo off
set PYTHONDONTWRITEBYTECODE=1

:: Remover caches apenas se existirem
if exist __pycache__ rmdir /s /q __pycache__
if exist .pytest_cache rmdir /s /q .pytest_cache

:: Executa o ai_test_executor.py com limpeza de cache do pytest
python ai\ai_test_executor.py --cache-clear

:: Gerar relatório do Allure
if exist reports\allure-report rmdir /s /q reports\allure-report
allure generate reports/ -o reports/allure-report --clean
allure open reports/allure-report

:: Remove novamente os caches após a execução
if exist __pycache__ rmdir /s /q __pycache__
if exist .pytest_cache rmdir /s /q .pytest_cache
pause
