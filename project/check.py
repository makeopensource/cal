""" Args parse Implemented and View """
import sys
import os
import json


def check():
    if os.path.isfile("./metadata.json"):
        with open("./metadata.json", "r") as f:
            meta = json.loads(f.read())

            for key in meta:
                if len(key) >= 8:
                    print(f"{key}\t{meta.get(key)}")
                else:
                    print(f"{key}\t\t{meta.get(key)}")

    else:
        print("no projects created!")
