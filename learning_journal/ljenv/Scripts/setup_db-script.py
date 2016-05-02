#!D:\Python_200_Projects\learning_journal\ljenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'learning-journal','console_scripts','setup_db'
__requires__ = 'learning-journal'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('learning-journal', 'console_scripts', 'setup_db')()
    )
