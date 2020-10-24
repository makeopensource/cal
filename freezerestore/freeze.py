import shutil
import json
import os

def freeze(filetitle):
    with open('../config.json') as f:
        data = json.load(f)
    print(os.getcwd())
    shutil.copy(os.getcwd() + '/' + filetitle, data.get("location", "~/.calfreeze") + filetitle)