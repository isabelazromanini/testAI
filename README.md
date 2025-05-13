
# 🤖 Testes Automatizados com Inteligência Artificial

Este projeto demonstra como automatizar a geração, execução e correção de testes de software utilizando Robot Framework, SeleniumLibrary e a API Gemini da Google, com visualização de resultados por meio de um dashboard em Streamlit.

## 📂 Estrutura do Projeto

```
.
├── ai_dashboard.py             # Dashboard interativo com Streamlit
├── ai_test_executor.py        # Executor dos testes + integração com IA
├── ai_test_fixer.py           # Corrige testes quebrados usando Gemini
├── ai_test_generator.py       # Gera novos testes com base em prompts
├── requirements.txt           # Dependências do projeto
├── runTest.bat                # Script Windows para execução automatizada
├── tests/
│   └── login.robot            # Arquivo de testes em Robot Framework
├── keywords/
│   └── login_kws.robot        # Palavras-chave utilizadas nos testes
└── logs/                      # Armazena logs, correções e sugestões
```

## 🚀 Funcionalidades

- **Execução automatizada de testes Robot Framework**
- **Detecção de testes que falharam**
- **Correção automática dos testes com falha via Gemini**
- **Geração de novos testes com base em descrição**
- **Visualização dos resultados e sugestões via dashboard em Streamlit**

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/nome-do-projeto.git
   cd nome-do-projeto
   ```

2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate.bat    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔐 Configuração da API Gemini

Antes de rodar os scripts que usam IA, defina sua chave da API Gemini:

**Linux/macOS**
```bash
export GEMINI_API_KEY="sua-chave-api"
```

**Windows (CMD)**
```cmd
set GEMINI_API_KEY=sua-chave-api
```

---

## 🧪 Executando os Testes

Para executar os testes com análise automática:

```bash
python ai_test_executor.py
```

Isso irá:
- Rodar os testes do Robot Framework
- Identificar falhas
- Corrigir os testes com IA
- Gerar um novo teste automaticamente
- Salvar os logs e sugestões em `/logs`

---

## 📊 Visualizando o Dashboard

Após a execução dos testes, visualize os resultados com:

```bash
streamlit run ai_dashboard.py
```

Acesse o dashboard no navegador em: [http://localhost:8501](http://localhost:8501)

---

## 📁 Pasta `/logs`

Após cada execução, os seguintes arquivos serão criados:

- `dashboard_log_*.json`: resumo completo de falhas, correções e novos testes
- `fixer_log.json`: apenas correções feitas pela IA
- `generator_log.json`: novos testes sugeridos

---

## 🖥️ Rodando no Windows com Script `.bat`

Use o arquivo `runTest.bat` para rodar o processo completo com duplo clique (certifique-se que a variável de ambiente esteja configurada ou adaptada no próprio `.bat`).

---

## ✅ Requisitos

- Python 3.8+
- Navegador Chrome instalado (para Selenium)
- Internet ativa (para uso da API Gemini)

---

## 🧠 Sobre o Projeto

Este projeto foi criado como parte de um TCC no MBA em Data Science & Analytics da USP ESALQ, com foco em como a inteligência artificial pode revolucionar o ciclo de vida da garantia de qualidade em software.
