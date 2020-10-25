""" Args parse Implemented and View """
import sys
import os
import json
def listDirectory():
    print("Projects:")
    if os.path.isfile("metadata.json"):
        with open("metadata.json", "r") as f:
            meta = json.load(f)
    else:
        meta = {}
    # This is mostly for formating purposes
    for keys in meta.keys():
        print(meta.get(keys, ""))
