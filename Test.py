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

