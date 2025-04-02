from pathlib import Path
from typing import Final
import sys

# Configurações do Usuário
USUARIO: Final[str] = "franc"
BASE_DIR: Final[Path] = Path(f"C:/Users/{USUARIO}/scripts/projetos")
LOG_FILE: Final[Path] = BASE_DIR / "criar_projeto.log"


# Cores para terminal
class Cores:
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[91m"
    AZUL = "\033[94m"
    RESET = "\033[0m"


# Verifica se o diretório base existe
if not BASE_DIR.exists():
    print(f"{Cores.AMARELO}⚠️ Diretório base não encontrado. Criando...{Cores.RESET}")
    try:
        BASE_DIR.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"{Cores.VERMELHO}❌ Erro ao criar diretório base: {e}{Cores.RESET}")
        sys.exit(1)
