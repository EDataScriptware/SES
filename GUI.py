import tkinter as tk
import threading

from util.keystroke_listener import keystrokes_detector
from util.utility import profile_getter
from util.discord_file import logged_on
from menubar import menubar_creator
from functools import partial

window = tk.Tk()
window.geometry("625x300") 
window.title("SES")

greeting = tk.Label(text="SES Project\nCurrently in development.")
greeting.grid(column=1, row=0)

profile = profile_getter()
nameEntry = tk.Entry()

if not profile.get('user_name'):
    nameEntry.insert(0, 'Enter your name...')
else: 
    nameEntry.insert(0, profile.get('user_name'))

firstclick = True

def on_entry_click(event):
    global firstclick

    if firstclick: 
        firstclick = False
        nameEntry.delete(0, "end")

nameEntry.bind('<FocusIn>', on_entry_click)
nameEntry.grid(column=0, row=0)

menubar_creator(window)

def start_keystroke(event, name):
    global running
    if not running:
        x = threading.Thread(target=keystrokes_detector, args=(name, game, window))
        x.start()
        running = True
        logged_on(name, display_game_text)
    else:
        print("A game is already running!")

game_list = profile.get('game_list')
game_list_counter = 1

for game in game_list:

    display_game_text = game.replace('_', ' ').title()
    print(display_game_text)
    button = tk.Button(
        text=f'Play {display_game_text}',
        width=25,
        height=5,
        bg="white",
        fg="black"
        )

    button.grid(column=0, row=game_list_counter, sticky=tk.N+tk.S+tk.W+tk.E)
    button.bind("<Button-1>", lambda event: start_keystroke(event, game))
    game_list_counter += 1



running = False
window.mainloop()