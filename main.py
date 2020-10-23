import argparse
import sys
import os

from project import make_project as mp


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("argA")
    parser.add_argument("--projectname", action="store_true")

    args = parser.parse_args()

    # creates a project, assigns project to directory if PATH defined.
    if (args.argA == "project"):
        print("creating project...")
        mp.make_project()
        sys.exit(0)

    elif args.project and args.projectname:
        print("creating project...")
        mp.make_project(args.projectname)
        sys.exit(0)

    else:
        print("project creation failed")
