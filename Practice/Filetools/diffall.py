"""
Compares two directories and it's subdirectories to find differences. Also compares content of files
with identical names to be sure these files identical.

Usage:
> python difall.py dir1 dir2

Output example:
--------------------
Comparing G:\eclipse-workspace\Tests\Dir1 to G:\eclipse-workspace\Tests\Dir2
Files unique to G:\eclipse-workspace\Tests\Dir2
... File1.pdf
Comparing contents
text.txt matches
.pydevproject matches
2.py matches
3.py DIFFERS
--------------------
Comparing G:\eclipse-workspace\Tests\Dir1\Subdir1\ to G:\eclipse-workspace\Tests\Dir2\Subdir2
Directory lists are identical
Comparing contents
--------------------
Diffs found: 2
- unique files at G:\eclipse-workspace\Tests\Dir1 - G:\eclipse-workspace\Tests\Dir2
- files differ at G:\eclipse-workspace\Tests\Dir1\3.py - G:\eclipse-workspace\Tests\Dir2\3.py
"""


import os
import dirdiff


blocksize = 1024 * 1024


def intersect(seq1, seq2):
    return [item for item in seq1 if item in seq2]


def comparetrees(dir1, dir2, diffs, verbose=False):
    print('-' * 20)
    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)
    if not dirdiff.comparedirs(dir1, dir2, names1, names2):
        diffs.append('unique files at {0} - {1}'.format(dir1, dir2))
    print('Comparing contents')
    common = intersect(names1, names2)
    missed = common[:]

    for name in common:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if os.path.isfile(path1) and os.path.isfile(path2):
            missed.remove(name)
            file1 = open(path1, 'rb')
            file2 = open(path2, 'rb')
            while True:
                bytes1 = file1.read(blocksize)
                bytes2 = file2.read(blocksize)
                if (not bytes1) and (not bytes2):
                    if verbose:
                        print(name, 'matches')
                    break
                if bytes1 != bytes2:
                    print(name, 'DIFFERS')
                    diffs.append('files differ at {0} - {1}'.format(path1, path2))
                    break

    for name in common:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if os.path.isdir(path1) and os.path.isdir(path2):
            missed.remove(name)
            comparetrees(path1, path2, diffs, verbose)

    for name in missed:
        diffs.append('files missed at {0} - {1}: {2}'.format(dir1, dir2, name))
        print(name, 'DIFFERS (miss)')


if __name__ == '__main__':
    dir1, dir2 = dirdiff.getargs()
    diffs = []
    comparetrees(dir1, dir2, diffs, True)
    print('=' * 20)
    if not diffs:
        print('No diffs found')
    else:
        print('Diffs found:', len(diffs))
        for diff in diffs:
            print('-', diff)

