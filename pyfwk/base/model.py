#!/usr/bin/env python

"""
  object.py: instance methods for extending model objects
"""
import os
from object import *
from ..struc.dbrow import *


# ---------------------ABSTRACT-BASE-CLASS-DATA-MODEL---------------------#
class Model(Object):
    '''
      Vars dbase, table, columns should be declared in extended class
      Values for dbase, table and columns should be set at class __init__()
    '''

    def getRecFromId(self, id):
        sql = 'SELECT * FROM "{}" WHERE id = ?'.format(self.table)
        values = self.dbase.fetchRec(sql, id)
        if (values is not None):
            return DBRow.dict(self.columns, values)
        else:
            return None

    def getRecFromSymbol(self, symbol):
        sql = 'SELECT * FROM "{}" WHERE symbol = ?'.format(self.table)
        values = self.dbase.fetchRec(sql, symbol)
        return DBRow.dict(self.columns, values)

    def getRecsFromSymbol(self, symbol):
        lst = []
        sql = 'SELECT * FROM "{}" WHERE symbol = ?'.format(self.table)
        for values in self.dbase.fetchRecs(sql, symbol):
            row = DBRow.dict(self.columns, values)
            lst.append(row)
        return lst

    def getAllRecs(self):
        lst = []
        sql = 'SELECT * FROM "{}"'.format(self.table)
        for values in self.dbase.fetchRecs(sql):
            row = DBRow.dict(self.columns, values)
            lst.append(row)
        return lst

    def createTable(self):
        c = len(self.columns)
        i = 1
        sql = 'CREATE TABLE IF NOT EXISTS "{}" ('.format(self.table)
        for col in self.columns:
            sql += '"{}" {}'.format(col.name, col.datatype)
            if (i < c):
                sql += ', '
            i += 1
        sql += ');'
        print sql
        self.dbase.execute(sql)

    def dropTable(self):
        sql = 'DROP TABLE "{}";'.format(self.table)
        self.dbase.execute(sql)

    def importCSV(self):
        fms = FileManager.default(FileManager())
        pth = os.path.join(fms.csvDir(), '{}.csv'.format(self.table))
        fil = open(pth, 'r')
        for line in fil.readlines():
            lst = line.rstrip().split(',')
            sql = DBRow.sqlForRowInsert(self.table, self.columns, lst)
            self.dbase.execute(sql)
            print sql

    def createIndex(self, column):
        idx = column[0]
        sql = 'CREATE INDEX IF NOT EXISTS {}x ON "{}" ({});'.format(idx, self.table, column)
        self.dbase.execute(sql)

# ---------------------------------EXPORT---------------------------------#
__all__ = ['Model']


# ----------------------------------MAIN----------------------------------#
def main():
    mdl = Model()
    print mdl.name()
    print mdl.alloc()


if __name__ == '__main__':
    main()
