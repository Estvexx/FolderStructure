def parse_tree(tree_str: str) -> list:
    """Versão mais robusta do parser"""
    lines = [line for line in tree_str.split("\n") if line.strip()]
    structure = []
    stack = []

    for line in lines:
        line = line.replace("├──", "").replace("└──", "").replace("│", "").strip()
        indent = len(line) - len(line.lstrip())
        name = line.strip()

        # Mantém apenas os níveis relevantes na stack
        stack = stack[: indent // 4]

        if name:
            # Constrói o path completo
            full_path = "/".join(stack + [name])

            # Garante que diretórios terminam com /
            if "/" in name or any(c in name for c in ["├", "└", "│"]):
                full_path = full_path.rstrip("/") + "/"

            structure.append(full_path)

            # Se for diretório, adiciona à stack
            if full_path.endswith("/"):
                stack.append(name)

    return structure
