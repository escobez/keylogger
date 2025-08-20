from ..utils.folder_create import N_ARQUIVE

def handle_normal_key(tecla):
    try:
        with open(N_ARQUIVE, "a", encoding="utf-8") as f:
            f.write(tecla)
        print(f"Normal: {tecla}")
    except Exception as e:
        print(f"[ERROR]: {e}")