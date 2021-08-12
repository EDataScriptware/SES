import json
from GUI import profile_name

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


def profile_get():
    try:
        with open('util/profile.json') as f:
            profile = json.loads(f.read())
    except FileNotFoundError:
            profile = profile_creator()
    
    return profile

def profile_name_get():
    return profile_get().get('user_name')

def profile_name_update(name):
    global profile_name
    profile_name = name

def save_name(item):
    load_file = open('util/profile.json', 'r')
    json_object = json.load(load_file)
    load_file.close()

    name = item.get()
    json_object["user_name"] = name
    print(name)

    dump_file = open('util/profile.json', 'w')
    json.dump(json_object, dump_file)
    dump_file.close()

    profile_name_update(name)