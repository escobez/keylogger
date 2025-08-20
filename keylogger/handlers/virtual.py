from ..utils.folder_create import N_ARQUIVE
from ..handlers.special import handle_special_key

def handle_virtual_code(tecla_nome):
    try:
        codigo = int(tecla_nome[1:-1])
        # 48-57: números do teclado principal, 96-105: números do numpad
        if 48 <= codigo <= 57:
            numero = chr(codigo)
            with open(N_ARQUIVE, "a", encoding="utf-8") as f:
                f.write(numero)
            print(f"Normal (virtual): {numero}")
        elif 96 <= codigo <= 105:
            numero = str(codigo - 96)
            with open(N_ARQUIVE, "a", encoding="utf-8") as f:
                f.write(numero)
            print(f"Normal (numpad virtual): {numero}")
        else:
            handle_special_key(tecla_nome)
    except Exception as e:
        print(f"[ERROR]: {e}")