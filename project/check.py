""" Args parse Implemented and View """
import sys
import os


def listDirectory(dictionary):
    print("Projects:")
    # This is mostly for formating purposes

    for fileName in dictionary.keys():
        value = dictionary.get(fileName)
        retval = fileName + '  '
        for item in value:
            retval += item + '  '
        print(retval)


