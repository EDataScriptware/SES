from pynput.keyboard import Listener
from util.discord_file import send_message
from util.utility import action_checker

combo = False
def everything(name, game): 
    key_sequence = []

    def on_press(key):
        global combo
        print("Key pressed: {0}".format(key))
        concat_string = ""
        if combo:
            key_sequence.append(key)
            print(key_sequence)
        if(format(key).strip("'").lower() == 'v' and not combo):
            combo = True
            key_sequence.append(key)
            print(key_sequence)
        if len(key_sequence) == 3:
            combo = False
            for key_sequence_value in key_sequence:
                concat_string += str(key_sequence_value).strip("'").lower()
            try:
                print(name + ": " + action_checker(concat_string, game))
                send_message(name + ": " + action_checker(concat_string, game))
            except Exception as e:
                print(e)
                print(f'{concat_string} command not found!')
            key_sequence.clear()

    with Listener(on_press=on_press) as listener:
        listener.join()
