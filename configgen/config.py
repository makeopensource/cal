import json
def config():
    config = {"location": "~/.calfreeze"}
    with open("~/.config/cal/calconfig.json", "w") as f:
        json.dump(config, f)
