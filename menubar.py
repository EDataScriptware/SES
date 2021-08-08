from tkinter import Menu
from sys import exit

def menubar_creator(window):
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=do_nothing)
    filemenu.add_command(label="Open", command=do_nothing)
    filemenu.add_command(label="Save", command=do_nothing)
    filemenu.add_command(label="Save As", command=do_nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_program)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Redo", command=do_nothing)
    editmenu.add_command(label="Undo", command=do_nothing)
    editmenu.add_command(label="Delete All", command=do_nothing)
    editmenu.add_command(label="Reset to Default", command=do_nothing)
    menubar.add_cascade(label="Edit", menu=editmenu)

    viewmenu = Menu(menubar, tearoff=0)
    viewmenu.add_command(label="Games", command=do_nothing)
    viewmenu.add_command(label="Hotkeys", command=do_nothing)
    menubar.add_cascade(label="View", menu=viewmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Tutorial", command=do_nothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    aboutmenu = Menu(menubar, tearoff=0)
    aboutmenu.add_command(label="Upgrade", command=do_nothing)
    aboutmenu.add_command(label="Donate", command=do_nothing)
    aboutmenu.add_command(label="Contact Us", command=do_nothing)
    menubar.add_cascade(label="About", menu=aboutmenu)
    
    window.config(menu=menubar)


def do_nothing():
   x = 0

def exit_program():
    exit(0)