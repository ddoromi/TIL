#!C:\Users\student\SSAFY\TIL\Programming\07_Django\INSTA\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'kit==0.2.15','console_scripts','kit'
__requires__ = 'kit==0.2.15'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('kit==0.2.15', 'console_scripts', 'kit')()
    )
