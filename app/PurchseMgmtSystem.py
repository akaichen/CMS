# -*- coding: utf-8 -*-
#Boa:Dialog:PurchseMgmtSystem

import wx
import wx.lib.buttons

import GetSysInfo
import ConnectDB
import PurchseProduct

def create(parent):
    return PurchseMgmtSystem(parent)

[wxID_PURCHSEMGMTSYSTEM, wxID_PURCHSEMGMTSYSTEMEXITBUTTON, 
 wxID_PURCHSEMGMTSYSTEMCUSTLIST, wxID_PURCHSEMGMTSYSTEMPANEL1,
 wxID_BITMAPCMSMAINPAGE, wxID_CMSMAINDIALOGWARNINGTEXT,
 wxID_PURCHSEMGMTSYSTEMPURCHSEPRODUCT, wxID_PURCHSEMGMTSYSTEMPURCHSEPOINT,
 wxID_PURCHSEMGMTSYSTEMPURCHSELIST, 
] = [wx.NewId() for _init_ctrls in range(9)]

class PurchseMgmtSystem(wx.Dialog):
    def _init_ctrls(self, prnt, purchsetitle):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PURCHSEMGMTSYSTEM,
              name='PURCHSEMgmtSystem', parent=prnt, pos=wx.Point(284, 86),
              size=self.mainwin, style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=purchsetitle)
        self.SetClientSize(self.mainwin)

        self.panel1 = wx.Panel(id=wxID_PURCHSEMGMTSYSTEMPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.panel1,
              pos=wx.Point(0, 0), size=self.mainpagesize, style=wx.TAB_TRAVERSAL)

        self.PurchseProduct = wx.lib.buttons.GenButton(id=wxID_PURCHSEMGMTSYSTEMPURCHSEPRODUCT,
              label=self.purprodlabel, name='PurchseProduct', parent=self.CMSMainPage,
              pos=wx.Point(20, 10), size=wx.Size(120, 30), style=0)
        self.PurchseProduct.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.PurchsePoint = wx.lib.buttons.GenButton(id=wxID_PURCHSEMGMTSYSTEMPURCHSEPOINT,
              label=u'積分查詢', name='PurchsePoint', parent=self.CMSMainPage,
              pos=wx.Point(160, 10), size=wx.Size(120, 30), style=0)
        self.PurchsePoint.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        purpoint_size_x = 320
        purpoint_size_y = self.mainwin[1] - 20 - 40 - 40
        custlist_size_x = self.mainwin[0] - 40 - purpoint_size_x - 20
        custlist_size_y = purpoint_size_y
        self.CustList = wx.ListCtrl(id=wxID_PURCHSEMGMTSYSTEMCUSTLIST,
              name='CustList', parent=self.CMSMainPage, pos=wx.Point(20, 50),
              size=wx.Size(custlist_size_x, custlist_size_y),
              style=wx.LC_REPORT | wx.SUNKEN_BORDER | wx.LC_VRULES | wx.LC_HRULES |
              wx.LC_SINGLE_SEL)
        self.CustList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        purpoint_x = self.mainwin[0] - 20 - purpoint_size_x
        purpoint_y = 50
        self.PurchseList = wx.ListCtrl(id=wxID_PURCHSEMGMTSYSTEMPURCHSELIST,
              name='PurchseList', parent=self.CMSMainPage, pos=wx.Point(purpoint_x, purpoint_y),
              size=wx.Size(purpoint_size_x, purpoint_size_y),
              style=wx.LC_REPORT | wx.SUNKEN_BORDER | wx.LC_VRULES | wx.LC_HRULES | 
              wx.LC_SINGLE_SEL)
        self.PurchseList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        exit_x = self.mainwin[0] / 2 - 40
        exit_y = self.mainwin[1] - 40
        self.ExitButton = wx.Button(id=wxID_PURCHSEMGMTSYSTEMEXITBUTTON, label=u'離開',
              name='ExitButton', parent=self.CMSMainPage, pos=wx.Point(exit_x, exit_y),
              size=wx.Size(80, 30), style=0)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 警語
        warnpoint = (10, self.mainwin[1] - 15)
        self.WarningText = wx.StaticText(id=wxID_CMSMAINDIALOGWARNINGTEXT,
              label=self.warntext, name='WarningText', parent=self.CMSMainPage,
              pos=warnpoint, size=wx.Size(200, 13),
              style=wx.ALIGN_RIGHT)
        self.WarningText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))
        self.WarningText.SetForegroundColour((144, 144, 144))

    def __init__(self, membertype, purchsetitle, parent, mainwin, mainpagefile, mainpage, mainpagesize, prodpicturefile, imagedir, imginfo, dbname, custtable, prodtable, saletable, warntext):
        self.currentItem      = ''
        self.currentPointItem = ''
        self.purprodlabel     = u'產品訂購'

        self.membertype = membertype
        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.prodpicturefile = prodpicturefile
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.dbname = dbname
        self.custtable = custtable
        self.prodtable = prodtable
        self.saletable = saletable
        self.warntext = warntext

        sysinfo = GetSysInfo.GetSysInfo(self.membertype)
        self.CustomerHeaderList, self.CustomerHeaderId = sysinfo.GetCustomerHeaderList('purchse')
        self.ProductHeaderList, self.ProductHeaderId = sysinfo.GetProductHeaderList()
        self.PurchseHeaderList, self.PurchseHeaderId = sysinfo.GetPurchseHeaderList()

        self.prodimgdir = self.imginfo.GetProdImageDir()

        self._init_ctrls(parent, purchsetitle)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnPurchseProduct, self.PurchseProduct)
        self.Bind(wx.EVT_BUTTON, self.OnPurchsePoint,   self.PurchsePoint)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,     self.ExitButton)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelect, self.CustList)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.OnItemFocus, self.CustList)
        self.CustList.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.CustList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRightClick)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnPointSelect, self.PurchseList)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.OnPointFocus, self.PurchseList)
        self.PurchseList.Bind(wx.EVT_LEFT_DCLICK, self.OnPointDoubleClick)
        self.PurchseList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnPointRightClick)
        self.SetEscapeId(wxID_PURCHSEMGMTSYSTEMEXITBUTTON)

        self.PurchsePoint.Hide()

        self.allprodinfo = self.GetProductList()
        self.alluserinfo = self.GetAllUserInfo('alluser', '')
        #print self.alluserinfo
        self.CreatHeader()
        self.InitData(self.membertype, self.alluserinfo)
        
    def OnPurchseProduct(self, event):
        self.OnItemSelect(self.CustList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('PURCHSE')
        else:
            userinfo = self.alluserinfo[self.currentItem]
            userid = userinfo[0]
            dlg = PurchseProduct.PurchseProduct(self.parent, self.mainwin, self.purprodlabel, self.mainpagefile,
                                                self.mainpage, self.mainpagesize, self.ProductHeaderList, self.prodpicturefile,
                                                self.prodimgdir, self.imginfo, self.dbname, self.saletable,
                                                userid, self.allprodinfo, self.warntext)
            dlg.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

            purchseinfo = self.GetAllUserInfo('purchse', userid)
            self.InitPurchseData(purchseinfo)

        return

    def OnPurchsePoint(self, event):
        self.OnItemSelect(self.CustList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('MODIFY')
        else:
            userinfo = self.alluserinfo[self.currentItem]
            userid = userinfo[0]
            purchseinfo = self.GetAllUserInfo('purchse', userid)
            #print '%s Purchse list:  %s'%(userid, purchseinfo)
            self.InitPurchseData(purchseinfo)

        return

    def OnItemSelect(self, event):
        selectitem = self.CustList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
        if selectitem != self.currentItem:
            self.currentItem = selectitem
            self.OnPurchsePoint(self.PurchsePoint)

        return

    def OnItemFocus(self, event):

        return

    def OnRightClick(self, event):

        return

    def OnDoubleClick(self, event):
        self.OnPurchseProduct(self.PurchseProduct)

        return

    def OnPointSelect(self, event):
        self.currentPointItem = self.PurchseList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)

        return

    def OnPointFocus(self, event):

        return

    def OnPointRightClick(self, event):

        return

    def OnPointDoubleClick(self, event):

        return

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def GetAllUserInfo(self, gettype, userid):
        alluserinfo = []
        sqlaction = 'select'
        if gettype == 'alluser':
            sqlcmd = '''SELECT * FROM %s
                    '''%(self.custtable)
        elif gettype == 'allprod':
            sqlcmd = '''SELECT Product_SerialNo, Product_Name, Product_Spec,
                                Product_ListPrice, Product_SalePrice
                        FROM %s
                    '''%(self.prodtable)
        elif gettype == 'purchse':
            sqlcmd = '''SELECT Sale_CustomerId, FORMAT(Sale_PurchseTime, 'yyyy-mm') AS PurchseTime,
                                SUM(Sale_TotalPrice)
                        FROM %s
                        WHERE Sale_CustomerId = %s
                        GROUP BY Sale_CustomerId, FORMAT(Sale_PurchseTime, 'yyyy-mm')
                    '''%(self.saletable, int(userid))

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
            alluserinfo = info
            #print 'Query user info:  '
            #print alluserinfo
        except:
            print 'Query database error'
            print sqlcmd
            info = 'error'
        
        return alluserinfo

    def GetProductList(self):
        allprodinfo = {}

        prodinfo = self.GetAllUserInfo('allprod', '')
        for prod in prodinfo:
            sntext, nametext, spectext, listprice, saleprice = prod
            if not allprodinfo.has_key(sntext):
                allprodinfo[sntext] = []
            allprodinfo[sntext] = [nametext, spectext, listprice, saleprice]

        return allprodinfo

    def CreatHeader(self):
        #print 'Create list header'
        cid = 0
        for id in range(0, len(self.CustomerHeaderList)):
            hidlist = self.CustomerHeaderId.keys()
            hidlist.sort()
            if id in hidlist:
                titlename = self.CustomerHeaderList[id]
                colwidth  = self.CustomerHeaderId[id]
                #print id, titlename, colwidth
                self.CustList.InsertColumn(cid, titlename, width=colwidth)
                cid += 1

        cid = 0
        for id in range(0, len(self.ProductHeaderList)):
            hidlist = self.PurchseHeaderId.keys()
            hidlist.sort()
            if id in hidlist:
                titlename = self.PurchseHeaderList[id]
                colwidth  = self.PurchseHeaderId[id]
                #print id, titlename, colwidth
                self.PurchseList.InsertColumn(cid, titlename, width=colwidth)
                cid += 1

        return

    def InitData(self, membertype, showuserinfo):
        #print 'Clean all data'
        self.CustList.DeleteAllItems()

        if showuserinfo:
            listid = 0
            for userinfo in showuserinfo:
                #print userinfo
                cid = 0
                hidlist = self.CustomerHeaderId.keys()
                hidlist.sort()
                #print hidlist
                for id in hidlist:
                    #print listid, id, cid, userinfo[id + 2]
                    if hidlist.index(id) == 0:
                        self.CustList.InsertStringItem(listid, u'%s'%userinfo[id + 2])
                    else:
                        self.CustList.SetStringItem(listid, cid, u'%s'%userinfo[id + 2])
                    cid += 1
                listid += 1

        return

    def InitPurchseData(self, purchseinfo):
        #print 'Clean purchse data'
        self.PurchseList.DeleteAllItems()
        if purchseinfo:
            listid = 0
            for purinfo in purchseinfo:
                #print purinfo
                cid = 0
                hidlist = self.PurchseHeaderId.keys()
                hidlist.sort()
                #print hidlist
                for id in hidlist:
                    #print listid, id, cid, purinfo[id + 2]
                    if hidlist.index(id) == 0:
                        self.PurchseList.InsertStringItem(listid, u'%s'%purinfo[id])
                    else:
                        self.PurchseList.SetStringItem(listid, cid, u'%s'%purinfo[id])
                    cid += 1
                listid += 1

        return

    def ShowNoItemSelectMessage(self, type):
        if type == 'PURCHSE':
            msg = u'請先選擇一個用戶進行產品訂購！'

        dialog = wx.MessageDialog(self, msg, u'警告', wx.OK | wx.ICON_INFORMATION)
        dialog.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        result = dialog.ShowModal()

        return

