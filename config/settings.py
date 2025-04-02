import sys
from .paths import setup_paths
from .colors import Cores

config = setup_paths()
USUARIO = config["USUARIO"]
BASE_DIR = config["BASE_DIR"]
LOG_FILE = config["LOG_FILE"]


# Verifica se o diretório base existe
if not BASE_DIR.exists():
    print(f"{Cores.AMARELO}⚠️ Diretório base não encontrado. Criando...{Cores.RESET}")
    try:
        BASE_DIR.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"{Cores.VERMELHO}❌ Erro ao criar diretório base: {e}{Cores.RESET}")
        sys.exit(1)


TREE_SYNTAX_HELP = """\
Sintaxe da árvore de diretórios:
- Prefixos: 
  '├── ' para itens intermédios
  '└── ' para o último item
  '│   ' para continuar ligação vertical
- Indentação com 4 espaços indica hierarquia
Exemplo:
MeuProjeto
├── src
│   ├── components
│   │   ├── Button.js
│   ├── index.js
├── assets
│   ├── logo.png
│   ├── styles.css
├── README.md
"""
