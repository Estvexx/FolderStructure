from config.settings import Cores

TEMPLATES = {
    "site": {
        "description": f"{Cores.AZUL}Estrutura básica para website{Cores.RESET}",
        "structure": ["index.html", "css/", "js/", "images/", "assets/"],
    },
    "python": {
        "description": f"{Cores.AZUL}Projeto Python padrão{Cores.RESET}",
        "structure": [
            "src/",
            "tests/",
            "requirements.txt",
            ".gitignore",
            "README.md",
            "setup.py",
        ],
    },
    "django": {
        "description": f"{Cores.AZUL}Projeto Django básico{Cores.RESET}",
        "structure": [
            "manage.py",
            "requirements.txt",
            ".env",
            "static/",
            "templates/",
            "apps/",
        ],
    },
    "vazio": {
        "description": f"{Cores.AZUL}Pasta vazia{Cores.RESET}",
        "structure": [],
    },
}
