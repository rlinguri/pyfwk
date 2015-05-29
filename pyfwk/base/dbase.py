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

    def fetch_rec(self, sql, *args):
        self.curs.execute(sql, args)
        return self.curs.fetchone()

    def fetch_recs(self, sql, *args):
        self.curs.execute(sql, args)
        return self.curs.fetchall()

    def table_exists(self,table_name):
        sql = 'SELECT name FROM sqlite_master WHERE type = "table" AND name = "{}";'.format(table_name)
        res = self.fetch_rec(sql)
        if (res is not None):
            return True
        else:
            return False

# ---------------------------------EXPORT---------------------------------#
__all__ = ['DBase']


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
