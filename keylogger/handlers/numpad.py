from ..utils.folder_create import N_ARQUIVE

def handle_numpad_key(tecla_nome):
    try:    
        numero = tecla_nome[-1]
        with open(N_ARQUIVE, "a", encoding="utf-8") as f:
            f.write(numero)
        print(f"Normal (numpad): {numero}")
    except Exception as e:
        print(f"[ERROR]: {e}")