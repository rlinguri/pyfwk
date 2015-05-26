#!/usr/bin/env python

"""
  dbcol.py: DBCol is a struct describing an sqlite database table column
"""

from dbcol import *


# -----------------------------DATABASE-ROW-------------------------------#
class DBRow:
    @staticmethod
    def dict(columns, values):
        if (values is not None):
            if (len(columns) == len(values)):
                dict = {}
                i = 0
                for col in columns:
                    dict[col.name] = values[i]
                    i += 1
                return dict
            else:
                raise ValueError('columns do not match values')
        else:
            return None

    @staticmethod
    def sqlForRowInsert(table, columns, values):
        c = len(columns)
        v = len(values)
        sql = 'INSERT INTO "{}" ('.format(table)
        i = 1
        for col in columns:
            sql += '"{}"'.format(col.name)
            if (i < c):
                sql += ','
            i += 1
        sql += ') VALUES ('
        i = 1
        # allow for first column autoincrement
        if (v == (c - 1)):
            sql += 'NULL,'
            i += 1
        for val in values:
            if (isinstance(val, int)):
                # don't need quotes in integer values
                sql += str(val)
            elif (val == 'NULL'):
                # keep quotes off of NULL
                sql += val
            else:
                # wrap value with quotes
                sql += '"{}"'.format(val)
            if (i < v):
                sql += ','
            i += 1
        sql += ');'
        return sql

# ---------------------------------EXPORT---------------------------------#
__all__ = ['DBRow']


# ----------------------------------MAIN----------------------------------#
def main():
    f1 = DBCol('f1', 'INTEGER')
    f2 = DBCol('f2', 'TEXT')
    f3 = DBCol('f3', 'TEXT')
    cols = [f1, f2, f3]
    vals = [1, 'Test', 'Third']
    print DBRow.dict(cols, vals)
    print DBRow.sqlForRowInsert('sample', cols, vals)


if __name__ == '__main__':
    main()
