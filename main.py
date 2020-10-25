import argparse
import sys
import os
import project as p

from project import make_project as mp


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", action="store", type=str)
    parser.add_argument("--argname", default="", action="store", type=str)

    args = parser.parse_args()

    if arg.operation == "project":
        if arg.argname == "":
            print("Creating project...")
            p.make_project()
            sys.exit(0)
        elif:
            print("Creating project...")
            p.make_project(arg.argname)
            sys.exit(0)
    elif arg.operation == "check":
        if arg.argname == "":
            print("You didn't give a project name!")
        elif:
            print("Checking project status...")
            p.check(arg.argname)
            sys.exit(0)
    elif arg.operation == "freeze":
        if arg.argname == "":
            print("You didn't input a file name!")
        elif:
            print("Freezing file " + arg.argname + ".")
            p.freeze(arg.argname)
            sys.exit(0)
    elif arg.operation == "restore":
        if arg.argname == "":
            print("You didn't input a file name!")
        elif:
            print("Restoring file " + arg.argname + ".")
            p.restore(arg.argname)
            sys.exit(0)

    else:
        print("Command not found.")
