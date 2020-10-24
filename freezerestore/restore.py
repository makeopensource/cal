import shutil
import os.path
from os import path

def restore(filetitle):
    if not path.exists(filetitle):
        return
    if not path.exists(filetitle + ".temp"):
        return
    shutil.move(filetitle, filetitle + ".temp2")
    shutil.move(filetitle + ".temp", filetitle)
    shutil.move(filetitle + ".temp2", filetitle + ".temp")
