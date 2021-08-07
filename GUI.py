import tkinter as tk
from tkinter import *
from util.keystroke_listener import everything
from util.discord_file import logged_on
import threading

window = tk.Tk()
window.geometry("625x300") 
window.title("SES")

greeting = tk.Label(text="SES Project\nCurrently in development.")
greeting.grid(column=1, row=0)

nameEntry = tk.Entry()
nameEntry.insert(0, 'Enter your name...')

firstclick = True

def on_entry_click(event):
    """function that gets called whenever name_entry is clicked"""        
    global firstclick

    if firstclick: # if this is the first time they clicked it
        firstclick = False
        nameEntry.delete(0, "end") # delete all the text in the entry

def donothing():
   x = 0

#menu bar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Export", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Redo", command=donothing)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Delete all", command=donothing)
editmenu.add_command(label="Reset to default", command=donothing)
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
aboutmenu.add_command(label="Contact us", command=donothing)
menubar.add_cascade(label="About", menu=aboutmenu)

window.config(menu=menubar)

#name box
nameEntry.bind('<FocusIn>', on_entry_click)
nameEntry.grid(column=0, row=0)

#buttons
button_dead_by_daylight = tk.Button(
    text="Play Dead by Daylight",
    width=25,
    height=5,
    bg="white",
    fg="black"
)

button_phasmophobia = tk.Button(
    text="Play Phasmophobia",
    width=25,
    height=5,
    bg="white",
    fg="grey"
)

button_overwatch = tk.Button(
    text="Play Overwatch",
    width=25,
    height=5,
    bg="white",
    fg="grey"
)

button_dead_by_daylight.grid(column=0, row=1, sticky=tk.N+tk.S+tk.W+tk.E)
button_phasmophobia.grid(column=0, row=2, sticky=tk.N+tk.S+tk.W+tk.E)
button_overwatch.grid(column=0, row=3, sticky=tk.N+tk.S+tk.W+tk.E)


def start_dead_by_daylight(event):
    name = nameEntry.get()
    game = "dead_by_daylight"
    print("Using Dead by Daylight pings")
    x = threading.Thread(target=everything, args=(name, game))
    x.start()
    logged_on(name, "Dead by Daylight")

def start_phasmophobia(event):
    name = nameEntry.get()
    game = "phasmophobia"
    print("Using Phasmophobia pings")
    x = threading.Thread(target=everything, args=(name, game))
    x.start()
    logged_on(name, "Phasmophobia")

button_dead_by_daylight.bind("<Button-1>", start_dead_by_daylight)
button_phasmophobia.bind("<Button-1>", start_phasmophobia)

window.mainloop()
