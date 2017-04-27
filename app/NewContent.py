# -*- coding: utf-8 -*-
#Boa:Dialog:NewContent

from os import path
from glob import glob
from datetime import datetime
import wx

import CalendarDialog
import ConnectDB

def create(parent):
    return NewContent(parent)

[wxID_NEWCONTENT, wxID_BITMAPCMSMAINPAGE, 
 wxID_NEWCONTENTNAMEHEADER, wxID_NEWCONTENTNAMETEXT,
 wxID_NEWCONTENTDATEHEADER, wxID_NEWCONTENTDATETEXT,
 wxID_NEWCONTENTPAGEHEADER, wxID_CMSMAINDIALOGWARNINGTEXT,
 wxID_NEWCONTENTCONTENTHEADER, wxID_NEWCONTENTCONTENTTEXT,
 wxID_NEWCONTENTADDBUTTON, wxID_NEWCONTENTEXITBUTTON,
 wxID_NEWCONTENTCATEGORYHEADER, wxID_NEWCONTENTCATEGORYTEXT,
] = [wx.NewId() for _init_ctrls in range(14)]

class NewContent(wx.Dialog):
    def _init_ctrls(self, prnt, contenttitle, custlist, conlist):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_NEWCONTENT,
              name='NewContent', parent=prnt, pos=wx.Point(453, 154),
              size=self.mainwin, style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=contenttitle)
        self.SetClientSize(self.mainwin)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self,
              pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.ALIGN_CENTRE|wx.TAB_TRAVERSAL)

        header_x = 20
        header_y = 20
        self.PageHeader = wx.StaticText(id=wxID_NEWCONTENTPAGEHEADER,
              label=contenttitle, name='PageHeader', parent=self.CMSMainPage,
              pos=wx.Point(header_x, header_y), size=wx.Size(250, 40),
              style=wx.ALIGN_CENTER)
        self.PageHeader.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        split_x_1 = 20
        col2_extend = 150
        datelabel = u'%s'%self.ContentHeaderList[0]
        self.DateHeader = wx.StaticText(id=wxID_NEWCONTENTDATEHEADER,
              label=datelabel, name='DateHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 80), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.DateHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.DateText = wx.TextCtrl(id=wxID_NEWCONTENTDATETEXT,
              name='DateText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 80),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.DateText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        categorylabel = u'%s'%self.ContentHeaderList[1]
        self.CategoryHeader = wx.StaticText(id=wxID_NEWCONTENTCATEGORYHEADER,
              label=categorylabel, name='CategoryHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 120), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.CategoryHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.CategoryText = wx.Choice(choices=conlist,
              id=wxID_NEWCONTENTCATEGORYTEXT, name='CategoryText',
              parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 120),
              size=wx.Size(200, 25), style=0)
        self.CategoryText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        namelabel = u'%s'%self.ContentHeaderList[2]
        self.NameHeader = wx.StaticText(id=wxID_NEWCONTENTNAMEHEADER,
              label=namelabel, name='NameHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 160), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.NameHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.NameText = wx.Choice(choices=custlist,
              id=wxID_NEWCONTENTNAMETEXT, name='NameText',
              parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 160),
              size=wx.Size(200, 25), style=0)
        self.NameText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))


        contentlabel = u'%s'%self.ContentHeaderList[3]
        self.ContentHeader = wx.StaticText(id=wxID_NEWCONTENTCONTENTHEADER,
              label=contentlabel, name='ContentHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 200), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.ContentHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.ContentText = wx.TextCtrl(id=wxID_NEWCONTENTCONTENTTEXT,
              name='ContentText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 200),
              size=wx.Size(400, 300), style=wx.TE_RICH|wx.TE_MULTILINE, value='')
        self.ContentText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        add_x = split_x_1 + col2_extend
        add_y = 520
        self.AddButton = wx.Button(id=wxID_NEWCONTENTADDBUTTON,
              label=u'確認', name='AddButton', parent=self.CMSMainPage,
              pos=wx.Point(add_x, add_y), size=wx.Size(80, 30), style=0)
        self.AddButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        exit_x = add_x + 140
        exit_y = add_y
        self.ExitButton = wx.Button(id=wxID_NEWCONTENTEXITBUTTON,
              label=u'離開', name='ExitButton', parent=self.CMSMainPage,
              pos=wx.Point(exit_x, exit_y), size=wx.Size(80, 30), style=0)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        warnpoint = (10, self.mainwin[1] - 15)
        self.WarningText = wx.StaticText(id=wxID_CMSMAINDIALOGWARNINGTEXT,
              label=self.warntext, name='WarningText', parent=self.CMSMainPage,
              pos=warnpoint, size=wx.Size(200, 13),
              style=wx.ALIGN_LEFT)
        self.WarningText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))
        self.WarningText.SetForegroundColour((144, 144, 144))

    def __init__(self, parent, action, contenttitle, mainwin, mainpagefile, mainpage, mainpagesize, mainpagetype, ContentHeaderList, dbname, followtable, warntext, conlist, custlist, followinfo):
        self.followid = ''

        self.parent = parent
        self.action = action
        self.contenttitle = contenttitle
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.mainpagetype = mainpagetype
        self.ContentHeaderList = ContentHeaderList
        self.dbname = dbname
        self.followtable = followtable
        self.warntext = warntext
        self.conlist = conlist
        self.custlist = custlist
        self.followinfo = followinfo

        self._init_ctrls(parent, contenttitle, custlist, conlist)

        self.Bind(wx.EVT_BUTTON, self.OnAddButton,  self.AddButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton, self.ExitButton)
        self.DateText.Bind(wx.EVT_LEFT_DOWN, self.OnDateSelect)
        self.SetEscapeId(wxID_NEWCONTENTEXITBUTTON)

        self.NameText.SetSelection(0)
        self.CategoryText.SetSelection(0)
        currentdate = datetime.now().strftime('%Y-%m-%d')
        self.DateText.SetValue(currentdate)

        if self.action == 'modify' and self.followinfo:
            self.InsertProductInfo(self.followinfo)
            self.followid = self.followinfo[0]

    def OnDateSelect(self, event):
        selectdate = self.DateText.GetValue()
        dlg = CalendarDialog.CalendarDialog(self.parent, selectdate)
        dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        try:
            dlg.ShowModal()
            selectdate = dlg.selectdate
        except:
            selectdate = ''
        dlg.Destroy()

        self.DateText.SetValue(selectdate)

        return

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def OnAddButton(self, event):
        visittime = self.DateText.GetValue()
        category  = self.CategoryText.GetSelection()
        if category == 0:
            categoryinfo = ''
        else:
            categoryinfo = self.conlist[category]
        user = self.NameText.GetSelection()
        if user == 0:
            visituser = ''
        else:
            visituser = self.custlist[user]
        content   = self.ContentText.GetValue()

        #print visittime, categoryinfo, visituser, content
        if self.action == 'add':
            sqlaction = 'insert'
            sqlcmd  = '''INSERT INTO %s '''%(self.followtable, )
            sqlcmd += '''   (
                            Follow_Date, Follow_Category,
                            Follow_CustomerName, Follow_Content
                            )
                        VALUES (
                            '%s', '%s', 
                            '%s', '%s'
                            )
                    '''%(visittime, categoryinfo, visituser, content)
            addsqlcmd = ''
        elif self.action == 'modify':
            sqlaction = 'update'
            sqlcmd  = '''UPDATE %s SET '''%(self.followtable, )
            sqlcmd += '''   
                            Follow_Date       ='%s', Follow_Category ='%s',
                            Follow_CustomerName ='%s', Follow_Content  ='%s'
                    '''%(visittime, categoryinfo, visituser, content)
            addsqlcmd = '''WHERE Follow_ItemNo = %s '''%(self.followid)
        sqlcmd += addsqlcmd

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
        except:
            print 'Insert into database error'
            print sqlcmd
            info = 'error'

        self.Close()
        event.Skip()

    def InsertProductInfo(self, followinfo):
        self.followid, visittime, categoryinfo, visituser, content = followinfo
        if categoryinfo == '':
            catid = 0
        else:
            catid = self.conlist.index(categoryinfo)
        if visituser == '':
            userid = 0
        else:
            userid = self.custlist.index(visituser)


        self.DateText.SetValue(visittime)
        self.CategoryText.SetSelection(catid)
        self.NameText.SetSelection(userid)
        self.ContentText.SetValue(u'%s'%content)


        return

