from pathlib import Path


def validate_and_create(project_name: str, tree_str: str, base_dir: Path):
    """Valida e cria a estrutura"""
    from .tree_parser import parse_tree
    from .creator import ProjectCreator

    structure = parse_tree(tree_str)
    if not structure:
        print("❌ Estrutura vazia ou inválida!")
        return False

    print("\n📋 Estrutura a ser criada:")
    for item in structure:
        print(f"  → {item}")

    confirm = input("\nConfirmar criação? (s/n): ").lower()
    if confirm != "s":
        print("Operação cancelada")
        return False

    creator = ProjectCreator(base_dir)
    return creator._create_from_custom_tree(
        project_name, {"structure": structure, "description": "Tree personalizada"}
    )
