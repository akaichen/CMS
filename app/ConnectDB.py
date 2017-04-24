import os, sys
import string, re
import pyodbc

class ConnectDB():
    def __init__(self, dbname, dbaction, sqlcmd):
        #print 'init'
        self.dbname = dbname
        self.dbaction = dbaction
        self.sqlcmd = sqlcmd
        #print self.dbname

    def ConnectDB(self):
        #print 'con'
        #print self.dbname
        self.conn = ''
        s = 1
        while 1:
            try:
                self.conn = pyodbc.connect(self.dbname)
                self.cur = self.conn.cursor()
                #print 'Connect successed'
                break
            except:
                msg = 'Connect failed: (%s)'%s
                #print msg
                return msg
            s+=1
            if s == 10:
                break

        sqlstr = ''
        if self.sqlcmd:
            try:
                self.cur.execute(self.sqlcmd)
            except:
                print 'Access database error  '
                print self.sqlcmd

            if self.dbaction == 'create' or self.dbaction == 'update' or self.dbaction == 'insert' or self.dbaction == 'delete':
                self.cur.commit()
            elif self.dbaction == 'select':
                info = self.cur.fetchall()
                if info:
                    sqlstr = info

        self.cur.close()
        self.conn.close()

        return sqlstr

