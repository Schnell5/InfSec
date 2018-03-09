"""
Combine the parts that were created by the split.py script into one file

Usage:
> python join.py [from-dir-name to-file-name]
from-dir-name - directory where parts of file are in
to-file-name - name of file to be created after combining the parts
"""


import sys
import os


readsize = 1024


def join(fromdir, tofile):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj = open(filepath, 'rb')
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close()
    output.close()


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: join.py [from-dir-name to-file-name]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files: ')
            tofile = input('Name of file to be recreated: ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        print('Joining {0} to make {1}'.format(absfrom, absto))

        try:
            join(fromdir, tofile)
        except Exception:
            print('Error joining files:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Job complete: see', absto)
        if interactive:
            input('Press <Enter> to exit')
