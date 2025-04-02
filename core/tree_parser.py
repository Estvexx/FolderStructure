from pathlib import Path
import re


class TreeParser:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    def parse_tree(self, tree_str: str) -> dict:
        """Converte string de árvore em estrutura de dicionário"""
        lines = [line.rstrip() for line in tree_str.split("\n") if line.strip()]
        if not lines:
            return {}

        root = {}
        stack = [(-1, root)]

        for line in lines:
            clean_line = re.sub(r"^([│ ]*(├|└)── )", "", line)
            indent = len(line) - len(clean_line.lstrip())
            name = clean_line.strip()

            if not name:
                continue

            is_folder = not "." in name.split("/")[-1]
            current_level = indent // 4

            while stack and stack[-1][0] >= current_level:
                stack.pop()

            if not stack:
                continue

            _, parent_dict = stack[-1]

            if is_folder:
                new_dict = {}
                key = f"{name}/"
                parent_dict[key] = new_dict
                stack.append((current_level, new_dict))
            else:
                parent_dict[name] = None

        return root

    def create_from_tree(self, tree_str: str, root_path: Path) -> bool:
        """Cria estrutura a partir da string tree"""
        try:
            structure = self.parse_tree(tree_str)
            if not structure:
                print("❌ Estrutura inválida ou vazia")
                return False

            return self._create_structure(structure, root_path)

        except Exception as e:
            print(f"❌ Erro ao processar árvore: {str(e)}")
            return False

    def _create_structure(self, structure: dict, current_path: Path) -> bool:
        """Cria estrutura recursivamente"""
        try:
            for name, content in structure.items():
                item_path = current_path / name

                if name.endswith("/"):
                    item_path.mkdir(exist_ok=True)
                    print(f"📁 Criada pasta: {item_path.relative_to(self.base_dir)}")

                    if content:
                        self._create_structure(content, item_path)
                else:
                    item_path.touch()
                    print(f"📄 Criado arquivo: {item_path.relative_to(self.base_dir)}")

            return True

        except Exception as e:
            print(f"❌ Falha em {current_path}: {str(e)}")
            return False
