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
# Importing From Files
import updater
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
window_msg = winmsg.read()
window.title(window_msg + ' Main')
console.title(window_msg + ' Game Console')
window.geometry('600x300')  
console.geometry('300x400')  
window.resizable(True, True)
window.resizable(True, True)
# Functions
def send2console():
    updateconsole()
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
    lines += 1
    
    # Create a new label for the console output
    
    # If there are 3 labels, remove the first one
    if lines > 2:
        consoleout.pack_forget()
        consoleout.destroy()
        consoleout = new_label
    else:
        consoleout = new_label
    
    # If there are 10 labels, add a clear button
    if lines == 10:
        clear_button.pack()
        lines = 0

def clear_console():
    global consoleout
    global lines
    
    # Clear the console output
    consoleout.pack_forget()
    consoleout.destroy()
    consoleout = tkinter.Label(console, text='')
    lines = 0

# Elements
playerlabel = ttk.Label(window, text='Players:')
clabel = ttk.Label(console, text='Game Console:')
consoleout = ttk.Label(console, text='')
sendbtn = ttk.Button(console, text="Send", command=send2console)
consolein = tkinter.Text(console, height = 1, width = 20)
# Program 
# Window Window
playerlabel.pack()
# Console Window
clabel.pack()
consoleout.pack()
consolein.pack() 
sendbtn.pack() 
## Wait a second before calling update dialog
time.sleep(1)
checkupdate()
console.mainloop()
window.mainloop()