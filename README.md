# 📂 Project Creator CLI

Ferramenta para criação automatizada de estruturas de projetos com templates pré-definidos ou customizados.

## 📥 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Estvexx/FolderStructure.git
   cd AUTOMATEFOLDER
   ```

## 🚀 Como Usar

### 🔧 Modo Interativo

```bash
python project_Creator.py -i
# ou
python project_Creator.py --interactive
```

**Exemplo de fluxo:**

1. Insira o nome do projeto
2. Selecione um template disponível
3. Confirme a criação

### ⚡ Modo CLI Rápido

```bash
python project_Creator.py [NOME_DO_PROJETO] [TEMPLATE]
```

**Exemplos:**

```bash
# Criar projeto vazio
python project_Creator.py meu_projeto

# Criar projeto web
python project_Creator.py meu_site site

# Criar projeto Python
python project_Creator.py meu_script python
```

### 🌳 Modo Tree (Estrutura Customizada)

```bash
python project_Creator.py --tree [NOME] [ARQUIVO_ESTRUTURA]
```

**Exemplo:**
Crie um arquivo `estrutura.txt`:

```
MeuProjeto
├── src
│   ├── main.py
│   └── utils.py
└── README.md
```

Execute:

```bash
python project_Creator.py --tree meu_projeto estrutura.txt
```

## 📋 Templates Disponíveis

| Comando | Descrição          | Estrutura                        |
| ------- | ------------------ | -------------------------------- |
| site    | Projeto Web básico | `index.html, css/, js/, images/` |
| python  | Projeto Python     | `src/, tests/, requirements.txt` |
| django  | Projeto Django     | `manage.py, static/, templates/` |
| vazio   | Pasta vazia        | `(nenhum)`                       |

## 🛠 Estrutura do Projeto

```
project_creator/
├── config/
│   ├── settings.py      # Configurações
│   └── templates.py     # Templates pré-definidos
├── core/
│   ├── creator.py       # Lógica principal
│   └── tree_parser.py   # Processador de estruturas
└── project_Creator.py   # Ponto de entrada
```

## 📌 Dicas

- Para ver todos os templates disponíveis:
  ```bash
  python project_Creator.py --help
  ```
- Use `-h` para ajuda rápida:
  ```bash
  python project_Creator.py -h
  ```
- No Linux/Mac, pode usar redirecionamento:
  ```bash
  python project_Creator.py --tree meu_projeto < estrutura.txt
  ```

## 📝 Licença

MIT License - Consulte o arquivo `LICENSE` para detalhes.
