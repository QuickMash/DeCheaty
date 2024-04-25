import tkinter
from tkinter import ttk

# Initialize the main window
installer = tkinter.Tk()
installer.title('DeCheaty Installer')
installer.geometry('500x600')

# Initialize the page variable
page = 0
pgmsg = None  # For message labels
entry_path = None  # For the entry on page 2

def create_label(text):
    global pgmsg
    if pgmsg:  # Check if there is an existing label and destroy it if present
        pgmsg.destroy()
    pgmsg = ttk.Label(installer, text=text)
    pgmsg.pack()

def create_entry(initial_text):
    global entry_path
    if entry_path:  # Ensure any existing entry is destroyed first
        entry_path.destroy()
    entry_path = ttk.Entry(installer)
    entry_path.insert(0, initial_text)  # Pre-fill the entry with initial text
    entry_path.pack()

def next():
    global page
    page += 1
    updatepage()

def back():
    global page
    if page > 0:
        page -= 1
    updatepage()

def updatepage():
    global page, entry_path
    if page == 0:
        create_label('Welcome to DeCheaty!\nFor installation, be sure that you have admin\nThen Press next.')
        if entry_path:  # Make sure to clear the entry box when not needed
            entry_path.destroy()
            entry_path = None
    elif page == 1:
        create_label('Step 1: Basic Information.\nPlease enter your details.')
        if entry_path:
            entry_path.destroy()
            entry_path = None
    elif page == 2:
        create_label('Step 2: Installation Settings.\nPlease choose the installation options.')
        create_entry("C:/default/path/")  # Example path
    elif page == 3:
        create_label('Thanks for installing DeCheaty!')
        if entry_path:
            entry_path.destroy()
            entry_path = None
    else:
        create_label('Welcome back to the start of the DeCheaty Installer.')
        if entry_path:
            entry_path.destroy()
            entry_path = None
        page = 0  # Reset to the first page
def install()
    requests.get(entry_path, timeout=5, allow_redirects=True, stream=True, verify=False, proxies=None)
# Navigation buttons
nextbtn = ttk.Button(installer, text='Next', command=next)
backbtn = ttk.Button(installer, text='Back', command=back)
backbtn.pack(side=tkinter.BOTTOM)
nextbtn.pack(side=tkinter.BOTTOM)

installer.mainloop()
