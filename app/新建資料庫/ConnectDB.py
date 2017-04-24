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

class GetSysInfo():
    def __init__(self):
        self.sysinifile = 'systemsetup.ini'

    def GetDriver(self):
        import pyodbc
        drivers = pyodbc.drivers()
        mdb_driver = [d for d in drivers if 'Microsoft Access Driver (*.mdb' in d]

        return mdb_driver[0]
        
    def GetDBFileName(self):
        rfile = open(self.sysinifile,'r').readlines()
        for line in rfile:
            pat2 = re.compile(r'dbname = ')
            if pat2.findall(line):
                dbfilename = string.split(line)[2]

        return dbfilename

    def GetTablename(self):
        EmpTablename = ''
        CustTablename = ''
        VendorTablename = ''
        SystemTablename = ''

        rfile = open(self.sysinifile,'r').readlines()
        for line in rfile:
            if re.compile(r'^EmpTablename').findall(line):
                EmpTablename = string.split(line)[2]
            elif re.compile(r'^CustTablename').findall(line):
                CustTablename = string.split(line)[2]
            elif re.compile(r'^VendorTablename').findall(line):
                VendorTablename = string.split(line)[2]
            elif re.compile(r'^SystemTablename').findall(line):
                SystemTablename = string.split(line)[2]

        return EmpTablename, CustTablename, VendorTablename, SystemTablename
      
if __name__ == "__main__":
    sysinfo = GetSysInfo()
    driver = sysinfo.GetDriver()
    dbfilename = sysinfo.GetDBFileName()
    if os.path.isfile(dbfilename):
        #dbname = DRIVER={Microsoft Access Driver (*.mdb)};DBQ=F:\akai\python\crm\main\customer.mdb;ExtendedAnsiSQL=1;
        dbname = 'DRIVER={%s};DBQ=%s;ExtendedAnsiSQL=1;'%(driver, dbfilename)
        dbaction = 'select'
        sysparam = 'CustType'
        sqlcmd = '''SELECT PValue, PName
                    FROM SysParameter
                    WHERE Parameter = '%s'
                    ORDER BY PValue
                    '''%sysparam
        print sqlcmd
        Con_DB = ConnectDB(dbname, dbaction, sqlcmd)
        cur = Con_DB.ConnectDB()
        print cur

    sys.exit(0)