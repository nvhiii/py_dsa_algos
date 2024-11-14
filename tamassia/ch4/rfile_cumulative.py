# pseudocode for cumulative file storage system
from os import path, listdir

def file_space(p):
    total = path.getsize(p)
    if path.isdir(p): # do check if str is valid
        for f in listdir(p):
            childpath = path.join(p, f)
            total += path.getsize(childpath)

    return total

