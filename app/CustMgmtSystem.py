# -*- coding: utf-8 -*-
#Boa:Dialog:CustMgmtSystem

from os import path
from glob import glob
import string
import wx
import wx.lib.buttons

import GetSysInfo
import NewCustomerInfo
import ConnectDB

def create(parent):
    return CustMgmtSystem(parent)

[wxID_CUSTMGMTSYSTEM, wxID_CUSTMGMTSYSTEMEXITBUTTON, 
 wxID_CUSTMGMTSYSTEMNEWCUSTOMER, wxID_CUSTMGMTSYSTEMMODIFYCUSTOMER, 
 wxID_CUSTMGMTSYSTEMGENQUERYCUSTOMER, wxID_CUSTMGMTSYSTEMCUSTLIST, 
 wxID_BITMAPCMSMAINPAGE,
 wxID_CMSMAINDIALOGWARNINGTEXT, wxID_CUSTMGMTSYSTEMQUERYJOBLEVEL,
 wxID_CUSTMGMTSYSTEMCUSTIMAGEBUTTON, 
] = [wx.NewId() for _init_ctrls in range(10)]

class CustMgmtSystem(wx.Dialog):
    def _init_ctrls(self, prnt, queryjoblist):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_CUSTMGMTSYSTEM, name='CustMgmtSystem',
              parent=prnt, pos=wx.Point(314, 167), size=self.mainwin,
              style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=self.custtitle)
        self.SetClientSize(self.mainwin)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self,
              pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.ALIGN_CENTRE|wx.TAB_TRAVERSAL)

        self.NewCustomer = wx.lib.buttons.GenButton(id=wxID_CUSTMGMTSYSTEMNEWCUSTOMER,
              label=u'新增', name='NewCustomer', parent=self.CMSMainPage,
              pos=wx.Point(20, 10), size=wx.Size(80, 30), style=wx.ALIGN_CENTRE)
        self.NewCustomer.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.ModifyCustomer = wx.lib.buttons.GenButton(id=wxID_CUSTMGMTSYSTEMMODIFYCUSTOMER,
              label=u'編輯', name='ModifyCustomer', parent=self.CMSMainPage,
              pos=wx.Point(120, 10), size=wx.Size(80, 30), style=wx.ALIGN_CENTRE)
        self.ModifyCustomer.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        if self.membertype == 'Member':
            ### Show on Customer page
            joblevel_x = 120 + 100
            joblevel_y = 10
            self.QueryJobLevel = wx.Choice(choices=queryjoblist,
                  id=wxID_CUSTMGMTSYSTEMQUERYJOBLEVEL, name='QueryJobLevel',
                  parent=self.CMSMainPage, pos=wx.Point(joblevel_x, joblevel_y),
                  size=wx.Size(150, 30), style=0)
            self.QueryJobLevel.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
                  False, u'新細明體'))
        elif self.membertype == 'Nonmember':
            ### Show on Non-Customer page
            joblevel_x = 120 + 100
            joblevel_y = 10
            self.QueryJobLevel = wx.lib.buttons.GenButton(id=wxID_CUSTMGMTSYSTEMQUERYJOBLEVEL, 
                  label=u'轉成正式會員', name='MoveCustomer', parent=self.CMSMainPage,
                  pos=wx.Point(joblevel_x, joblevel_y), size=wx.Size(150, 30),
                  style=wx.ALIGN_CENTRE)
            self.QueryJobLevel.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
                  False, u'新細明體'))

        ###
        query_x = self.mainwin[0] - 20 - 250
        query_y = 10
        self.QueryCustomer = wx.SearchCtrl(id=wxID_CUSTMGMTSYSTEMGENQUERYCUSTOMER,
              name='QueryCustomer', parent=self.CMSMainPage, pos=wx.Point(query_x, query_y),
              size=wx.Size(250, 30), style=wx.TE_PROCESS_ENTER, value='')
        self.QueryCustomer.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))
        self.QueryCustomer.ShowSearchButton(True)
        self.QueryCustomer.ShowCancelButton(True)

        custimage_size_x, custimage_size_y = self.fgimagesize
        custlist_size_x = self.mainwin[0] - 40 - custimage_size_x - 20
        custlist_size_y = self.mainwin[1] - 20 - 40 - 40
        self.CustList = wx.ListCtrl(id=wxID_CUSTMGMTSYSTEMCUSTLIST,
              name='CustList', parent=self.CMSMainPage, pos=wx.Point(20, 50),
              size=wx.Size(custlist_size_x, custlist_size_y), style=wx.LC_REPORT | wx.SUNKEN_BORDER |
              wx.LC_VRULES | wx.LC_HRULES | wx.LC_SINGLE_SEL)
        self.CustList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        custimage_x = self.mainwin[0] - 20 - custimage_size_x
        custimage_y = 50
        self.CustImageButton = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_CUSTMGMTSYSTEMCUSTIMAGEBUTTON, name='CustImageButton',
              parent=self.CMSMainPage, pos=wx.Point(custimage_x, custimage_y),
              size=wx.Size(custimage_size_x, custimage_size_y),
              style=wx.BU_AUTODRAW)
        self.CustImageButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        exit_x = self.mainwin[0] / 2 - 40
        exit_y = self.mainwin[1] - 40
        self.ExitButton = wx.Button(id=wxID_CUSTMGMTSYSTEMEXITBUTTON, label=u'離開',
              name='ExitButton', parent=self.CMSMainPage, pos=wx.Point(exit_x, exit_y),
              size=wx.Size(80, 30), style=0)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 警語
        warnpoint = (10, self.mainwin[1] - 15)
        self.WarningText = wx.StaticText(id=wxID_CMSMAINDIALOGWARNINGTEXT,
              label=self.warntext, name='WarningText', parent=self.CMSMainPage,
              pos=warnpoint, size=wx.Size(200, 13),
              style=wx.ALIGN_LEFT)
        self.WarningText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))
        self.WarningText.SetForegroundColour((144, 144, 144))

    def __init__(self, membertype, custtitle, parent, mainwin, mainpagefile, mainpage, mainpagesize, custpicturefile, imagedir, imginfo, dbname, custtable, warntext):
        self.membertype = membertype
        self.custtitle = custtitle
        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.custpicturefile = custpicturefile
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.dbname = dbname
        self.custtable = custtable
        self.warntext = warntext
        self.currentItem = -1

        self.fgimagefilename, self.fgimage, self.fgimagesize, self.fgimagetype = \
                              self.imginfo.GetImageInfo('custpicture', self.custpicturefile)
        #print self.fgimagefilename, self.fgimage, self.fgimagesize
        self.mainpagetype = self.imginfo.GetImageType(self.mainpagefile)
        self.custimgdir = self.imginfo.GetCustImageDir()

        sysinfo = GetSysInfo.GetSysInfo(self.membertype)
        self.CustomerHeaderList, self.CustomerHeaderId = sysinfo.GetCustomerHeaderList('customer')
        self.joblist, self.queryjoblist = sysinfo.GetJobLevelList()
        self.yearlist, self.monthlist, self.daylist = sysinfo.GetDateList()

        self._init_ctrls(parent, self.queryjoblist)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnNewCustomer,    self.NewCustomer)
        self.Bind(wx.EVT_BUTTON, self.OnModifyCustomer, self.ModifyCustomer)
        self.Bind(wx.EVT_BUTTON, self.OnQueryCustomer,  self.QueryCustomer)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,     self.ExitButton)
        self.Bind(wx.EVT_BUTTON, self.OnCustImageButton, self.CustImageButton)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelect, self.CustList)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.OnItemFocus, self.CustList)
        self.CustList.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.CustList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRightClick)
        #self.QueryCustomer.Bind(wx.EVT_TEXT, self.OnQueryCustomer)
        self.QueryCustomer.Bind(wx.EVT_TEXT_ENTER, self.OnQueryCustomer)
        self.QueryCustomer.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnQueryCustomer)
        self.QueryCustomer.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnQueryCustomerBTN)
        self.QueryCustomer.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnQueryCustomerCTN)
        self.SetEscapeId(wxID_CUSTMGMTSYSTEMEXITBUTTON)
        self.NewCustomer.SetFocus()

        if self.membertype == 'Member':
            self.QueryJobLevel.SetSelection(0)
            self.Bind(wx.EVT_CHOICE, self.OnQueryJobLevel, self.QueryJobLevel)
            #self.QueryJobLevel.Show()
        elif self.membertype == 'Nonmember':
            self.Bind(wx.EVT_BUTTON, self.OnMoveCustomer, self.QueryJobLevel)
            #self.QueryJobLevel.Hide()

        self.CustImageButton.SetBitmap(self.fgimage)

        self.alluserinfo = self.GetAllUserInfo(self.membertype, '')
        #print self.alluserinfo
        self.CreatHeader()
        self.InitData(self.membertype, self.alluserinfo)

    def OnNewCustomer(self, event):
        userinfo = []
        action = 'add'
        dlg = NewCustomerInfo.NewCustomerInfo(self.parent, self.membertype, self.mainwin, self.custtitle, self.mainpagefile, 
                                              self.mainpage, self.mainpagesize, self.custpicturefile, self.currentItem,
                                              self.custimgdir, self.imginfo, self.dbname, self.custtable, self.warntext,
                                              self.CustomerHeaderList, self.joblist, self.yearlist, self.monthlist, self.daylist,
                                              action, userinfo)
        dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

        self.alluserinfo = self.GetAllUserInfo(self.membertype, '')
        #print self.alluserinfo
        self.InitData(self.membertype, self.alluserinfo)

        return

    def OnModifyCustomer(self, event):
        self.OnItemSelect(self.CustList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('MODIFY')
        else:
            userinfo = self.alluserinfo[self.currentItem]
            action = 'modify'
            dlg = NewCustomerInfo.NewCustomerInfo(self.parent, self.membertype, self.mainwin, self.custtitle, self.mainpagefile, 
                                                  self.mainpage, self.mainpagesize, self.custpicturefile, self.currentItem,
                                                  self.custimgdir, self.imginfo, self.dbname, self.custtable, self.warntext,
                                                  self.CustomerHeaderList, self.joblist, self.yearlist, self.monthlist, self.daylist,
                                                  action, userinfo)
            dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

            searchname = self.QueryCustomer.GetValue()
            self.alluserinfo = self.GetAllUserInfo(self.membertype, searchname)
            #print self.alluserinfo
            self.InitData(self.membertype, self.alluserinfo)

        return

    def OnQueryCustomer(self, event):
        #print 'Query Customer'
        searchname = self.QueryCustomer.GetValue()
        if searchname == '':
            self.ShowNoItemSelectMessage('QUERYFAILED')
        else:
            self.alluserinfo = self.GetAllUserInfo(self.membertype, searchname)
            # print self.alluserinfo
            self.InitData(self.membertype, self.alluserinfo)

        return

    def OnQueryCustomerBTN(self, event):
        #print 'On query click'
        self.OnQueryCustomer(self.QueryCustomer)

        return

    def OnQueryCustomerCTN(self, event):
        #print 'Clear search string'
        self.QueryCustomer.Clear()
        self.alluserinfo = self.GetAllUserInfo(self.membertype, '')
        # print self.alluserinfo
        self.InitData(self.membertype, self.alluserinfo)

        return
                                
    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def OnItemSelect(self, event):
        self.currentItem = self.CustList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)

        if self.currentItem != -1:
            userinfo = self.alluserinfo[self.currentItem]
            userid_pic = string.zfill(userinfo[0], 6)
            #userpicture = '%s/%s.png'%(self.custimgdir, userid_pic)
            listpictures = glob('%s/%s.*'%(self.custimgdir, userid_pic))
            #print userinfo, userid_pic, self.custimgdir, listpictures
            if listpictures:
                custpicture = listpictures[0]
                if not path.isfile(custpicture):
                    custpicture = self.custpicturefile
            else:
                custpicture = self.custpicturefile

            self.fgimagefilename, self.fgimage, self.fgimagesize, self.fgimagetype = \
                                  self.imginfo.GetImageInfo('custpicture', custpicture)
            #print fgimagefilename, fgimage, fgimagesize, custpicture

            self.CustImageButton.SetBitmap(self.fgimage)

        return

    def OnItemFocus(self, event):

        return

    def OnRightClick(self, event):

        return

    def OnDoubleClick(self, event):
        self.OnModifyCustomer(self.ModifyCustomer)

        return

    def OnCustImageButton(self, event):

        return

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

    def GetAllUserInfo(self, membertype, searchname):
        alluserinfo = []
        sqlaction = 'select'
        if searchname == '':
            sqlcmd = '''SELECT * FROM %s
                        WHERE Customer_SaleType = '%s'
                    '''%(self.custtable, membertype)
        elif searchname in range(0, len(self.queryjoblist)):
            searchname = self.queryjoblist[searchname]
            sqlcmd = '''SELECT * FROM %s
                        WHERE Customer_SaleType = '%s' AND Customer_JobLevel = '%s'
                    '''%(self.custtable, membertype, searchname)
        else:
            sqlcmd = '''SELECT * FROM %s
                        WHERE Customer_SaleType = '%s' AND (
                                Customer_Name LIKE '%s' OR Customer_JobTitle LIKE '%s'
                                OR Customer_Telephone LIKE '%s' OR Customer_Cellphone LIKE '%s'
                                OR Customer_Area LIKE '%s' OR Customer_JobLevel LIKE '%s' )
                    '''%(self.custtable, membertype,
                         '%'+searchname+'%', '%'+searchname+'%', '%'+searchname+'%',
                         '%'+searchname+'%', '%'+searchname+'%', '%'+searchname+'%')

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

    def OnQueryJobLevel(self, event):
        searchselect = self.QueryJobLevel.GetSelection()
        if searchselect != 0:
            self.alluserinfo = self.GetAllUserInfo(self.membertype, searchselect)
            #print self.alluserinfo
        else:
            searchname = ''
            self.alluserinfo = self.GetAllUserInfo(self.membertype, searchname)
            #print self.alluserinfo
        self.InitData(self.membertype, self.alluserinfo)

        return

    def OnMoveCustomer(self, event):
        self.OnItemSelect(self.CustList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('MODIFY')
        else:
            userinfo = self.alluserinfo[self.currentItem]
            action = 'modify'
            dlg = NewCustomerInfo.NewCustomerInfo(self.parent, 'Member', self.mainwin, self.custtitle, self.mainpagefile, 
                                                  self.mainpage, self.mainpagesize, self.custpicturefile, self.currentItem,
                                                  self.custimgdir, self.imginfo, self.dbname, self.custtable, self.warntext,
                                                  self.CustomerHeaderList, self.joblist, self.yearlist, self.monthlist, self.daylist,
                                                  action, userinfo)
            dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

            searchname = self.QueryCustomer.GetValue()
            self.alluserinfo = self.GetAllUserInfo(self.membertype, searchname)
            #print self.alluserinfo
            self.InitData(self.membertype, self.alluserinfo)

        return

        self.OnItemSelect(self.CustList)
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('MOVECUSTOMER')
        else:
            userinfo = self.alluserinfo[self.currentItem]
            userid = userinfo[0]
            sqlaction = 'update'
            sqlcmd  = '''UPDATE %s SET Customer_SaleType = 'Member'
                            WHERE Customer_ItemNo = %s 
                    '''%(self.custtable, userid)

            try:
                db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
                info = db.ConnectDB()
                #print 'Query user info:  '
                #print alluserinfo
            except:
                print 'Query database error'
                print sqlcmd
                info = 'error'

            searchname = self.QueryCustomer.GetValue()
            self.alluserinfo = self.GetAllUserInfo(self.membertype, searchname)
            #print self.alluserinfo
            self.InitData(self.membertype, self.alluserinfo)

        return

    def ShowNoItemSelectMessage(self, type):
        if type == 'MODIFY':
            msg = u'請先選擇一個用戶進行修改！'
        elif type == 'QUERYFAILED':
            msg = u'請輸入搜尋關鍵字！'
        elif type == 'MOVECUSTOMER':
            msg = u'請先選擇一個用戶進行轉換！'

        dialog = wx.MessageDialog(self, msg, u'警告', wx.OK | wx.ICON_INFORMATION)
        dialog.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        result = dialog.ShowModal()

        return

