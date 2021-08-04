import tkinter as tk
from util.keystroke_listener import everything

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


nameEntry.bind('<FocusIn>', on_entry_click)
nameEntry.grid(column=0, row=0)


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

button_dead_by_daylight.grid(column=0, row=1, sticky=tk.N+tk.S+tk.W+tk.E)
button_phasmophobia.grid(column=0, row=2, sticky=tk.N+tk.S+tk.W+tk.E)


def start_dead_by_daylight(event):
    name = nameEntry.get()
    game = "dead_by_daylight"
    print("Startng Dead by Daylight...")
    everything(name, game).start()

def start_phasmophobia(event):
    name = nameEntry.get()
    game = "phasmophobia"
    print("Startng Phasmophobia...")
    everything(name, game).start()



button_dead_by_daylight.bind("<Button-1>", start_dead_by_daylight)
button_phasmophobia.bind("<Button-1>", start_phasmophobia)


window.mainloop()
