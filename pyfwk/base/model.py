#!/usr/bin/env python

"""
  object.py: instance methods for extending model objects
"""
import os
from object import *
from ..struc.dbrow import *
from ..utils.filemanager import *


# ---------------------ABSTRACT-BASE-CLASS-DATA-MODEL---------------------#
class Model(Object):
    '''
      Vars dbase, table, columns should be declared in extended class
      Values for dbase, table and columns should be set at class __init__()
    '''

    def get_rec_from_id(self, id):
        sql = 'SELECT * FROM "{}" WHERE id = ?'.format(self.table)
        values = self.dbase.fetch_rec(sql, id)
        if (values is not None):
            return DBRow.dict(self.columns, values)
        else:
            return None

    def get_rec_from_entity_id(self, entity_id):
        sql = 'SELECT * FROM "{}" WHERE entity = ?'.format(self.table)
        values = self.dbase.fetch_rec(sql, entity_id)
        return DBRow.dict(self.columns, values)

    def get_rec_from_symbol(self, symbol):
        sql = 'SELECT * FROM "{}" WHERE symbol = ?'.format(self.table)
        values = self.dbase.fetch_rec(sql, symbol)
        return DBRow.dict(self.columns, values)

    def get_recs_from_symbol(self, symbol):
        lst = []
        sql = 'SELECT * FROM "{}" WHERE symbol = ?'.format(self.table)
        for values in self.dbase.fetch_recs(sql, symbol):
            row = DBRow.dict(self.columns, values)
            lst.append(row)
        return lst

    def get_all_recs(self):
        lst = []
        sql = 'SELECT * FROM "{}"'.format(self.table)
        for values in self.dbase.fetch_recs(sql):
            row = DBRow.dict(self.columns, values)
            lst.append(row)
        return lst

    def create_table(self):
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

    def drop_table(self):
        sql = 'DROP TABLE "{}";'.format(self.table)
        self.dbase.execute(sql)

    def import_csv(self):
        fms = FileManager.instance()
        pth = os.path.join(fms.csv_dir(), '{}.csv'.format(self.table))
        fil = open(pth, 'r')
        for line in fil.readlines():
            lst = line.rstrip().split(',')
            sql = DBRow.sqlForRowInsert(self.table, self.columns, lst)
            self.dbase.execute(sql)
            print sql

    def create_index(self, column):
        idx = column[0]
        sql = 'CREATE INDEX IF NOT EXISTS {}x ON "{}" ({});'.format(idx, self.table, column)
        self.dbase.execute(sql)

    def validate(self):
        if (self.dbase.table_exists(self.table) is False):
            fm = FileManager.instance()
            if fm.get_csv(self.table) is not None:
                self.create_table()
                self.import_csv()
                self.create_index('type')
                self.create_index('exchange')
                self.create_index('profile')

# ---------------------------------EXPORT---------------------------------#
__all__ = ['Model']


# ----------------------------------MAIN----------------------------------#
def main():
    mdl = Model()
    print mdl.name()
    print mdl.alloc()


if __name__ == '__main__':
    main()
