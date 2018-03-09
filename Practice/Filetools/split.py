"""
Split specific file into several parts. Use join.py script to combine parts into one file.

Usage:
> python split.py [file-to-split target-dir [chunksize]]
file-to-split - initial file
target-dir - directory where parts of initial file will be saved
chunksize - maximum size of parts in bytes (default: 1.4 Mb)
"""


import os
import sys


kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)


def split(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir, fname))
    partnum = 0
    inputfile = open(fromfile, 'rb')

    while True:
        chunk = inputfile.read(chunksize)
        if not chunk: break
        partnum += 1
        filename = os.path.join(todir, 'part{0:04}'.format(partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    inputfile.close()
    assert partnum <= 9999
    return partnum


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split: ')
            todir = input('Directory to store parts of file: ')
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]
            if len(sys.argv) == 4:
                try:
                    chunksize = int(sys.argv[3])
                except Exception:
                    print('chunksize argument must be int:')
                    print(sys.exc_info()[0], sys.exc_info()[1])
                    sys.exit(1)
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print('Splitting {0} to {1} by {2}'.format(absfrom, absto, chunksize))

        try:
            parts = split(fromfile, todir, chunksize)
        except Exception:
            print('Error during split:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Split finished: {0} parts are in {1}'.format(parts, absto))
        if interactive:
            input('Press <Enter> to exit')
