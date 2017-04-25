# -*- coding: utf-8 -*-
#Boa:Dialog:FollowUpSystem

import wx
import wx.lib.buttons

def create(parent):
    return FollowUpSystem(parent)

[wxID_FOLLOWUPSYSTEM, wxID_FOLLOWUPSYSTEMEXITBUTTON, 
 wxID_FOLLOWUPSYSTEMCUSTLIST, wxID_FOLLOWUPSYSTEMPANEL1,
 wxID_BITMAPCMSMAINPAGE, wxID_CMSMAINDIALOGWARNINGTEXT, 
] = [wx.NewId() for _init_ctrls in range(6)]

class FollowUpSystem(wx.Dialog):
    def _init_ctrls(self, prnt, followtitle):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_FOLLOWUPSYSTEM, name='FollowUpSystem',
              parent=prnt, pos=wx.Point(82, 86), size=self.mainwin,
              style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=followtitle)
        self.SetClientSize(self.mainwin)

        self.panel1 = wx.Panel(id=wxID_FOLLOWUPSYSTEMPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.panel1,
              pos=wx.Point(0, 0), size=self.mainpagesize, style=wx.TAB_TRAVERSAL)

        custlist_size_x = self.mainwin[0] - 40
        custlist_size_y = self.mainwin[1] - 40 - 50 - 50
        self.CustList = wx.ListCtrl(id=wxID_FOLLOWUPSYSTEMCUSTLIST,
              name='CustList', parent=self.CMSMainPage, pos=wx.Point(20, 70),
              size=wx.Size(custlist_size_x, custlist_size_y), style=wx.LC_ICON)
        self.CustList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        exit_x = self.mainwin[0] / 2 - 40
        exit_y = self.mainwin[1] - 50
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
              style=wx.ALIGN_RIGHT)
        self.WarningText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))
        self.WarningText.SetForegroundColour((144, 144, 144))

    def __init__(self, followtitle, parent, mainwin, mainpagefile, mainpage, mainpagesize, imagedir, imginfo, warntext):
        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.warntext = warntext

        self._init_ctrls(parent, followtitle)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnExitButton,        self.ExitButton)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelect, self.CustList)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.OnItemFocus, self.CustList)
        self.CustList.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.CustList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRightClick)
        self.SetEscapeId(wxID_FOLLOWUPSYSTEMEXITBUTTON)
        #self.ExitButton.SetFocus()

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

