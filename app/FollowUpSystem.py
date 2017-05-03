# -*- coding: utf-8 -*-
#Boa:Dialog:FollowUpSystem

import wx
import wx.lib.buttons

import GetSysInfo
import NewContent

def create(parent):
    return FollowUpSystem(parent)

[wxID_FOLLOWUPSYSTEM, wxID_FOLLOWUPSYSTEMEXITBUTTON, 
 wxID_FOLLOWUPSYSTEMCUSTLIST, wxID_FOLLOWUPSYSTEMADDCONTENT, 
 wxID_BITMAPCMSMAINPAGE, wxID_CMSMAINDIALOGWARNINGTEXT,
 wxID_FOLLOWUPSYSTEMQUERYCONTENT, wxID_FOLLOWUPSYSTEMMODIFYCONTENT,
] = [wx.NewId() for _init_ctrls in range(8)]

class FollowUpSystem(wx.Dialog):
    def _init_ctrls(self, prnt, followtitle, queryconlist):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_FOLLOWUPSYSTEM, name='FollowUpSystem',
              parent=prnt, pos=wx.Point(82, 86), size=self.mainwin,
              style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=followtitle)
        self.SetClientSize(self.mainwin)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self,
              pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.ALIGN_CENTRE|wx.TAB_TRAVERSAL)

        self.AddContent = wx.lib.buttons.GenButton(id=wxID_FOLLOWUPSYSTEMADDCONTENT,
              label=self.addconlabel, name='AddContent', parent=self.CMSMainPage,
              pos=wx.Point(20, 10), size=wx.Size(150, 30), style=0)
        self.AddContent.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.ModifyContent = wx.lib.buttons.GenButton(id=wxID_FOLLOWUPSYSTEMMODIFYCONTENT,
              label=self.modconlabel, name='ModifyContent', parent=self.CMSMainPage,
              pos=wx.Point(190, 10), size=wx.Size(150, 30), style=0)
        self.ModifyContent.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.QueryContent = wx.Choice(choices=queryconlist,
              id=wxID_FOLLOWUPSYSTEMQUERYCONTENT, name='QueryContent',
              parent=self.CMSMainPage, pos=wx.Point(360, 10),
              size=wx.Size(200, 30), style=0)
        self.QueryContent.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        custlist_size_x = self.mainwin[0] - 40
        custlist_size_y = self.mainwin[1] - 20 - 40 - 40
        self.CustList = wx.ListCtrl(id=wxID_FOLLOWUPSYSTEMCUSTLIST,
              name='CustList', parent=self.CMSMainPage, pos=wx.Point(20, 50),
              size=wx.Size(custlist_size_x, custlist_size_y),
              style=wx.LC_REPORT | wx.SUNKEN_BORDER | wx.LC_VRULES | wx.LC_HRULES | 
              wx.LC_SINGLE_SEL)
        self.CustList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        exit_x = self.mainwin[0] / 2 - 40
        exit_y = self.mainwin[1] - 40
        self.ExitButton = wx.Button(id=wxID_FOLLOWUPSYSTEMEXITBUTTON, label=u'離開',
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

    def __init__(self, followtitle, parent, mainwin, mainpagefile, mainpage, mainpagesize, imagedir, imginfo, dbname, custtable, followtable, warntext):
        self.currentItem    = -1
        self.addconlabel = u'新增行程記錄'
        self.modconlabel = u'修改行程記錄'

        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.dbname = dbname
        self.custtable = custtable
        self.followtable = followtable
        self.warntext = warntext

        self.membertype = ''
        self.sysinfo = GetSysInfo.GetSysInfo()
        self.conlist, self.queryconlist = self.sysinfo.GetQueryContentList()
        self.ContentHeaderList, self.ContentHeaderId = self.sysinfo.GetContentHeaderList()
        self.allusername = self.GetAllUserName()

        self.mainpagetype = self.imginfo.GetImageType(self.mainpagefile)

        self._init_ctrls(parent, followtitle, self.queryconlist)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnAddContent,    self.AddContent)
        self.Bind(wx.EVT_BUTTON, self.OnModifyContent, self.ModifyContent)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,    self.ExitButton)
        self.Bind(wx.EVT_CHOICE, self.OnQueryContent,  self.QueryContent)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelect, self.CustList)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.OnItemFocus, self.CustList)
        self.CustList.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.CustList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRightClick)
        self.SetEscapeId(wxID_FOLLOWUPSYSTEMEXITBUTTON)
        #self.ExitButton.SetFocus()

        self.QueryContent.SetSelection(0)

        self.allfollowinfo = self.sysinfo.GetAllFollowInfo(self.dbname, self.followtable, '')
        #print self.allfollowinfo
        self.CreateHeader()
        self.InitData(self.allfollowinfo)

    def OnAddContent(self, event):
        followinfo = []
        action = 'add'
        dlg = NewContent.NewContent(self.parent, action, self.addconlabel, self.mainwin, self.mainpagefile, self.mainpage, self.mainpagesize,
                                    self.mainpagetype, self.ContentHeaderList, self.dbname, self.followtable, self.warntext,
                                    self.conlist, self.allusername, followinfo)
        dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

        searchselect = self.QueryContent.GetSelection()
        if searchselect != 0:
            searchname = self.conlist[searchselect]
        else:
            searchname = ''
        self.allfollowinfo = self.sysinfo.GetAllFollowInfo(self.dbname, self.followtable, searchname)
        #print self.allfollowinfo
        self.InitData(self.allfollowinfo)

        return

    def OnModifyContent(self, event):
        self.OnItemSelect(self.CustList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('MODIFY')
        else:
            followinfo = self.allfollowinfo[self.currentItem]
            action = 'modify'
            dlg = NewContent.NewContent(self.parent, action, self.addconlabel, self.mainwin, self.mainpagefile, self.mainpage, self.mainpagesize,
                                        self.mainpagetype, self.ContentHeaderList, self.dbname, self.followtable, self.warntext,
                                        self.conlist, self.allusername, followinfo)
            dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

            searchselect = self.QueryContent.GetSelection()
            if searchselect != 0:
                searchname = self.conlist[searchselect]
            else:
                searchname = ''
            self.allfollowinfo = self.sysinfo.GetAllFollowInfo(self.dbname, self.followtable, searchname)
            #print self.allfollowinfo
            self.InitData(self.allfollowinfo)

        return

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def OnQueryContent(self, event):
        searchselect = self.QueryContent.GetSelection()
        if searchselect != 0:
            searchname = self.conlist[searchselect]
        else:
            searchname = ''
        self.allfollowinfo = self.sysinfo.GetAllFollowInfo(self.dbname, self.followtable, searchname)
        #print self.allfollowinfo
        self.InitData(self.allfollowinfo)

        return
        
    def OnItemSelect(self, event):
        self.currentItem = self.CustList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)

        return

    def OnItemFocus(self, event):

        return

    def OnDoubleClick(self, event):

        return

    def OnRightClick(self, event):

        return

    def GetAllUserName(self):
        namelist = [u'請選擇']

        allusername = self.sysinfo.GetAllUserInfo(self.dbname, '', self.custtable, self.queryconlist, '')
        if allusername:
            for item in allusername:
                name = item[0]
                namelist.append(name)

        return namelist

    def CreateHeader(self):
        #print 'Create list header'
        cid = 0
        for id in range(0, len(self.ContentHeaderList)):
            hidlist = self.ContentHeaderId.keys()
            hidlist.sort()
            if id in hidlist:
                titlename = self.ContentHeaderList[id]
                colwidth  = self.ContentHeaderId[id]
                #print id, titlename, colwidth
                self.CustList.InsertColumn(cid, titlename, width=colwidth)
                cid += 1

        return

    def InitData(self, showfollowinfo):
        #print 'Clean all data'
        self.CustList.DeleteAllItems()

        if showfollowinfo:
            listid = 0
            for followinfo in showfollowinfo:
                #print followinfo
                cid = 0
                hidlist = self.ContentHeaderId.keys()
                hidlist.sort()
                #print hidlist
                for id in hidlist:
                    #print listid, id, cid, followinfo[id + 2]
                    if id == 0:
                        self.CustList.InsertStringItem(listid, u'%s'%followinfo[id + 1])
                    else:
                        self.CustList.SetStringItem(listid, cid, u'%s'%followinfo[id + 1])
                    cid += 1
                listid += 1

        return

    def ShowNoItemSelectMessage(self, type):
        if type == 'MODIFY':
            msg = u'請先選擇一個項目進行修改！'

        dialog = wx.MessageDialog(self, msg, u'警告', wx.OK | wx.ICON_INFORMATION)
        dialog.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        result = dialog.ShowModal()

        return



