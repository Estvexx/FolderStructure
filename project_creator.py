#!/usr/bin/env python3
from core.creator import ProjectCreator, show_help
import sys


def main():
    creator = ProjectCreator()

    # Modo tree interativo
    if len(sys.argv) > 1 and sys.argv[1] in ("-t", "--tree"):
        if len(sys.argv) < 3:
            print("❌ Uso: criar_projeto --tree [NOME_DO_PROJETO]")
            sys.exit(1)

        project_name = sys.argv[2]
        print("\n🛠️  Modo Tree Interativo")
        print("Insira sua estrutura de pastas (Ctrl+Z + Enter para finalizar):\n")

        try:
            tree_lines = []
            while True:
                try:
                    line = input()
                    tree_lines.append(line)
                except EOFError:  # Ctrl+Z no Windows
                    break

            tree_str = "\n".join(tree_lines)

            if not tree_str.strip():
                print("❌ Nenhuma estrutura fornecida!")
                sys.exit(1)

            if not creator.create_from_tree(project_name, tree_str):
                sys.exit(1)

        except KeyboardInterrupt:
            print("\n❌ Operação cancelada pelo usuário")
            sys.exit(1)

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
