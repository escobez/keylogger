from ..utils.folder_create import S_ARQUIVE

def handle_special_key(tecla_nome):
    try:
        with open(S_ARQUIVE, "a", encoding="utf-8") as f:
            f.write(f"[{tecla_nome.upper()}]\n")
        print(f"Especial: [{tecla_nome.upper()}]")
    except Exception as e:
        print(f"[ERROR]: {e}")