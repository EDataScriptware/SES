import json

def action_checker(value):
    with open('mem/game_commands.json') as f:
        game_commands = json.loads(f.read())

    return game_commands[value]