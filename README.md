# 🌍 RPA - Sistema de Consulta de Países

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![API](https://img.shields.io/badge/API-REST%20Countries-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Um sistema de automação robótica de processos (RPA) para consultar, processar e armazenar informações de países através da API REST Countries.

[Funcionalidades](#-funcionalidades) • [Instalação](#-instalação) • [Uso](#-uso) • [Estrutura](#-estrutura-do-projeto) • [Tecnologias](#-tecnologias)

</div>

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Robotic Process Automation (RPA)**. O sistema automatiza o processo de:

1. 📝 Coletar nomes de países do usuário
2. 🌐 Buscar informações detalhadas na API REST Countries
3. 🔍 Filtrar e processar os dados recebidos
4. 💾 Armazenar no banco de dados SQLite
5. ✅ Validar duplicatas antes de inserir

---

## ✨ Funcionalidades

- ✅ **Consulta Automatizada**: Busca dados de 3 países por execução
- ✅ **API REST Countries**: Integração com API pública de dados geográficos
- ✅ **Banco de Dados Local**: Armazenamento em SQLite na pasta `data/`
- ✅ **Validação de Duplicatas**: Impede inserção de países já cadastrados
- ✅ **Filtro Inteligente**: Seleciona o país correto quando há múltiplos resultados
- ✅ **Feedback Visual**: Mensagens coloridas informando status das operações

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a passo

1. **Clone o repositório**
```bash
git clone https://github.com/Impacta-Projetos/Ap2-RPA.git
cd Ap2-RPA
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute o programa**
```bash
python main.py
```

---

## 💻 Uso

### Execução Principal

```bash
python main.py
```

**Exemplo de interação:**

```
Digite o nome do 1º país: brasil
Digite o nome do 2º país: china
Digite o nome do 3º país: japão

✓ País 'brasil' inserido com sucesso!
✓ País 'china' inserido com sucesso!
✓ País 'japão' inserido com sucesso!
```

---

## 📁 Estrutura do Projeto

```
AP2-RPA/
│
├── 📄 main.py                 # Ponto de entrada do programa
├── 📄 requirements.txt        # Dependências do projeto
│
├── 📂 api/
│   └── 📄 api.py             # Consumo da API REST Countries
│
├── 📂 core/
│   ├── 📄 input.py           # Coleta de dados do usuário
│   ├── 📄 filter.py          # Filtragem e processamento de dados
│   └── 📄 insert.py          # Inserção no banco de dados
│
├── 📂 models/
│   ├── 📄 __init__.py        # Conexão com banco de dados
│   └── 📄 paises.py          # Modelo da tabela de países
│
├── 📂 data/
│   └── 💾 paises.db          # Banco de dados SQLite (gerado automaticamente)
│
└── 📂 docs/
    └── 📄 RELATORIO.pdf       # Relatório técnico completo
```

---

## 🗄️ Estrutura do Banco de Dados

### Tabela: `paises`

| Campo              | Tipo    | Descrição                          |
|--------------------|---------|------------------------------------|
| `id`               | INTEGER | Chave primária (auto incremento)  |
| `nome_comum`       | TEXT    | Nome comum do país                 |
| `nome_oficial`     | TEXT    | Nome oficial completo              |
| `capital`          | TEXT    | Capital do país                    |
| `continente`       | TEXT    | Continente onde se localiza        |
| `regiao`           | TEXT    | Região geográfica                  |
| `subregiao`        | TEXT    | Sub-região específica              |
| `populacao`        | INTEGER | População total                    |
| `area`             | REAL    | Área territorial (km²)             |
| `moeda_nome`       | TEXT    | Nome da moeda oficial              |
| `moeda_simbolo`    | TEXT    | Símbolo da moeda                   |
| `idioma_principal` | TEXT    | Idioma principal                   |
| `fuso_horario`     | TEXT    | Fuso horário principal             |
| `bandeira_url`     | TEXT    | URL da imagem da bandeira          |

---

## 🛠️ Tecnologias

### Core

- **[Python 3.13](https://www.python.org/)** - Linguagem principal
- **[SQLite3](https://www.sqlite.org/)** - Banco de dados relacional
- **[REST Countries API](https://restcountries.com/)** - API de dados geográficos

### Bibliotecas

- **[Requests](https://requests.readthedocs.io/)** - Requisições HTTP
  
---

## 🎯 Funcionalidades Técnicas

### Filtro Inteligente de Países

O sistema implementa um algoritmo que:

1. Busca correspondência exata com o nome digitado
2. Prioriza países cujo nome começa com o termo buscado
3. Evita resultados incorretos (ex: Taiwan ao buscar "china")

```python
# Exemplo: Busca por "china"
# ✅ Retorna: People's Republic of China
# ❌ Não retorna: Taiwan (Republic of China)
```

### Validação de Duplicatas

Antes de inserir um país, o sistema verifica se já existe:

```python
cursor.execute('SELECT id FROM paises WHERE nome_comum = ?', (nome_pais,))
if cursor.fetchone():
    print("⚠ País já existe no banco de dados!")
```

### Tratamento de Erros

- ✅ API indisponível ou país não encontrado
- ✅ Dados incompletos na resposta da API
- ✅ Duplicatas no banco de dados
- ✅ Criação automática do diretório `data/`

---

## 📊 Dados Coletados

Para cada país, são extraídos **13 campos** da API:

| Categoria         | Campos                                          |
|-------------------|-------------------------------------------------|
| **Identificação** | Nome comum, Nome oficial                        |
| **Localização**   | Capital, Continente, Região, Sub-região         |
| **Demografia**    | População                                       |
| **Geografia**     | Área territorial                                |
| **Economia**      | Moeda (nome e símbolo)                          |
| **Cultura**       | Idioma principal                                |
| **Outros**        | Fuso horário, URL da bandeira                   |

---

## 📝 Exemplos de Uso

### Caso 1: Primeira Execução

```bash
$ python main.py
Digite o nome do 1º país: brasil
Digite o nome do 2º país: frança
Digite o nome do 3º país: canadá

✓ País 'brasil' inserido com sucesso!
✓ País 'frança' inserido com sucesso!
✓ País 'canadá' inserido com sucesso!
```

### Caso 2: Tentativa de Duplicata

```bash
$ python main.py
Digite o nome do 1º país: brasil
Digite o nome do 2º país: alemanha
Digite o nome do 3º país: méxico

⚠ País 'brasil' já existe no banco de dados!
✓ País 'alemanha' inserido com sucesso!
✓ País 'méxico' inserido com sucesso!
```

### Caso 3: País Não Encontrado

```bash
$ python main.py
Digite o nome do 1º país: xyzabc
Digite o nome do 2º país: portugal
Digite o nome do 3º país: espanha

✗ Não foi possível obter dados para 'xyzabc'
✓ País 'portugal' inserido com sucesso!
✓ País 'espanha' inserido com sucesso!
```

---

## 🔧 Configuração

### Modificar Quantidade de Países

Edite `core/input.py`:

```python
def obter_paises():
    paises = []
    cont = 1
    while cont <= 5:  # Altere de 3 para 5
        pais = input(f'Digite o nome do {cont}º país: ').lower()
        paises.append(pais)
        cont += 1
    return paises
```

### Alterar Localização do Banco

Edite `models/__init__.py`:

```python
db = sqlite3.connect('meu_banco/paises.db')  # Novo caminho
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autores

**Felipe Viana** e **Ryan Rodrigues**

---

<div align="center">

⭐ Se este projeto foi útil, considere dar uma estrela!

</div>
