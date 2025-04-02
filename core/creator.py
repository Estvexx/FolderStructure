from typing import Dict
from config import settings, templates
from core.tree_parser import TreeParser
import re
import sys


class ProjectCreator:
    def __init__(self):
        self.base_dir = settings.BASE_DIR
        self.templates: Dict = templates.TEMPLATES

    def create_from_tree(self, project_name: str, tree_str: str) -> bool:
        """Cria projeto a partir de string de árvore"""
        if not self.validate_project_name(project_name):
            return False

        project_dir = self.base_dir / project_name
        try:
            project_dir.mkdir(exist_ok=False)
            print(f"📂 Projeto '{project_name}' criado em {project_dir}")

            # Cria instância do parser de árvore
            tree_parser = TreeParser(self.base_dir)

            # Executa a criação da estrutura
            result = tree_parser.create_from_tree(tree_str, project_dir)

            # Retorna o resultado diretamente sem verificar templates
            return result

        except FileExistsError:
            print(f"⚠️ Erro: O projeto '{project_name}' já existe!")
            return False
        except Exception as e:
            print(f"❌ Erro crítico: {str(e)}")
            # Limpeza em caso de erro
            try:
                import shutil

                shutil.rmtree(project_dir)
            except:
                pass
            return False

    def validate_project_name(self, name: str) -> bool:
        """Valida o nome do projeto com regex melhorado"""
        if not name:
            print(
                f"{settings.Cores.VERMELHO}❌ Nome do projeto não pode ser vazio!{settings.Cores.RESET}"
            )
            return False

        pattern = r"^[a-zA-Z0-9_-]+$"
        if not re.match(pattern, name):
            print(
                f"{settings.Cores.VERMELHO}❌ Nome inválido! Use apenas:"
                f"\n- Letras (a-z, A-Z)"
                f"\n- Números (0-9)"
                f"\n- Hífens (-) ou underscores (_){settings.Cores.RESET}"
            )
            return False

        if len(name) > 50:
            print(
                f"{settings.Cores.VERMELHO}❌ Nome muito longo (máx. 50 caracteres){settings.Cores.RESET}"
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

    def show_interactive_menu(self):
        """Menu interativo completo com tratamento de erros"""
        print(
            f"\n{settings.Cores.AZUL}🛠️  Criador de Projetos Interativo{settings.Cores.RESET}"
        )
        print(
            f"{settings.Cores.VERDE}================================{settings.Cores.RESET}\n"
        )

        print(f"📁 Local padrão: {self.base_dir}\n")

        # Obter nome do projeto com validação
        project_name = ""
        while True:
            project_name = input(
                f"{settings.Cores.AZUL}? Nome do projeto:{settings.Cores.RESET} "
            ).strip()
            try:
                if self.validate_project_name(project_name):
                    break
            except Exception as e:
                print(
                    f"{settings.Cores.VERMELHO}❌ Erro na validação: {e}{settings.Cores.RESET}"
                )
                sys.exit(1)

        # Mostrar templates
        print(f"\n{settings.Cores.AZUL}📦 Templates disponíveis:{settings.Cores.RESET}")
        templates_list = list(self.templates.items())

        for i, (name, template) in enumerate(templates_list, 1):
            print(f"{i}. {name.ljust(8)} → {template['description']}")
            if template["structure"]:
                print(f"   Estrutura: {', '.join(template['structure'])}")

        # Selecionar template
        template_name = ""
        while True:
            choice = input(
                f"\n{settings.Cores.AZUL}? Escolha o template (1-{len(templates_list)}):{settings.Cores.RESET} "
            ).strip()
            try:
                if choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(templates_list):
                        template_name = templates_list[index][0]
                        break
                print(
                    f"{settings.Cores.VERMELHO}⚠️ Escolha inválida! Digite um número entre 1 e {len(templates_list)}{settings.Cores.RESET}"
                )
            except Exception as e:
                print(
                    f"{settings.Cores.VERMELHO}❌ Erro inesperado: {e}{settings.Cores.RESET}"
                )

        # Confirmação final
        confirm = (
            input(
                f"\n{settings.Cores.AMARELO}? Confirmar criação do projeto '{project_name}' com template '{template_name}'? [s/N]:{settings.Cores.RESET} "
            )
            .strip()
            .lower()
        )

        if confirm == "s":
            success = self.create_structure(project_name, template_name)
            if success:
                print(
                    f"\n{settings.Cores.VERDE}✅ Projeto criado com sucesso em: {self.base_dir / project_name}{settings.Cores.RESET}"
                )
                return True
            return False

        print(
            f"\n{settings.Cores.AMARELO}✖ Operação cancelada pelo usuário{settings.Cores.RESET}"
        )
        return False

    # ... (mantenha os métodos existentes create_structure e outros)

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
    """Mostra ajuda completa com todos os modos de operação"""
    # Cabeçalho
    print(f"\n{settings.Cores.AZUL}🛠️  Project Creator - Ajuda{settings.Cores.RESET}")
    print(f"{settings.Cores.VERDE}=========================={settings.Cores.RESET}")

    # Modos de uso
    print(f"\n{settings.Cores.AZUL}📌 Modos de Uso Disponíveis:{settings.Cores.RESET}")

    # 1. Modo Interativo
    print(f"\n{settings.Cores.VERDE}1. Modo Interativo:{settings.Cores.RESET}")
    print(f"   {settings.Cores.AZUL}python project_creator.py -i{settings.Cores.RESET}")
    print(
        f"   {settings.Cores.AZUL}python project_creator.py --interactive{settings.Cores.RESET}"
    )
    print("   \n   Um assistente passo-a-passo para criação de projetos")

    # 2. Modo CLI Tradicional
    print(f"\n{settings.Cores.VERDE}2. Modo CLI Rápido:{settings.Cores.RESET}")
    print(
        f"   {settings.Cores.AZUL}python project_creator.py [NOME] [TEMPLATE]{settings.Cores.RESET}"
    )
    print(f"   \n   Exemplos:")
    print(
        f"   {settings.Cores.AZUL}python project_creator.py meu_projeto python{settings.Cores.RESET}"
    )
    print(
        f"   {settings.Cores.AZUL}python project_creator.py meu_site site{settings.Cores.RESET}"
    )

    # 3. Modo Tree
    print(f"\n{settings.Cores.VERDE}3. Modo Tree:{settings.Cores.RESET}")
    print(
        f"   {settings.Cores.AZUL}python project_creator.py -t [NOME] [ARQUIVO]{settings.Cores.RESET}"
    )
    print(
        f"   {settings.Cores.AZUL}python project_creator.py --tree [NOME] < estrutura.txt{settings.Cores.RESET}"
    )
    print(
        f"   {settings.Cores.AZUL}python project_creator.py --tree [NOME] (modo interativo){settings.Cores.RESET}"
    )
    print("   \n   Cria estrutura customizada a partir de um arquivo ou entrada direta")

    # Templates disponíveis
    print(f"\n{settings.Cores.AZUL}📦 Templates Pré-definidos:{settings.Cores.RESET}")
    for name, template in templates.TEMPLATES.items():
        print(
            f"  {settings.Cores.VERDE}{name.ljust(8)}{settings.Cores.RESET} → {template['description']}"
        )
        if template["structure"]:
            print(f"      Estrutura: {', '.join(template['structure'])}")

    # Configurações
    print(f"\n{settings.Cores.AZUL}⚙️  Configurações Atuais:{settings.Cores.RESET}")
    print(f"   Diretório Base: {settings.BASE_DIR}")
    print(f"   Arquivo de Log: {settings.LOG_FILE}")

    # Exemplo de tree
    print(f"\n{settings.Cores.AZUL}🌳 Exemplo de Estrutura Tree:{settings.Cores.RESET}")
    print("MeuProjeto")
    print("├── src")
    print("│   ├── main.py")
    print("│   └── utils.py")
    print("└── README.md")

    # Rodapé
    print(
        f"\n{settings.Cores.VERDE}✅ Dica: Use --help a qualquer momento para ver esta mensagem{settings.Cores.RESET}"
    )
