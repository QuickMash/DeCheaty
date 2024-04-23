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
window_msg = open(r'src/configs/window-message.conf', 'r')
def connect():
    tf2_dir = open('src/configs/tf2-dir.conf', 'r')
    _passwd = random.randint(123832, 98239823)
    # Use 127.0.0.0 instead of localhost to connect to the server
    # In case of a local server with the hostname of localhost
    tkinter.messagebox.askquestion(title=window_msg, message="Hi")
window = tkinter.Tk()
window.title(window_msg)
window.geometry('600x300')
window.resizable(True, True)
connect()
window.mainloop()