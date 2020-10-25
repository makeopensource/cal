import argparse
import sys
import os

from project import make_project as mp


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", action="store", type=str)
    parser.add_argument("--argname", default="", action="store", type=str)

    args = parser.parse_args()

    if operation == "project":
        print("make a project (use code from github)")
    elif operation == "check":
        print("use check (needs projectname)")
    elif operation == "freeze":
        print("run freeze (needs filename)")
    elif operation == "restore":
        print("run restore (also needs filename)")
    else:
        print("Command not found.")
