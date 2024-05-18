import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import rcon
import time
import platform
import keyboard
import random
import requests
import sys

# From File directories
sys.path.insert(1, 'upgrade')
sys.path.insert(1, 'rc')
sys.path.insert(1, 'rc/loadingui')
sys.path.insert(1, 'rc/game_connection')
sys.path.insert(1, 'rc/configs')

# Importing From Files
import updater
import config
import command
import dcmanage

# Variables
## Setup Variables
window = tk.Tk()
console = tk.Tk()
## Generic Variables
# Setup
version = config.load('version')
print(version)
window.title(version + 'ain')
console.title(version + 'ame Console')
window.geometry('600x300')  
console.geometry('300x400')  
window.resizable(True, True)
console.resizable(False, True)

# Functions
def send_command():
    command = consolein.get("1.0", "end-1c")
    dcmanage.updateconsole(command)
    consolein.delete("1.0", "end")

# Elements
playerlabel = ttk.Label(window, text='Players:')
playerlabel.pack(side=tk.TOP, fill=tk.X)

consoleout = tk.Text(console, height=10, width=280)
consolescroll = ttk.Scrollbar(console, orient=tk.VERTICAL, command=consoleout.yview)
consoleout.config(yscrollcommand=consolescroll.set)
consoleout.grid(row=0, column=0, sticky='nsew')
consolescroll.grid(row=0, column=1, sticky='ns')

consolein = tk.Text(console, height=1, width=40)
consolein.grid(row=1, column=0, pady=(5, 0), sticky='ew')

sendbtn = ttk.Button(console, text="Send", command=send_command)
sendbtn.grid(row=1, column=1, pady=(5, 0), sticky='ew')

playerlist = tk.Text(window)
playerlist.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Program
consoleout.insert("end", 'ame Console\nBy QuickMash\nUse dc to interact with DeCheaty Commands\n')

# Resizing configuration for console frame grid
console.grid_columnconfigure(0, weight=1)
console.grid_rowconfigure(0, weight=1)

dcmanage.checkupdate()

def keybinding():
    print('Keybinding was pressed')

keyboard.add_hotkey('ctrl+q', keybinding)

console.mainloop()
window.mainloop()