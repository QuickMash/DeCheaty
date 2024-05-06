config = open('settings.conf', 'a+')
api = None
password = None
ip = None
port = None
winmsg = None
for line in config:
    if line.startswith('steamapi'):
        api = line.split('=')[1]
    elif line.startswith('password'):
        password = line.split('=')[1]
    elif line.startswith('address'):
        ip = line.split('=')[1]
    elif line.startswith('port'):
        port = line.split('=')[1]
    elif line.startswith('winmsg'):
        winmsg = line.split('=')[1]
def load(address):
    if address == 'all':
        return api, password, ip, port, winmsg
    elif address == 'rcon':
        return api, port, ip, password
    elif address == 'steam':
        return api
    elif address == 'version':
        return winmsg
    else:
        return 'Cannot Get Request, Undefined'