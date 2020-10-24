import shutil
import os.path
from os import path

def freeze(filetitle):
    if not path.exists(filetitle):
        return
    shutil.copy(filetitle,filetitle + ".temp")
