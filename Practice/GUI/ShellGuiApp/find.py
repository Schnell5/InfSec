"""
Find files in specific directory and it's subdirectories by using Unix-based patterns to search

Usage:
> python find.py pattern startdir

Example:
> python find.py *.py .
"""


import os
import fnmatch


def find(pattren, startdir=os.curdir):
    for (thisdir, subshere, fileshere) in os.walk(startdir):
        for name in subshere + fileshere:
            if fnmatch.fnmatch(name, pattren):
                fpath = os.path.join(thisdir, name)
                yield fpath


def findlist(pattern, startdir=os.curdir, dosort=False):
    matches = list(find(pattern, startdir))
    if dosort:
        matches.sort()
    return matches


if __name__ == '__main__':
    import sys
    namepattern, statrdir = sys.argv[1], sys.argv[2]
    for name in find(namepattern, statrdir):
        print(name)
