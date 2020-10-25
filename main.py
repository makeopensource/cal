import argparse
import sys
import os
from project import check as c
<<<<<<< HEAD
from project import make_project as mp
from project import submit as s
=======
from project import make_project as p
>>>>>>> ed8805eee4eda2f819f85dc43e16f718bc6877a9
from project.freezerestore import freeze as f
from project.freezerestore import restore as r

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", action="store", type=str)
    parser.add_argument("--argname", default="", action="store", type=str)

    arg = parser.parse_args()

    if arg.operation == "project":
        if arg.argname == "":
            print("Creating project...")
            p.make_project()
            sys.exit(0)
        else:
            print("Creating project...")
            p.make_project(arg.argname)
            sys.exit(0)
    elif arg.operation == "check":
        if arg.argname == "":
            print("You didn't give a project name!")
        else:
            print("Checking project status...")
            c.check(arg.argname)
            sys.exit(0)
    elif arg.operation == "submit":
        if arg.argname == "":
            print("You didn't give a project name!")
        else:
            print("Opening submit link...")
            s.submit("")
            sys.exit(0)
    elif arg.operation == "freeze":
        if arg.argname == "":
            print("You didn't input a file name!")
        else:
            print("Freezing file " + arg.argname + ".")
            f.freeze(arg.argname)
            sys.exit(0)
    elif arg.operation == "restore":
        if arg.argname == "":
            print("You didn't input a file name!")
        else:
            print("Restoring file " + arg.argname + ".")
            r.restore(arg.argname)
            sys.exit(0)

    else:
        print("Command not found.")
