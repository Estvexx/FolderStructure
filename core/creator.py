from pathlib import Path
import sys
from typing import Dict
from config import settings, templates
import re


class ProjectCreator:
    def __init__(self):
        self.base_dir = settings.BASE_DIR
        self.templates: Dict = templates.TEMPLATES

    def validate_project_name(self, name: str) -> bool:
        """Valida o nome do projeto"""
        if not name:
            print(
                f"{settings.Cores.VERMELHO}❌ Nome do projeto não pode ser vazio!{settings.Cores.RESET}"
            )
            return False

        if not re.match(r"^[a-zA-Z0-9_-]+$", name):
            print(
                f"{settings.Cores.VERMELHO}❌ Nome inválido! Use apenas letras, números, hífens ou underscores.{settings.Cores.RESET}"
            )
            return False

        return True

    def template_exists(self, template_name: str) -> bool:
        """Verifica se o template existe"""
        exists = template_name in self.templates
        if not exists:
            print(
                f"{settings.Cores.VERMELHO}❌ Template '{template_name}' não encontrado!{settings.Cores.RESET}"
            )
        return exists

    def create_structure(self, project_name: str, template_name: str = "vazio") -> bool:
        """Cria a estrutura do projeto com tratamento robusto de erros"""
        if not self.validate_project_name(project_name):
            return False

        if not self.template_exists(template_name):
            return False

        try:
            project_dir = self.base_dir / project_name
            project_dir.mkdir(exist_ok=False)

            print(
                f"{settings.Cores.VERDE}📂 Projeto '{project_name}' criado em {project_dir}{settings.Cores.RESET}"
            )

            for item in self.templates[template_name]["structure"]:
                item_path = project_dir / item
                if item.endswith("/"):
                    item_path.mkdir(parents=True, exist_ok=True)
                    print(
                        f"  {settings.Cores.VERDE}📁 Criada pasta: {item}{settings.Cores.RESET}"
                    )
                else:
                    item_path.touch()
                    print(
                        f"  {settings.Cores.VERDE}📄 Criado arquivo: {item}{settings.Cores.RESET}"
                    )

            return True

        except FileExistsError:
            print(
                f"{settings.Cores.AMARELO}⚠️ Erro: O projeto '{project_name}' já existe!{settings.Cores.RESET}"
            )
            return False
        except Exception as e:
            print(
                f"{settings.Cores.VERMELHO}❌ Erro crítico: {str(e)}{settings.Cores.RESET}"
            )
            return False


def show_help():
    """Mostra ajuda dos templates disponíveis com formatação colorida"""
    print(
        f"\n{settings.Cores.AZUL}📌 Uso: project_creator.py [NOME] [TEMPLATE]{settings.Cores.RESET}"
    )
    print(
        f"{settings.Cores.AZUL}📍 Local padrão: {settings.BASE_DIR}\n{settings.Cores.RESET}"
    )
    print(f"{settings.Cores.AZUL}📦 Templates disponíveis:{settings.Cores.RESET}")

    for name, template in templates.TEMPLATES.items():
        print(
            f"  {settings.Cores.VERDE}{name.ljust(8)}{settings.Cores.RESET} → {template['description']}"
        )
        if template["structure"]:
            print(f"      Estrutura: {', '.join(template['structure'])}")

    print(
        f"\n{settings.Cores.AZUL}Exemplo: python project_creator.py meu_site site{settings.Cores.RESET}"
    )
