# keylogger - an unoriginal name
This program is a simple keylogger written in Python. It listens to keyboard input and records all pressed keys into separate log files:

* Normal keys: letters, numbers, and standard symbols
* Numpad keys: numbers from the numeric keypad
* Special keys: like Enter, Backspace, Shift, Ctrl, etc.
* Virtual codes: handles keys that are represented by virtual key codes
* The keylogger also features:
* Live console output with timestamps for each key press
* Optional color-coded logging to differentiate between normal, numpad, and special keys
* Automatic log folder creation (logs/)

> *⚠️ Intended for educational purposes only. Don’t use it for malicious activities.*

## Statistics
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![Last Commit](https://img.shields.io/github/last-commit/escobez/keylogger)](https://github.com/escobez/keylogger/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/escobez/keylogger/pulls)
![Issues](https://img.shields.io/github/issues/escobez/keylogger)
![Stars](https://img.shields.io/github/stars/escobez/keylogger?style=social)

## How to use?

1. clone this repo
```bash
git clone https://github.com/escobez/keylogger
```

2. enter in repo
```bash
cd ./keylogger
```

3. install the dependencies
```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

4. run code
```bash
python run.py
```
> If there is an error, don't look for me

## How it works?
the program listens to keyboard input and saves it to a text file (for me it's kind of obvious).
Saves pressed keys into a file in logs/
Special keys saved separately

> don't use this for anything wrong (no matter how difficult it is)

## Contributors
If you want to contribute to this shitty project feel free to help and put your name and username in [CONTRIBUTORS](CONTRIBUTORS.md).