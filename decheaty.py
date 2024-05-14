import tkinter.messagebox
import rcon
import time
import tkinter
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import platform
import keyboard
import random
import requests
import sys
# From File directorys
sys.path.insert(1, 'upgrade')
sys.path.insert(1, 'src')
sys.path.insert(1, 'src\loadingui')
sys.path.insert(1, 'src\game_connection')
sys.path.insert(1, 'src\configs')
# Importing From Files
import updater
import config
import command
import dcmanage
# Variables
## Setup Variables
window = tkinter.Tk()
console = tkinter.Tk()
## Generic Variables
# Setup
version = config.load('version')
print(version)
window.title(version + ' Main')
console.title(version + ' Game Console')
window.geometry('600x300')  
console.geometry('300x400')  
window.resizable(True, True)
window.resizable(True, True)
# Functions
# Elements
playerlabel = ttk.Label(window, text='Players:')
consoleout = tkinter.Text(console, height=10, width=280)
consolescroll = ttk.Scrollbar(console, orient=tkinter.VERTICAL, command=consoleout.yview)
consoleout.config(yscrollcommand=consolescroll.set)
consoleout.grid(row=0, column=0, sticky='nsew')
consolescroll.grid(row=0, column=1, sticky='ns')
consolein = tkinter.Text(console, height=1, width=40)
consolein.grid(row=1, column=0, pady=(5, 0), sticky='ew')
sendbtn = ttk.Button(console, text="Send", command=dcmanage.updateconsole)
sendbtn.grid(row=1, column=1, pady=(5, 0), sticky='ew')
playerlist =tkinter.Text(window)
# Program
consoleout.insert("end", window_msg + ' Game Console\nBy QuickMash\nUse dc to interact with DeCheaty Commands\n')
# Resizing configuration for console frame grid
console.grid_columnconfigure(0, weight=1)
console.grid_rowconfigure(0, weight=1)
playerlabel.pack(side=tkinter.TOP, fill=tkinter.X)
dcmanage.checkupdate()
console.mainloop()
window.mainloop()
