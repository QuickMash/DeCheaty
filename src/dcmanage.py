import sys
sys.path.insert(1, 'src\configs')
import config
# Default Config
player = 'QuickMash'
def kick(player):
    rcon.send('kick' + player)
def tellkick(player):
    rcon.send("say" + kickmsg)
def createmsg(message, index):
        messages = open('msgs.txt', 'a+')
        if index != (''|' '):
            message.write( 'message' + index'="'+message+'"')
            return "Wrote to file!"
        else:
            print('Error! Index cannot be blank')
def readmsg(indexnumber):
    messages = open('msgs.txt', 'r')
if indexnumber != (""|" ")
    msgr = messages.read()
        for line in msgsr:
            if line.startswith('message' + indexnumber):
                replyedmsg = line.split('"=')[1].split('"')[0]
                return replymsg
elif indexnumber > 0:
    return "The indexnumber is not positive!"
elif indexnumber == None:
    return "The index number cannot be None"
elif indexnumber == ('debug'|'dbc'|'cat'):
    print('I am always watching')
    return 'iwatchu'
else:
    return "The indexnumber was not defined. newcmd([indexnumber here])"
def quitclient():
    window.destroy()
    console.destroy()
def checkupdate():
    if config.load('version') != remote_version:
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
    global dcprefix
    cmd = consolein.get("1.0", "end-1c")
    if cmd == '':
        pass
    elif cmd == 'exit':
        quitclient()
    elif cmd == 'clear':
        consoleout.delete(1.0, "end")
    # If the command starts with decheaty:
    elif cmd.startswith('dc'):
        # DeCheaty Commands
        # Take DeCheat prefix off, no matter what one was used
        dccmd = cmd.replace('dc', '')
        if dccmd == '':
            consoleout.insert("end", 'DeCheaty Command Helper\n')
        elif dccmd == (' help'):
            consoleout.insert("end", 'DeCheaty Command Helper\n')   
        elif dccmd == (' quit all'):
            quitclient()
            if window():
                print('hi')
        elif dccmd == (' quit'):
            console.destroy()
        elif dccmd == (' msgedit'):
            consoleout.insert("end", 'Opening Message Editor...\n') 
        elif dccmd == (' quit main'):
            window.destroy()
        elif dccmd == (' user ' + (player)):
            # Get info about the player...
        else:
            consoleout.insert("end", 'Unknown Command! Use HELP for help\n')
    else:
        command.send(cmd)
        consoleout.insert("end", '>>> '+ cmd + '\n')
        consoleout.insert("end", command.returned() + '\n')
