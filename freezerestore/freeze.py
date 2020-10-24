import shutil
import json
import os
from os.path import expanduser
def freeze(filetitle):
    home = expanduser("~")
    with open(home +'/.config/cal/calconfig.json') as f:
        data = json.load(f)
    print(os.getcwd())
    shutil.copy(os.getcwd() + '/' + filetitle, data.get("location", home + "/.calfreeze") + '/' + filetitle + ".temp")
