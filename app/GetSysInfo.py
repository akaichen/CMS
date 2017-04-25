# -*- coding: utf-8 -*-

import datetime

class GetSysInfo:
    def __init__(self, membertype):
        self.membertype = membertype

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

    def GetCustomerHeaderList(self, gettype):
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

            if self.membertype in ['Member', 'All']:
                CustomerHeaderId[0] = 100
                CustomerHeaderId[1] = 70
                CustomerHeaderId[2] = 100
                CustomerHeaderId[6] = 130
                CustomerHeaderId[7] = 130
                CustomerHeaderId[8] = 100
            elif self.membertype == 'Nonmember':
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
                      u'副理', u'經理', u'松柏',
                      u'長青', u'珍珠', u'翡翠',
                      u'藍鑽']

        joblist = [u'請選擇'] + alljoblist
        queryjoblist = [u'選擇顯示職級'] + alljoblist

        return joblist, queryjoblist

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

