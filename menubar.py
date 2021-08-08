from tkinter import Menu

def menubar_creator(window):
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save As", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Redo", command=donothing)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_command(label="Delete All", command=donothing)
    editmenu.add_command(label="Reset to Default", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)

    viewmenu = Menu(menubar, tearoff=0)
    viewmenu.add_command(label="Games", command=donothing)
    viewmenu.add_command(label="Hotkeys", command=donothing)
    menubar.add_cascade(label="View", menu=viewmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Tutorial", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    aboutmenu = Menu(menubar, tearoff=0)
    aboutmenu.add_command(label="Upgrade", command=donothing)
    aboutmenu.add_command(label="Donate", command=donothing)
    aboutmenu.add_command(label="Contact Us", command=donothing)
    menubar.add_cascade(label="About", menu=aboutmenu)
    
    window.config(menu=menubar)


def donothing():
   x = 0