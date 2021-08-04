import json

def action_checker(value, game):
    with open('util/game_commands.json') as f:
        game_commands = json.loads(f.read())

    return game_commands[game][value]