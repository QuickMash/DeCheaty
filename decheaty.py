import rcon
import time
import tkinter
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import platform
import keyboard
import random
import urllib 
import sys
# From File directorys
sys.path.insert(1, 'upgrade')
# Importing From Files
import updater
# Variables
## Setup Variables
window = tkinter.Tk()
console = tkinter.Tk()
## Generic Variables
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
    if version == version:
        upgrade_c = tkinter.messagebox.askquestion(title= window_msg + ' Upgrade', message='There is a newer version. Do you want to update to it?')
        if upgrade_c == 'yes':
            time.sleep(.2)
            quitclient()
            updater.upgrade()
def updateconsole():
    cmd = consolein.get(1.1)
    rconclient.sendcommand(cmd)
    print(cmd)
    print(rconreturn)
    consoleout = tkinter.Label(console, text=cmd)
    consoleout.pack()
# Elements
playerlabel = tkinter.Label(window, text='Players:')
clabel = tkinter.Label(console, text='Game Console:')
consoleout = tkinter.Label(console, text='')
sendbtn = tkinter.Button(console, text="Send", command=send2console)
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