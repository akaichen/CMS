# -*- coding: utf-8 -*-

import datetime

import ConnectDB

class GetSysInfo:
    def __init__(self):
        pass

    def GetPurchseHeaderList(self):
        PurchseHeaderList = [u'購買月份', u'月積分',
                             u'月累加總積分']

        PurchseHeaderId = {}
        PurchseHeaderId[0] = 100
        PurchseHeaderId[1] = 100
        PurchseHeaderId[2] = 120

        return PurchseHeaderList, PurchseHeaderId

    def GetProductHeaderList(self):
        ProductHeaderList = [u'產品編號', u'產品名稱',
                             u'產品規格', u'建議售價',
                             u'實際售價']

        ProductHeaderId    = {}
        ProductHeaderId[0] = 100
        ProductHeaderId[1] = 200
        ProductHeaderId[2] = 180
        ProductHeaderId[3] = 80
        ProductHeaderId[4] = 80

        return ProductHeaderList, ProductHeaderId

    def GetContentHeaderList(self):
        ContentHeaderList = [u'時間', u'類別',
                             u'姓名', u'內容']

        ContentHeaderId    = {}
        ContentHeaderId[0] = 100
        ContentHeaderId[1] = 100
        ContentHeaderId[2] = 100
        ContentHeaderId[3] = 600

        return ContentHeaderList, ContentHeaderId

    def GetCustomerHeaderList(self, membertype, gettype):
        CustomerHeaderList = []
        CustomerHeaderId = {}
        if gettype == 'customer':
            CustomerHeaderList = [u'經銷商編號', u'職級',
                          u'姓名', u'配偶', 
                          u'生日', u'職業',
                          u'電話[H,O]', u'行動電話',
                          u'地區', u'地址',
                          u'e-Mail', u'推薦人']
            # 職級(上聘年月)

            if membertype in ['Member', 'All']:
                CustomerHeaderId[0] = 100
                CustomerHeaderId[1] = 70
                CustomerHeaderId[2] = 100
                CustomerHeaderId[6] = 130
                CustomerHeaderId[7] = 130
                CustomerHeaderId[8] = 100
            elif membertype == 'Nonmember':
                CustomerHeaderId[2] = 100
                CustomerHeaderId[6] = 130
                CustomerHeaderId[7] = 130
                CustomerHeaderId[8] = 100
        elif gettype == 'purchse':
            CustomerHeaderList = [u'經銷商編號', u'職級',
                                  u'姓名', u'配偶',
                                  u'生日', u'職業',
                                  u'電話[H,O]', u'行動電話',
                                  u'地區', u'地址',
                                  u'e-Mail', u'推薦人']
            CustomerHeaderId[0] = 100
            CustomerHeaderId[1] = 70
            CustomerHeaderId[2] = 100
            CustomerHeaderId[6] = 130
            CustomerHeaderId[7] = 130
            CustomerHeaderId[8] = 100

        return CustomerHeaderList, CustomerHeaderId

    def GetJobLevelList(self):
        alljoblist = [u'會員', u'主任', 
                      u'副理', u'經理', 
                      u'松柏', u'長青', 
                      u'珍珠', u'翡翠', 
                      u'藍鑽']

        joblist = [u'請選擇'] + alljoblist
        queryjoblist = [u'選擇顯示職級'] + alljoblist

        return joblist, queryjoblist

    def GetQueryContentList(self):
        allconlist = [u'HP', u'NDS', 
                      u'春訓', u'表揚會', 
                      u'組織活動', u'平日作業']

        conlist = [u'請選擇'] + allconlist
        queryconlist = [u'選擇顯示類別'] + allconlist

        return conlist, queryconlist

    def GetDateList(self):
        currentTime = datetime.datetime.now()
        thisyear = int(currentTime.strftime("%Y"))
        firstyear = thisyear - 100
        
        yearlist = [u'請選擇']
        for yearname in range(thisyear, firstyear, -1):
            yearlist.append('%s'%yearname)

        monthlist = [u'請選擇']
        for monthname in range(1, 13):
            monthlist.append('%s'%monthname)

        daylist = [u'請選擇']
        for dayname in range(1, 32):
            daylist.append('%s'%dayname)

        return yearlist, monthlist, daylist

    def GetBackupTypeList(self):
        backuptype = [u'請選擇備份方式', u'本機磁碟']
        #[,
        #              u'Google Drive', u'One Drive',
        #              u'Dropbox']

        return backuptype

    def GetBackupHeaderList(self):
        HeaderList = [u'備份型態', u'備份時間',
                      u'檔案名稱', u'檔案大小',
                      u'備註']
        HeaderId    = {}
        HeaderId[0] = 120
        HeaderId[1] = 150
        HeaderId[2] = 400
        HeaderId[3] = 100
        HeaderId[4] = 150

        return HeaderList, HeaderId

    def GetAllUserInfo(self, dbname, membertype, custtable, queryjoblist, searchname):
        alluserinfo = []
        sqlaction = 'select'
        if membertype == '':
            if searchname == '':
                sqlcmd = '''SELECT Customer_Name FROM %s
                        '''%(custtable)
        else:
            if searchname in range(0, len(queryjoblist)):
                searchname = queryjoblist[searchname]
                sqlcmd = '''SELECT * FROM %s
                            WHERE Customer_SaleType = '%s' AND Customer_JobLevel = '%s'
                        '''%(custtable, membertype, searchname)
            elif searchname == '':
                sqlcmd = '''SELECT * FROM %s
                            WHERE Customer_SaleType = '%s'
                        '''%(custtable, membertype)
            else:
                sqlcmd = '''SELECT * FROM %s
                            WHERE Customer_SaleType = '%s' AND (
                                    Customer_Name LIKE '%s' OR Customer_JobTitle LIKE '%s'
                                    OR Customer_Telephone LIKE '%s' OR Customer_Cellphone LIKE '%s'
                                    OR Customer_Area LIKE '%s' OR Customer_JobLevel LIKE '%s' )
                        '''%(custtable, membertype,
                             '%'+searchname+'%', '%'+searchname+'%', '%'+searchname+'%',
                             '%'+searchname+'%', '%'+searchname+'%', '%'+searchname+'%')

        try:
            db = ConnectDB.ConnectDB(dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
            alluserinfo = info
            #print 'Query user info:  '
            #print alluserinfo
        except:
            print 'Access database error %s'%sqlacion
            print sqlcmd
            info = 'error'
        
        return alluserinfo

    def GetAllProductInfo(self, dbname, prodtable):
        allprodinfo = []
        sqlaction = 'select'
        sqlcmd = '''SELECT * FROM %s
                '''%(prodtable)

        try:
            db = ConnectDB.ConnectDB(dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
            allprodinfo = info
            #print 'Query user info:  '
            #print allprodinfo
        except:
            print 'Access database error %s'%sqlacion
            print sqlcmd
            info = 'error'
        
        return allprodinfo

    def GetAllFollowInfo(self, dbname, followtable, searchname):
        allfollowinfo = []
        sqlaction = 'select'
        if searchname == '':
            sqlcmd = '''SELECT * FROM %s
                        '''%(followtable)
        else:
            sqlcmd = '''SELECT * FROM %s
                        WHERE Follow_Category = '%s'
                        '''%(followtable, searchname)

        try:
            db = ConnectDB.ConnectDB(dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
            allfollowinfo = info
            #print 'Query user info:  '
            #print alluserinfo
        except:
            print 'Access database error %s'%sqlacion
            print sqlcmd
            info = 'error'
        
        return allfollowinfo


