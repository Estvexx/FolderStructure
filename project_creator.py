#!/usr/bin/env python3
from core.creator import ProjectCreator, show_help
import sys


def main():
    creator = ProjectCreator()

    # Modo tree (nova funcionalidade)
    if len(sys.argv) > 1 and sys.argv[1] in ("-t", "--tree"):
        if len(sys.argv) < 3:
            print("❌ Uso: criar_projeto --tree [NOME] [ARQUIVO_ESTRUTURA]")
            print("   Ou: criar_projeto --tree [NOME] < [ARQUIVO_ESTRUTURA]")
            sys.exit(1)

        project_name = sys.argv[2]

        # Tenta ler do arquivo (PowerShell)
        if len(sys.argv) > 3:
            try:
                with open(sys.argv[3], "r", encoding="utf-8") as f:
                    tree_str = f.read()
            except FileNotFoundError:
                print(f"❌ Arquivo '{sys.argv[3]}' não encontrado")
                sys.exit(1)
        # Tenta ler do stdin (Bash)
        else:
            try:
                tree_str = sys.stdin.read()
            except Exception as e:
                print(f"❌ Erro ao ler entrada: {e}")
                sys.exit(1)

        if not creator.create_from_tree(project_name, tree_str):
            sys.exit(1)
        return

    # Modo interativo
    if len(sys.argv) == 1 or sys.argv[1] in ("-i", "--interactive"):
        creator.show_interactive_menu()
        sys.exit(0)

    # Ajuda
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        show_help()
        sys.exit(0)

    # Modo CLI tradicional
    project_name = sys.argv[1]
    template = sys.argv[2] if len(sys.argv) > 2 else "vazio"

    if not creator.create_structure(project_name, template):
        sys.exit(1)


if __name__ == "__main__":
    main()
