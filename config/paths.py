from pathlib import Path
import getpass
import os


def get_system_user():
    """Detecta o usuário do sistema de forma cross-platform"""
    try:
        return getpass.getuser()  # Windows/Linux/Mac
    except:
        return os.environ.get("USERNAME", "default_user")


def setup_paths():
    """Configura os caminhos base do projeto"""
    user = get_system_user()
    base_dir = Path.home() / "scripts" / "projetos"
    base_dir.mkdir(parents=True, exist_ok=True)

    return {
        "USUARIO": user,
        "BASE_DIR": base_dir,
        "LOG_FILE": base_dir / "criar_projeto.log",
    }
