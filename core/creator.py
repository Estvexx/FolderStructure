from pathlib import Path
import sys
from typing import Dict
from config import settings
from config import templates


class ProjectCreator:
    def __init__(self):
        self.base_dir = settings.BASE_DIR
        self.templates: Dict = templates.TEMPLATES

    def create_structure(self, project_name: str, template_name: str = "vazio") -> bool:
        """Cria a estrutura do projeto"""
        try:
            project_dir = self.base_dir / project_name
            project_dir.mkdir(exist_ok=False)

            print(f"📂 Projeto '{project_name}' criado em {project_dir}")

            for item in self.templates[template_name]["structure"]:
                item_path = project_dir / item
                if item.endswith("/"):
                    item_path.mkdir()
                else:
                    item_path.touch()

            return True

        except FileExistsError:
            print(f"⚠️ Erro: O projeto '{project_name}' já existe!")
            return False
        except Exception as e:
            print(f"❌ Erro crítico: {str(e)}")
            return False


def show_help():
    """Mostra ajuda dos templates disponíveis"""
    print("\n📌 Uso: criar_projeto [NOME] [TEMPLATE]")
    print(f"📍 Local padrão: {settings.BASE_DIR}\n")
    print("📦 Templates disponíveis:")
    for name, template in templates.TEMPLATES.items():
        print(f"  {name.ljust(8)} → {template['description']}")
        print(f"      Estrutura: {', '.join(template['structure'])}")
    print("\nExemplo: criar_projeto meu_site site")
