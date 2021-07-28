from pynput.keyboard import Listener
from utility import action_checker

key_sequence = []
combo = False

def on_press(key):
    global combo
    print("Key pressed: {0}".format(key))
    concat_string = ""
    if (combo == True):
        key_sequence.append(key)
        print(key_sequence)
    if(format(key).strip("'").lower() == 'v' and (combo == False)):
        combo = True
        key_sequence.append(key)
        print(key_sequence)
    if len(key_sequence) == 3:
        combo = False
        for key_sequence_value in key_sequence:
            concat_string += str(key_sequence_value).strip("'").lower()
        try:
            print(action_checker(concat_string))
        except:
            print(f'{concat_string} command not found!')
        key_sequence.clear()


with Listener(on_press=on_press) as listener:
    listener.join()
