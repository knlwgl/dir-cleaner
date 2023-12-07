import os
import shutil
from pathlib import Path

dir = input("Directory? >")
if (not dir): 
    dir = os.path.curdir
    print("Cleaning current directory...")
else:
    print("Cleaning ", dir)


for filepath in os.listdir(dir):
    path = Path(f"{dir}/{filepath}")
    ext = os.path.splitext(filepath)[1][1:].upper()
    if (path.is_file() and not ext and not ext == "PY"):
        if (filepath.startswith("Screenshot")):
            ext = "SCREENSHOT"
        if not os.path.exists(f"{dir}/{ext}"):
            os.mkdir(f"{dir}/{ext}")
        shutil.move(f"{dir}/{filepath}", f"{dir}/{ext}/{filepath}")
        print(f"Moving {filepath} to {dir}/{ext}")