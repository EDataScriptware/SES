import tkinter as tk
import threading
from util.logger import warningLogger

from util.keystroke_listener import keystrokes_detector
from util.utility import profile_getter
from util.discord_file import logged_on
from util.logger import warningLogger
from menubar import menubar_creator

window = tk.Tk()
window.title("SES")

greeting = tk.Label(text="SES Project\nCurrently in development.")
greeting.pack()

profile = profile_getter()
nameEntry = tk.Entry()
profile_name = profile.get('user_name')

if not profile_name:
    nameEntry.insert(0, 'Enter your name...')
else: 
    nameEntry.insert(0, profile_name)

firstclick = True

def on_entry_click(event):
    global firstclick

    if firstclick: 
        firstclick = False
        nameEntry.delete(0, "end")

nameEntry.bind('<FocusIn>', on_entry_click)
nameEntry.pack()

menubar_creator(window)

def start_keystroke(name):
    global running
    if not running:
        x = threading.Thread(target=keystrokes_detector, args=(profile_name, name, window))
        x.start()
        running = True
        logged_on(profile_name, name)
    else:
        warningLogger("A game is already running!")

gameFrame = tk.Frame(window)
gameFrame.pack()

game_list = profile.get('game_list')
game_list_counter = 0
column = 0
row = 0

for game in game_list:
    if (game_list_counter % 4) == 0:
        row = 0
        column += 1 
    
    display_game_text = game.replace('_', ' ').title()
    button = tk.Button(
        gameFrame,
        text=f'Play {display_game_text}',
        width=25,
        height=5,
        bg="white",
        fg="black",
        command=lambda name=display_game_text: start_keystroke(name)
        )
        
    button.grid(row=row, column=column)
    row += 1
    game_list_counter += 1


running = False
window.mainloop()