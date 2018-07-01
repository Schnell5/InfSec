import sys
import os

old_path = '#!/usr/bin/python'
new_path = '#!/usr/local/bin/python3'
extensions = ['.py']
init_dir = '.'
recursive = False
ch_dict = {}
if len(sys.argv) > 2:
    if sys.argv[1].lower() == '-r':
        recursive = True
    init_dir = sys.argv[2]
elif len(sys.argv) > 1:
    if sys.argv[1].lower() == '-r':
        recursive = True
    else:
        init_dir = sys.argv[1]

if not os.path.exists(os.path.abspath(init_dir)):
    print('[ERROR] No such directory:', os.path.abspath(init_dir))
    sys.exit(1)

print('Changing .py files in:', os.path.abspath(init_dir))

for (thisdir, subshere, fileshere) in os.walk(init_dir):
    if not recursive and thisdir != init_dir:
        break
    for file in fileshere:
        filepath = os.path.join(thisdir, file)
        if os.path.splitext(filepath)[1] in extensions:
            text = open(filepath, 'r').read()
            if old_path in text:
                new_text = text.replace(old_path, new_path)
                ch_dict[filepath] = new_text

if ch_dict:
    print('Changes will be done in the following files:')
    for (num, (path, text)) in enumerate(ch_dict.items()):
        print('{0:2}. {1}'.format(num+1, os.path.split(path)[1]))
    answer = input('Proceed? (Y/N) [N]: ')
    if answer and answer[0] in 'Yy':
        for (path, text) in ch_dict.items():
            file = open(path, 'w')
            file.write(text)
            file.close()
    else:
        print('Changes have been canceled')






