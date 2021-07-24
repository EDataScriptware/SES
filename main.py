from pynput.keyboard import Listener
from enum_lookups import action_checker

key_sequence = []

def on_press(key):
    print("Key pressed: {0}".format(key))
    concat_string = ""
    key_sequence.append(key)
    print(key_sequence)
    if len(key_sequence) == 3:
        for key_sequence_value in key_sequence:
            concat_string += str(key_sequence_value).strip("'").lower()
        try:
            print(action_checker(concat_string))
        except:
            print(f'{concat_string} command not found!')
        key_sequence.clear()


with Listener(on_press=on_press) as listener:
    listener.join()
