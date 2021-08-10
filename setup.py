from distutils.core import setup
import py2exe


Mydata_files = []

setup(
        options = {'py2exe': {'bundle_files': 1, 'compressed': False}},
        windows=['GUI.pyw'],
        data_files = Mydata_files,
)
