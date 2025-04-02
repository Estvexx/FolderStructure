#!/usr/bin/env python3
from core.creator import ProjectCreator, show_help
import sys


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        show_help()
        sys.exit()

    creator = ProjectCreator()
    project_name = sys.argv[1]
    template = sys.argv[2] if len(sys.argv) > 2 else "vazio"

    creator.create_structure(project_name, template)


if __name__ == "__main__":
    main()
