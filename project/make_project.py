""" Args parse Implemented and View """
import sys
import os
import json

def mkprj(local_path="./"):
    course = input("Course Name (i.e. CSE220):")
    semester = input("Semester (f for fall, s for spring, i.e. f20, s19):")
    assignment = input("FULL ASSIGNMENT NAME from Autograder:")
    retdict = {"course": course,"semester":semester, "assignment":assignment}
    retjson = json.dumps(retdict)
    curr_path = os.getcwd()
    separator = "/"  # path separator (change for linux)

    # turn current directory into project
    if local_path == "./":
        with open('metadata.json', 'w') as outfile:
            json.dump(retjson, outfile)
        return (curr_path.split(separator)[-1], curr_path)

    # make new project directory
    else:
        new_path = curr_path + separator + local_path

        try:
            os.mkdir(local_path)
            with open('metadata.json', 'w') as outfile:
                json.dump(retjson, outfile)
            return (local_path, new_path)
        except FileExistsError:
            print("file already exists")

print(mkprj("newproject"))
