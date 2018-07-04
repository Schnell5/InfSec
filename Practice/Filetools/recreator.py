"""
[*] Issue: Some files can't run successfully by web server on Unix/Linux
if these files were written on Windows (looks like there is some endline chars
representation issue). As result web server will return the error like this one:
"FileNotFoundError: [Errno 2] No such file or directory: <full_path_to_file>"
even if the directory actually exists.

[*] Solution: re-create such files on Unix/Linux and set the necessary permissions

[*] Usage: > python3 recreator.py <file_to_recreate> """

import sys
import os

orig_file = sys.argv[1]
orig_file_path = os.path.abspath(orig_file)
print('[*] Original file:', orig_file_path)
path = os.path.split(orig_file_path)[0]
savedir = os.path.curdir
new_file_path = os.path.splitext(orig_file_path)[0] + '_new' + os.path.splitext(orig_file_path)[1]
print('[*] New file:', new_file_path)
if input('Create? [Y/N]: ') in 'Yy':
    new_file = open(new_file_path, 'w')
    new_file.write(open(orig_file_path, 'r').read())
    new_file.close()
    if input('Set 755 permissions? [Y/N]: ') in 'Yy':
        os.system('chmod 755 {}'.format(new_file_path))
        print('Permissions 755 was set')
    else:
        print('Permissions setting was canceled')
else:
    print('Canceled')
    sys.exit(0)
