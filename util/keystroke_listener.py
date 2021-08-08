import platform
from sys import exit

if platform.system() != "Windows":
    from pynput.keyboard import Listener

from .discord_file import send_message
from .utility import action_checker
from .logger import errorLogger, infoLogger

combo = False
def keystrokes_detector(name, game, window): 
    key_sequence = []
    game = game.replace(' ', '_').lower()
    def on_press(key):
        global combo
        check_window_running(window)
        infoLogger("Key pressed: {0}".format(key))
        concat_string = ""
        if combo:
            key_sequence.append(key)
            infoLogger(key_sequence)
        if(format(key).strip("'").lower() == 'v' and not combo):
            combo = True
            key_sequence.append(key)
            infoLogger(key_sequence)
        if len(key_sequence) == 3:
            combo = False
            for key_sequence_value in key_sequence:
                concat_string += str(key_sequence_value).strip("'").lower()
            try:
                infoLogger(name + ": " + action_checker(concat_string, game))
                send_message(name + ": " + action_checker(concat_string, game))
            except Exception as e:
                errorLogger(e)
                infoLogger(f'{concat_string} command not found!')
            key_sequence.clear()

    with Listener(on_press=on_press) as listener:
        listener.join()


def check_window_running(window):
    try:
        if 'normal' == window.state():
            pass
    except: 
        infoLogger('The window is no longer running.')
        exit()
