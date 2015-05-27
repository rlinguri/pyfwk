#!/usr/bin/env python

"""
  filemanager.py: provides methods for accessing project directories
"""

import os

# --------------------------FILE-MANAGER-UTILITY--------------------------#
class FileManager:
    fms = None
    root = None
    """
      first static call of this class must include project root path
      as the first argument. Therafter, static calls will return the
      instance containing the path.
    """

    @staticmethod
    def instance():
        if not FileManager.fms:
            FileManager.fms = FileManager()
        return FileManager.fms

    def __init__(self):
        pass

    def set_root(self, arg):
        self.fms.root = arg

    def root_dir(self):
        return self.root

    def inc_dir(self):
        """ calling this method will create ./var/inc directory structure """
        par = os.path.join(self.root, "var", "inc")
        if not os.path.exists(par):
            os.makedirs(par)
        return par

    def db_dir(self):
        """ calling this method will create ./var/db directory structure """
        par = os.path.join(self.root, "var", "db")
        if not os.path.exists(par):
            os.makedirs(par)
        return par

    def dir_for_symbol(self, symbol):
        """ calling this method will create ./etc/sym/x/xxx directory structure """
        dir = symbol.lower()
        ltr = dir[0]
        par = os.path.join(self.root, "etc", "sym", ltr, dir)
        if not os.path.exists(par):
            os.makedirs(par)
        return par

    def csv_dir(self):
        """ calling this method will create ./etc/csv directory structure """
        par = os.path.join(self.root, "etc", "csv")
        if not os.path.exists(par):
            os.makedirs(par)
        return par

# ---------------------------------EXPORT---------------------------------#
__all__ = ['FileManager']


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
