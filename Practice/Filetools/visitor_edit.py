"""
Automatically opens files containing specific string by using system text editor
(notepad.exe - for Windows, vim - for *nix)

Usage:
> python visitor_edit.py string [directory]

default directory = '.'
"""

import sys
import os
from visitor import SearchVisitor


class EditVisitor(SearchVisitor):
    editor = 'notepad.exe' if sys.platform.startswith('win') else 'vim'

    def visitmatch(self, fname, text):
        os.system('{0} {1}'.format(self.editor, fname))      # Runs the editor - holds the main process. When
                                                             # the editor will be closed the main process will continue


if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print('Edited {0} files, visited {1}'.format(visitor.scount, visitor.fcount))

