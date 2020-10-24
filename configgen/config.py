import json
import os
from os.path import expanduser

def config():
    home = expanduser("~")
    config = {"location": home + "/.calfreeze"}
    with open("~/.config/cal/calconfig.json", "w") as f:
        json.dump(config, f)
