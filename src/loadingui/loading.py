# This is so users know that the program is loading incase it being slow
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

load = tk.Tk()
load.title("Loading...")
load.geometry("300x100")
load.resizable(False, False)
load.configure(bg="#000000")
load.attributes("-topmost", True)
logo = tk.PhotoImage(file="src/images/suspicious.png")
tk.Text = tk.Label(load, text="Loading DeCheaty...", foreground='#FFFFFF', background='#000000')
logo.pack()
tk.Text.pack()
load.mainloop()