#!/usr/bin/env python

"""
  increment.py: some scripts require fetching of internet data or operations that
  could cause a drain on the system if they were to be executed sequentially.
  The Increment class provides methods for reading and writing ids to disc so that
  execution the scripts can be looped on incremental values.
"""

import os
from filemanager import *

# ----------------------------INCREMENT-UTILITY---------------------------#
class Increment:
    file = None
    pdir = None

    def __init__(self, module):
        """ sets the path to the increment file based on module """
        fms = FileManager.instance()
        self.pdir = fms.inc_dir()
        self.file = os.path.join(self.pdir, '{}.txt'.format(module))
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                f.write('1000')
                f.close()

    def current(self):
        """ return the current value without incrementing """
        f = open(self.file, "r")
        i = int(f.read())
        f.close()
        return i

    def next(self):
        """ return the current value and increment by 1 in the file """
        c = self.current()
        f = open(self.file, 'r+')
        f.seek(0)
        f.write(str(c + 1))
        f.close()
        return c

    def reset(self):
        f = open(self.file, 'r+')
        f.seek(0)
        f.write('1000')
        f.close()

# ---------------------------------EXPORT---------------------------------#
__all__ = ['Increment']


# ----------------------------------MAIN----------------------------------#
def main():
    inc = Increment('inc')
    print inc.next()


if __name__ == '__main__':
    main()
