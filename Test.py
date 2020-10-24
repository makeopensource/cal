""" Args parse Implemented and View """
import sys
import os


def mkprj(path=os.getcwd()):
    if path != os.getcwd():
        os.mkdir(path)
        return path
    else:
        separator = "\\"  # path separator (change for linux)
        return path.split(separator)[-1]


print(mkprj())
{"Name Of File": "List of data about project"}
["List of data about project : Due date, path ", "submission file"]


def listDirectory(dictionary):
    print("Projects:")
    # This is mostly for formating purposes

    for fileName in dictionary.keys():
        value = dictionary.get(fileName)
        retval = fileName + '  '
        for item in value:
            retval += item + '  '
        print(retval)

listDirectory({"Project1": ["10/28/2020", "usr/test/Projects", "project.zip"],
               "Project2": ["10/28/2020", "usr/test/Projects", "project2.tar"],
               "Special3": ["10/31/2020", "usr/test/Projects", "Project3.py"]})
