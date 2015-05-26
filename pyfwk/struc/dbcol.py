#!/usr/bin/env python

"""
  dbcol.py: DBCol is a struct describing an sqlite database table column
"""


# ----------------------------DATABASE-COLUMN-----------------------------#
class DBCol:
    name = None
    datatype = None

    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype


# ---------------------------------EXPORT---------------------------------#
__all__ = ['DBCol']


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
