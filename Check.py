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



def listDirectory(dictionary):
    print("Projects:")
    # This is mostly for formating purposes

    for fileName in dictionary.keys():
        value = dictionary.get(fileName)
        retval = fileName + '  '
        for item in value:
            retval += item + '  '
        print(retval)


