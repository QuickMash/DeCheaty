import requests
# File able to append
config = open('src/configs/settings.conf', 'a+')
def upgrade():
    cupdate = config.readline(3)
    if cupdate != 'True':
        #response = requests.get('https://github.com/decheaty/releases/latest', allow_redirects=True, timeout=20)
        print(response.status_code)
        if response.status_code == '200':
            print()
        else:
            print()
    elif cupdate == 'True':
        eupdate = tkinter.messagebox.askquestion(window_msg + 'Upgrade', 'Would you like to enable updates?')
        if eupdate == 'yes':
            rmcancelupgrade()
        elif eupdate == 'no':
            cancelnextupgrade()
        else:
            print('Unexpected Input')
    else:
        print('Unexpected Input')
def cancelnextupgrade():
    config.seek(3)
    # Set Value to false
    config.write('True')
def rmcancelupgrade():
    config.seek(3)
    # Set Value to false
    config.write('False')