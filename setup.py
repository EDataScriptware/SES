from distutils.core import setup
import py2exe


Mydata_files = [
    ('util', ['util/profile.json']),
    ('util', ['util/game_commands.json'])
]

setup(
        options = {'py2exe': {'bundle_files': 1, 'compressed': False}},
        console=['GUI.py'],
        data_files = Mydata_files,
)
