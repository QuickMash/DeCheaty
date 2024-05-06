from rcon.source import Client
import tkinter
import random
import sys
sys.path.insert(1, 'src\configs')
import config
config.load('rcon')
password = None
# Message Prompts
if password == 'no_password':
    tkinter.messagebox.showwarning('Warning', 'You are using the default password. Please change it in the settings.conf file.')
elif password == None:
    tkinter.messagebox.showwarning('Warning', 'You have no password set, using default password, set it in settings.conf')
    password = 'no_password'
elif port == None:
    tkinter.messagebox.showwarning('Warning', 'You have no port set, using default port, set it in settings.conf')
    port = 25575
else:
    tkinter.messagebox.showinfo('Info', 'Your RCON password:' + password)
# Functions
def update():
    with Client(ip, port, passwd=password) as client:
        consoleout.insert(Client.send())
def send(command):
    with Client(ip, port, passwd=password) as client:
        consoleout.insert(Client.send(command))[1]
        
def randpasswd(seed):
    random.seed(seed)
    password = random.randint(10000, 999999)
def clear():
    command = None
    print('Command variable cleared.')