"""
[*] Issue: Some files can't run successfully by web server on Unix/Linux
if these files were written on Windows (looks like there is some endline chars
representation issue). As result web server will return the error like this one:
"FileNotFoundError: [Errno 2] No such file or directory: <full_path_to_file>"
even if the directory actually exists.

[*] Solution: re-create such files on Unix/Linux and set the necessary permissions

[*] Usage: > python3 recreator.py [-r] <file_to_recreate>
    -r - replace original file
"""

import sys
import os

replace = False  # Replace flag


# Parse arguments
if len(sys.argv) == 3:
    if sys.argv[1].lower() == '-r':
        replace = True
    orig_file = sys.argv[2]
elif len(sys.argv) == 2:
    orig_file = sys.argv[1]
else:
    sys.exit(0)

# Make an absolute path to original file
orig_file_path = os.path.abspath(orig_file)
print('[*] Original file:', orig_file_path)

# Form new file name
if not replace:
    new_file_path = os.path.splitext(orig_file_path)[0] + '_new' + os.path.splitext(orig_file_path)[1]
else:
    new_file_path = orig_file_path
print('[*] New file:     ', new_file_path)

# Recreation (with optional permissions setting)
if input('Create? [Y/N]: ') in 'Yy':
    try:
        orig_text = open(orig_file_path, 'r').read()
        new_file = open(new_file_path, 'w')
        new_file.write(orig_text)
        new_file.close()
    except IsADirectoryError as err:
        print(err)
        sys.exit(1)
    if not sys.platform.startswith('win'):                  # If Unix/Linux
        if input('Set 755 permissions? [Y/N]: ') in 'Yy':
            os.system('chmod 755 {}'.format(new_file_path))
            print('Permissions 755 have been set')
        else:
            print('Permissions setting canceled')
else:
    print('Canceled')
    sys.exit(0)
