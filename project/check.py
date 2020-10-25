""" Args parse Implemented and View """
import sys
import os
import json
def check():
    print("Projects:")
    if os.path.isfile("metadata.json"):
        with open("metadata.json", "r") as f:
            meta = json.load(f)
    else:
        meta = {}
    # This is mostly for formatting purposes
    for keys in meta.keys():
        print(meta.get(keys, {}))
