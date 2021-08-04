from pynput.keyboard import Listener
from util.utility import action_checker
from util.discord_file import send_message, logged_on

key_sequence = []
combo = False

name = input("Please type in your name: ")
print("[1] Dead by Daylight")
print("[2] Phasmophobia")

game = int(input("What game would you like to play: "))
if game == 1:
    game = "dead_by_daylight"
    logged_on(name, "Dead by Daylight")
elif game == 2: 
    game = "phasmophobia"
    logged_on(name, "Phasmophobia")
else:
    print("Game not selected. Ending...")
    exit(0)

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
