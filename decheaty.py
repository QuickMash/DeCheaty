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
sys.path.insert(1, 'src/loadingui')
sys.path.insert(1, 'src/game_connection')
# Importing From Files
import updater
import command
# Variables
## Setup Variables
window = tkinter.Tk()
console = tkinter.Tk()
## Generic Variables
lines = 0
cmd = None
remote_version = 'Error'
# Setup
v = open('upgrade/version.txt')
version = v.read()
winmsg = open('src/configs/window-message.conf', 'r')
config = open('src/configs/settings.conf', 'r')
for line in config:
    if line.startswith('consolebg'):
        consolebg = line.split(' ')[1]
    if line.startswith('consolefg'):
        consolefg = line.split(' ')[1]
fg = '#' + consolefg
bg = '#' + consolebg
window_msg = winmsg.read()
window.title(window_msg + ' Main')
console.title(window_msg + ' Game Console')
window.geometry('600x300')  
console.geometry('300x400')  
window.resizable(True, True)
window.resizable(True, True)
console.config(bg=bg, fg=fg)
# Functions
def quitclient():
    window.destroy()
    console.destroy()
def checkupdate():
    if version != remote_version:
        upgrade_c = tkinter.messagebox.askquestion(title= window_msg + ' Upgrade', message='There is a newer version. Do you want to update to it?\nNote: This is highly recommended, newer versions may have a better upgrader.')
        if upgrade_c == 'yes':
            time.sleep(.2)
            quitclient()
            updater.upgrade()
        elif upgrade_c == 'no':
            print('Not Updating')
        elif remote_version == 'Error':
            # Quite Important, if not connected to internet, the program might break
            tkinter.messagebox.showerror(title= window_msg + ' Error', message='Cannot Connect to GitHub!\nBe sure you are connected to internet.')
        else:
            tkinter.messagebox.showerror(title= window_msg + ' Error', message='Unexpected Input')
def updateconsole():
    global lines
    global cmd
    cmd = consolein.get("1.0", "end-1c")
    command.send(cmd)
    consoleout.insert("end", '>>> '+ cmd + '\n')
    consoleout.insert("end", command.returned() + '\n')
# Elements
playerlabel = ttk.Label(window, text='Players:')
consoleout = tkinter.Text(console, height=10, width=280, bg=consolebg, fg=consolefg)
consolescroll = ttk.Scrollbar(console, orient=tkinter.VERTICAL, command=consoleout.yview)
consoleout.config(yscrollcommand=consolescroll.set)
consoleout.grid(row=0, column=0, sticky='nsew')
consolescroll.grid(row=0, column=1, sticky='ns')
consolein = tkinter.Text(console, height=1, width=40)
consolein.grid(row=1, column=0, pady=(5, 0), sticky='ew')
sendbtn = ttk.Button(console, text="Send", command=updateconsole)
sendbtn.grid(row=1, column=1, pady=(5, 0), sticky='ew')
# Program
consoleout.insert("end", window_msg + ' Game Console\nBy QuickMash\nNote: This console is only a remote console and cannot interact with the program.\n')
# Resizing configuration for console frame grid
console.grid_columnconfigure(0, weight=1)
console.grid_rowconfigure(0, weight=1)
playerlabel.pack(side=tkinter.TOP, fill=tkinter.X)
checkupdate()
console.mainloop()
window.mainloop()