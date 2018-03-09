"""
Search for biggest files with specific extension in specific directory and it's subdirectories

Usage:
> python bigext-tree.py [dirname [ext [tracelvl]]]

dirname - name of base root directory (default: current directory from where scenario runs)
ext - extension in format .<extname> (default: .py)
tracelvl - trace level: 1 (default) - to print name of directory where search in;
                        2 - to print name of file which size is calculated

Example:
> python bigext-tree.py C:\Users .txt 2
"""


import os
import pprint
from sys import argv, exc_info


trace = 1
dirname, extname = os.curdir, '.py'
if len(argv) > 1:
    dirname = argv[1]
if len(argv) > 2:
    extname = argv[2]
if len(argv) > 3:
    trace = int(argv[3])


def tryprint(arg):
    try:
        print(arg)
    except UnicodeEncodeError:
        print(arg.encode())


visited = set()
allsizes = []
for (thisdir, subshere, fileshere) in os.walk(dirname):
    if trace: tryprint(thisdir)
    thisdir = os.path.normpath(thisdir)
    fixname = os.path.normcase(thisdir)
    if fixname in visited:
        if trace: tryprint('skipping ' + thisdir)
    else:
        visited.add(fixname)
        for filename in fileshere:
            if filename.endswith(extname):
                if trace > 1: tryprint('+++' + filename)
                fullname = os.path.join(thisdir, filename)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allsizes.append((bytesize, linesize, fullname))

for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy {}'.format(title))
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
