from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')

packages = [
    'reportlab.rl_settings',
]

dll_excludes = ['MSVCP90.dll']


setup( 
  options = {         
    'py2exe' : {
        'compressed': 1, 
        'optimize': 2,
        'bundle_files': 2, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': 'dist',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        'packages': packages,
        'dll_excludes': dll_excludes,
        }
        },
  console = ['main.py'],
)