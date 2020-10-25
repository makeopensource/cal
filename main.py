import argparse
import sys
import os
from project import check as c
from project import submit as s
from project import make_project as p
from project.freezerestore import freeze as f
from project.freezerestore import restore as r
import sqlite3

def main():
    if __name__ == "__main__":
        # setup sqlite server
        conn = sqlite3.connect('projects.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS projects
                (name text, duedate text, course text, semester text, assignment text,  path text)''')
        
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
            print("Checking project status...")
            c.check()
            sys.exit(0)
        elif arg.operation == "submit":
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
