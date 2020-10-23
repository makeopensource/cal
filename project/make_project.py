""" Args parse Implemented and View """
import sys
import os

def mkprj(local_path="./"):
    curr_path = os.getcwd()
    separator = "/"  # path separator (change for linux)

    # turn current directory into project
    if local_path == "./":
        return (curr_path.split(separator)[-1], curr_path)

    # make new project directory
    else:
        new_path = curr_path + separator + local_path

        try:
            os.mkdir(local_path)
            return (local_path, new_path)
        except FileExistsError:
            print("file already exists")

print(mkprj("newproject"))
