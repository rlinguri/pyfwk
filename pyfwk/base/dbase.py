#!/usr/bin/env python

"""
  dbase.py: instance methods for extending database classes
"""


# ----------------------ABSTRACT-BASE-CLASS-DATABASE----------------------#
class DBase:
    """
      import sqlite3 module in extended module
      Vars curs and conn should be declared in extended class
      Values for both should be set at extended class __init__
    """
    def execute(self, sql, *args):
        self.curs.execute(sql, args)
        self.conn.commit()

    def insert(self, sql, *args):
        self.curs.execute(sql, args)
        self.conn.commit()
        return self.curs.lastrowid

    def fetchrec(self, sql, *args):
        self.curs.execute(sql, args)
        return self.curs.fetchone()

    def fetchrecs(self, sql, *args):
        self.curs.execute(sql, args)
        return self.curs.fetchall()


# ---------------------------------EXPORT---------------------------------#
__all__ = ['DBase']


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
