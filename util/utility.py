import json

def action_checker(value, game):
    with open('util/game_commands.json') as f:
        game_commands = json.loads(f.read())

    return game_commands[game][value]

def profile_creator():
    json_template = {
        'user_name': None,
        'game_list': []
        }
    with open('util/profile.json', 'w') as f:
        f.write(json.dumps(json_template))
        return json_template


def profile_getter():
    try:
        with open('util/profile.json') as f:
            profile = json.loads(f.read())
    except FileNotFoundError:
            profile = profile_creator()
    
    return profile

def save_name(newName):
    print(newName)
    profile = profile_getter()
    profile['user_name'] = newName
    print(profile['user_name'])
    print(profile)