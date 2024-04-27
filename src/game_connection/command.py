import tkinter.messagebox
import rcon
from rcon.source import Client
import tkinter
import random
dcommand = ''
returned = ''
config = open('src\configs\settings.conf')
# Configs
for line in config:
    if line.startswith('rconaddress'):
        ip = line.split(' ')[1]
    if line.startswith('rconport'):
        port = line.split(' ')[1]
    if line.startswith('rconpassword'):
        password = line.split(' ')[1]
    if line.startswith('defaultcommand'):
        dcommand = line.split(' ')[1]
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
def send(command):
    with Client(ip, port, passwd=password) as client:
        client.send(command)