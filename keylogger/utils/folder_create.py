import os

# Caminhos dos arquivos
FOLDER = "logs"
N_ARQUIVE = os.path.join(FOLDER, "keylogger.txt")
S_ARQUIVE = os.path.join(FOLDER, "teclas_especiais.txt")

# Cria a pasta se não existir
os.makedirs(FOLDER, exist_ok=True)

# Teclas especiais a ignorar
IGNORE = {"shift", "ctrl", "alt", "caps_lock", "num_lock", "scroll_lock"}

# Variável global para o listener
LISTENER = None