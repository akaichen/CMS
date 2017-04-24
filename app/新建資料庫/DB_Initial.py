import os, sys
import string, re
import time
import codecs
import ConnectDB

class DBInitial:
    def __init__(self):
        self.dbfilename = 'customerinfo.mdb'
        self.sysinifile = 'systemsetup.ini'
        self.dbcreate = 'create'
        self.dbinsert = 'insert'
        self.dbupdate = 'update'
        self.dbselect = 'select'
        self.logfile = 'DB_initial.log'
        self.createdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def Start(self):
        driver = self.GetDriver()
        if not os.path.isfile(self.dbfilename):
            self.writelog = open(self.logfile, 'w')
            self.dbname = 'DRIVER={%s};DBQ=%s;ExtendedAnsiSQL=1'%(driver, self.dbfilename)
            ### Create tables
            errmsg = []
            dblist = self.GetTablename()
            print dblist
            exit(0)
            errmsg = self.CreateTable(dblist, errmsg)
            ### Create system administrator account
            showmsg = ''
            errmsg = self.CreateSysadmin(dblist, errmsg)
            if not errmsg:
                self.writelog.write('Database initialized finished')
            else:
                for err in errmsg:
                    self.writelog.write(err)
                    showmsg += '%s!\n'
            self.writelog.close()
    
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
                break

        return dbfilename

    def GetTablename(self):
        chk = 0
        dblist = {}
        rfile = open(self.sysinifile,'r').readlines()
        for line in rfile:
            if re.compile(r'^\[TABLES').findall(line):
                chk = 1
                continue

            if chk == 1:
                if line == '\n':
                    chk = 0
                    break
                tablename = string.split(line)[2]
                defaultid = self.GetDefaultID(tablename)
                if tablename not in dblist.keys():
                    dblist[tablename] = ''
                dblist[tablename] = defaultid

        return dblist

    def GetDefaultID(self, tablename):
        defaultid = ''

        rfile = open(self.sysinifile,'r').readlines()
        for line in rfile:
            if re.compile(r'^%s_IDFormat'%tablename).findall(line):
                defaultid = string.split(line)[2]
                break

        return defaultid

    def CreateTable(self, dblist, errmsg):
        ### Create Table
        for tablename in dblist.keys():
            table_types = self.GetTablesTypes(tablename)
            errmsg = self.CreateTableSchema(tablename, table_types, errmsg)

        ### Insert Table Schema into SysParameter
        for tablename in dblist.keys():
            def_types = self.GetDefaultTypes(tablename)
            table_types = self.GetTablesTypes(tablename)
            if def_types:
                errmsg = self.CreateDefaultSchema(tablename, def_types, table_types, errmsg)

        return errmsg

    def GetDefaultTypes(self, tablename):
        chk = 0
        def_types = {}
        rfile = open(self.sysinifile,'r').readlines()
        for line in rfile:
            if re.compile(r'^\[DEFAULT_TYPES').findall(line):
                chk = 1
                continue

            if chk == 1:
                if line == '\n':
                    chk = 0
                    break
                if re.compile(r'%s_'%tablename).findall(line):
                    param = string.split(string.split(line)[0], '_')[1]
                    value = string.split(line)[2]
                    if param not in def_types.keys():
                        def_types[param] = ''
                        def_types[param] = value

        return def_types

    def CreateDefaultSchema(self, tablename, def_types, table_types, errmsg):
        activeid = 0
        for param in def_types.keys():
            value = def_types[param]
            vid = 0
            for val1 in string.split(value, ','):
                schemalist = '''INSERT INTO SysParameter (Parameter, PValue, PName, PActive)
                                                  VALUES ('%s', %s, '%s', %s)
                            '''%(param, vid, val1, activeid)
                vid += 1
                errmsg = self.DoCreateTable(tablename, self.dbinsert, schemalist, errmsg)

        vidlist = table_types.keys()
        vidlist.sort()
        for vid in vidlist:
            for param in table_types[vid].keys():
                colinfo = table_types[vid][param]['CNAME']
                types = table_types[vid][param]['TYPES']
                p_key = table_types[vid][param]['P_KEY']

                schemalist = '''INSERT INTO SysParameter (Parameter, PValue, PName, PActive)
                                                  VALUES ('%s', '%s', '%s', '%s')
                            '''%(param, vid, colinfo, activeid)
                errmsg = self.DoCreateTable(tablename, self.dbinsert, schemalist, errmsg)

        return

    def GetTablesTypes(self, tablename):
        chk = 0
        table_types = {}
        rfile = open(self.sysinifile,'r').readlines()
        tid = 0
        for line in rfile:
            if re.compile(r'^\[%s'%tablename).findall(line):
                chk = 1
                continue
            if chk == 1:
                if line == '\n':
                    chk = 0
                    break
                param = string.split(line)[0]
                value = string.split(line)[2]
                types = string.split(line)[3]
                p_key = string.split(line)[4]
                if tid not in table_types.keys():
                    table_types[tid] = {}
                if param not in table_types[tid].keys():
                    table_types[tid][param] = {}
                table_types[tid][param]['CNAME'] = value
                table_types[tid][param]['TYPES'] = types
                table_types[tid][param]['P_KEY'] = p_key
                tid += 1

        return table_types

    def CreateTableSchema(self, tablename, table_types, errmsg):
        p_string = ', PRIMARY KEY ('
        schemalist = 'CREATE TABLE %s ('%tablename

        idlist = table_types.keys()
        idlist.sort()
        pid = 0
        for id in idlist:
            for param in table_types[id].keys():
                colname = string.split(param, '_')[1]
                colinfo = table_types[id][param]['CNAME']
                types = table_types[id][param]['TYPES']
                p_key = table_types[id][param]['P_KEY']
                if p_key == 'YES':
                    if pid == 0:
                        p_string += '%s'%colname
                    else:
                        p_string += ', %s'%colname
                    pid += 1
                if id == 0:
                    schemalist += '%s %s'%(colname, types)
                else:
                    schemalist += ', %s %s'%(colname, types)
        schemalist += '%s))'%p_string
        errmsg = self.DoCreateTable(tablename, self.dbcreate, schemalist, errmsg)

        return errmsg

    def DoCreateTable(self, tablename, dbaction, schemalist, errmsg):
        #print schemalist
        db = ConnectDB.ConnectDB(self.dbname, dbaction, schemalist)
        info = db.ConnectDB()
        if info:
            errmsg.append('%s table %s error'%(dbaction, tablename))

        return errmsg

    def CreateSysadmin(self, dblist, errmsg):
        ###
        ### Status: 0 = Enable, 1 = Disable
        ### Sex: 0 = Male, 1 = Female
        ###

        for tablename in dblist.keys():
            loopid = 0
            defaultid = dblist[tablename]
            if defaultid == '':
                continue

            if re.compile(r'Cust').search(tablename):
                ### Create Default Customer Account
                schemalist = '''INSERT INTO %s (CustNo, CustType, CustName, CustSex, CustStatus, CustCount, CustCreateDate)
                                        VALUES ('%s', 0, 'System Administrator', 0, 0, '0', '%s')
                             '''%(tablename, defaultid, self.createdate)

            elif re.compile(r'Emp').search(tablename):
                ### Create System Administrator Account
                schemalist = '''INSERT INTO %s (EmpNO, EmpName, EmpPasswd, EmpJobTitle, EmpSex,
                                                EmpStatus, EmpType, EmpEmail, EmpCreateDate)
                                        VALUES ('%s', 'admin', 'sunplusit', 0, 0,
                                                 0, 0, 'kasler67911@yahoo.com.tw', '%s')
                             '''%(tablename, defaultid, self.createdate)
            elif re.compile(r'Vendor').search(tablename):
                ### Create Default Vendor Account
                schemalist = '''INSERT INTO %s (VendorNO, VendorName, VendorType, VendorStatus, VendorCreateDate)
                                        VALUES ('%s', 'System Administrator', 0, 0, '%s')
                             '''%(tablename, defaultid, self.createdate)
            elif re.compile(r'Rooms').search(tablename):
                loopid = 1
                ### Create Default Room Info
                roombedlist = ['A', 'B']
                for roomname in string.split(defaultid, ','):
                    if len(roomname) == 4:
                        roomno   = roomname[0:3]
                        roombed  = roombedlist.index(roomname[3])
                        roomtype = 1
                    elif len(roomname) == 3:
                        roomno   = roomname[0:3]
                        roombed  = 0
                        roomtype = 0
                    else:
                        continue
                    schemalist = '''INSERT INTO %s (RoomNo, RoomType, RoomName, RoomBedNo, RoomUsage, RoomTotal)
                                            VALUES ('%s', %s, '%s', %s, '0', '0')
                                  '''%(tablename, roomno, roomtype, roomname, roombed)
                    errmsg = self.DoCreateTable(tablename, self.dbinsert, schemalist, errmsg)

            if loopid == 0:
                errmsg = self.DoCreateTable(tablename, self.dbinsert, schemalist, errmsg)

        return errmsg

if __name__ == '__main__':
    app = DBInitial()
    app.Start()
