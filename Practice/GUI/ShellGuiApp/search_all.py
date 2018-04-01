"""
Searches for specific string in files in specific directory and its subdirectories

Usage:
> python search_all.py startdir searchstring
"""


import os
import sys


listonly = False
textext = ['.py', '.txt']


def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    for (thisdir, subshere, fileshere) in os.walk(startdir):
        for file in fileshere:
            fpath = os.path.join(thisdir, file)
            visitfile(fpath, searchkey)
    print('Found in {0} files, visited {1}'.format(fcount, vcount))


def visitfile(fpath, searchkey):
    global fcount, vcount
    print(vcount+1, '=>', fpath)
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in textext:
                print('Scipping', fpath)
            elif searchkey in open(fpath).read():
                #input('{0} has {1}'.format(fpath, searchkey))
                print('{0} has {1}'.format(fpath, searchkey))
                fcount += 1
    except Exception:
        print('Failed:', fpath, sys.exc_info()[0])
    vcount += 1


if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print('Found in {0} files, visited {1}'.format(fcount, vcount))
