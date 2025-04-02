#!/usr/bin/env python3
from core.creator import ProjectCreator, show_help
import sys


def main():
    creator = ProjectCreator()

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
