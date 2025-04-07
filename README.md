# 📌 ProjetoTCC - Garantia de Qualidade Automatizada com Inteligência Artificial

Este projeto é uma implementação de testes automatizados funcionais utilizando Python, Selenium, Pytest, Pytest-BDD e Allure para geração de relatórios. A integração de IA é feita através do modelo Gemini da Google para corrigir erros e gerar novos cenários de teste automaticamente.

---

## 📂 Estrutura do Projeto

```
PROJETOTCC/
├── ai/                         # Integrações de IA (Gemini) para geração e correção de testes
│   ├── ai_dashboard.py         # Dashboard para visualização dos resultados da IA
│   ├── ai_test_executor.py     # Executor principal que roda os testes e utiliza a IA
│   ├── ai_test_fixer.py        # Corrige erros nos testes usando o Gemini
│   ├── ai_test_generator.py    # Gera novos cenários de teste utilizando IA
├── features/                   # Arquivos Gherkin (.feature)
│   ├── test_login.feature      # Cenários de teste de login
├── logs/                       # Logs detalhados das interações com a IA
├── pages/                      # Page Objects contendo métodos para interagir com elementos da interface
│   ├── login_page.py           # Página de login com métodos de interação
├── reports/                    # Relatórios gerados pelo Allure
├── tests/                      # Arquivos de testes que implementam os steps definidos nos arquivos .feature
│   ├── test_login.py           # Implementação dos testes de login
├── requirements.txt            # Dependências do projeto
├── runTest.bat                 # Script para execução dos testes
├── README.md                   # Documentação do projeto
```

---

## 🛠️ Configuração do Ambiente

### 1️⃣ Instale o Python 3.11
Certifique-se de ter o **Python 3.11** instalado. Para verificar, rode:
```sh
python --version
```
Se necessário, baixe a versão mais recente de [python.org](https://www.python.org/downloads/).

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado)
```sh
python -m venv venv
```
Ative o ambiente:
- **Windows**: `venv\Scripts\activate`
- **Linux/macOS**: `source venv/bin/activate`

### 3️⃣ Instale as dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Instale o Allure CLI (Para relatórios)
No **Windows**, instale via Chocolatey:
```sh
choco install allure
```
Ou baixe manualmente de [Allure Releases](https://github.com/allure-framework/allure2/releases).

Verifique a instalação com:
```sh
allure --version
```

### 5️⃣ Configure a chave da API do Gemini
Defina a variável de ambiente `GEMINI_API_KEY` com a chave da API fornecida pela Google:
```sh
set GEMINI_API_KEY=SUACHAVEAQUI
```

---

## 🚀 Executando os Testes

### 1️⃣ Rodando o script de testes (`runTest.bat`)
Execute no terminal:
```sh
.\runTest.bat
```
Isso:
- Remove caches (`__pycache__` e `.pytest_cache`)
- Executa o arquivo `ai_test_executor.py`
- Remove caches novamente após os testes
- Pausa a execução para visualizar os resultados

### 2️⃣ Rodando os testes manualmente
```sh
python ai_test_executor.py
```

### 3️⃣ Gerando Relatórios Allure
Os relatórios são gerados automaticamente após a execução dos testes.
Para visualizar:
```sh
allure serve reports/
```

### 4️⃣ Visualizando o Dashboard
Rode o dashboard do projeto para visualizar logs e métricas detalhadas:
```sh
streamlit run ai/ai_dashboard.py
```

---

## 🔥 Solução de Problemas

- Se os testes não encontrarem o módulo `pages`, adicione esta linha no topo de `test_login.py`:
```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

- Se aparecer `StepDefinitionNotFoundError`, certifique-se de que o arquivo `.feature` contém os mesmos textos dos métodos de step.

- Se o comando `setx GEMINI_API_KEY` falhar com `Access to the registry path is denied`, rode o terminal como **Administrador**.

---

## 📌 Notas Finais
Este projeto é projetado para utilizar IA na geração e correção de testes automatizados, otimizando o ciclo de vida de desenvolvimento de software. Certifique-se de configurar a chave da API do Gemini antes de executar os testes.

✅ Bom trabalho e boa sorte! 🚀
