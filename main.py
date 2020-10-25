import argparse
import sys
import os

from project import make_project


if __name__ == "__name__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project", action = "store_true")
    parser.add_argument("dir_name", action = "store_true")

    args = parser.parse_args()

    currdir = os.getcwd() # current directory

    # creates a project, assigns project to directory if PATH defined.
    if (args.project):
        make_project.mkprj(args.dir_name)

