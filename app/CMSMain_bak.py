# -*- coding: utf-8 -*-
#Boa:Dialog:CMSMainDialog

import wx

import GetImageInfo
import CustMgmtSystem
import NonCustMgmtSystem
import ProductMgmtSystem
import FollowUpSystem

def create(parent):
    return CMSMainDialog(parent)

[wxID_CMSMainDialog, wxID_CUSTMGMTBUTTON, wxID_NONCUSTMGMTBUTTON, wxID_PRODUCTMGMTBUTTON, 
 wxID_FOLLOWUPBUTTON, wxID_EXITBUTTON, wxID_CMSMAINPANEL, wxID_BITMAPCMSMAINPAGE,
] = [wx.NewId() for _init_ctrls in range(8)]

class CMSMainDialog(wx.Dialog):
    def __init__menus(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        aboutMenu = wx.Menu()

        quit = wx.MenuItem(fileMenu, wx.ID_EXIT, )
        fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+Q', 'Quit', kind=wx.ITEM_CHECK)

        aboutMenu.Append(wx.ID_ANY, '&About', 'About')
        
        menubar.Append(fileMenu, '&File')
        menubar.Append(aboutMenu, '&About')

        self.SetMenuBar(menubar)
        #self.text = wx.TextCtrl(self,-1, style = wx.EXPAND|wx.TE_MULTILINE)
        #self.Bind(wx.EVT_MENU, self.menuhandler)
        #self.SetSize((350, 250))
        #self.Centre()
        #self.Show(True)

    def menuhandler(self, event): 
        id = event.GetId() 
        if id == wx.ID_NEW: 
            self.text.AppendText("new"+"\n")

    def _init_ctrls(self, prnt, maintitle, custlabel, noncustlabel, productlabel, followlabel, exitlabel):
        buttonsize = (300, 50)
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_CMSMainDialog, name='CMSMainDialog',
              parent=prnt, pos=wx.Point(456, 150), size=self.mainwin,
              style=wx.DEFAULT_DIALOG_STYLE,
              title=maintitle)
        self.__init__menus()
        self.SetClientSize(self.mainwin)

        self.CMSMainPanel = wx.Panel(id=wxID_CMSMAINPANEL, name='CMSMainPanel',
              parent=self, pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.CMSMainPanel,
              pos=wx.Point(0, 0), size=self.mainpagesize, style=0)

        ### 會員資料
        custpoint = (50, 30)
        self.CustMgmtButton = wx.Button(id=wxID_CUSTMGMTBUTTON, label=custlabel,
              name='CustMgmtButton', parent=self.CMSMainPage, pos=custpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.CustMgmtButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        ### 非會員及消費者
        noncustpoint = (50, 110)
        self.NonCustMgmtButton = wx.Button(id=wxID_NONCUSTMGMTBUTTON, label=noncustlabel,
              name='NonCustMgmtButton', parent=self.CMSMainPage, pos=noncustpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.NonCustMgmtButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        ### 產品消費查詢
        prodpoint = (50, 190)
        self.ProductMgmtButton = wx.Button(id=wxID_PRODUCTMGMTBUTTON, label=productlabel,
              name='ProductMgmtButton', parent=self.CMSMainPage, pos=prodpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.ProductMgmtButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        ### 跟進內容
        followpoint = (50, 270)
        self.FollowUpButton = wx.Button(id=wxID_FOLLOWUPBUTTON, label=followlabel,
              name='FollowUpButton', parent=self.CMSMainPage, pos=followpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.FollowUpButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        ### 離開
        exitpoint = (50, 350)
        self.ExitButton = wx.Button(id=wxID_EXITBUTTON, label=exitlabel,
              name='ExitButton', parent=self.CMSMainPage, pos=exitpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

    def __init__(self, parent, workdir, imagedir, dbdir, mainpagefile, custpicturefile, picwidth, picheight, dbfilename, tablename, maxwidth, maxheight):
        self.parent = parent
        self.workdir = workdir
        self.imagedir = imagedir
        self.dbdir = dbdir
        self.mainpagefile = mainpagefile
        self.custpicturefile = custpicturefile
        self.dbfilename = '%s/%s'%(self.dbdir, dbfilename)
        self.tablename = tablename

        maintitle = '\xab\xc8\xa4\xe1\xb8\xea\xae\xc6\xba\xde\xb2z\xa8t\xb2\xce'
        custlabel = '  1. \xb7|\xad\xfb\xb8\xea\xae\xc6'
        noncustlabel = '  2. \xabD\xb7|\xad\xfb\xa4\xce\xae\xf8\xb6O\xaa\xcc'
        productlabel = '  3. \xb2\xa3\xab~\xae\xf8\xb6O\xacd\xb8\xdf'
        followlabel = '  4. \xb8\xf2\xb6i\xa4\xba\xaee'
        exitlabel = '  5. \xc2\xf7\xb6}'

        self.imginfo = GetImageInfo.GetImageInfo(self.imagedir, picwidth, picheight,
                                                 maxwidth, maxheight)
        self.mainpagefilename, self.mainpage, self.mainpagesize = \
                               self.imginfo.GetImageInfo('mainpage', '')     #(self.mainpagefile)
        self.custpicturefilename, self.custpicture, self.custpicturesize = \
                                  self.imginfo.GetImageInfo('custpicture', '')    #(self.custpicturefile)
        #print self.mainpagesize
        #print self.custpicturesize
        #self.mainwin = (500, 500)
        self.mainwin = self.mainpagesize
        #print self.mainwin

        self._init_ctrls(parent, maintitle, custlabel, noncustlabel, productlabel,
                         followlabel, exitlabel)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnCustMgmtButton,    self.CustMgmtButton)
        self.Bind(wx.EVT_BUTTON, self.OnNonCustMgmtButton, self.NonCustMgmtButton)
        self.Bind(wx.EVT_BUTTON, self.OnProductMgmtButton, self.ProductMgmtButton)
        self.Bind(wx.EVT_BUTTON, self.OnFollowUpButton,    self.FollowUpButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,        self.ExitButton)
        self.SetEscapeId(wxID_EXITBUTTON)
        self.CustMgmtButton.SetFocus()

        driver = self.GetDriver()
        self.dbname = 'DRIVER={%s};DBQ=%s;ExtendedAnsiSQL=1'%(driver, self.dbfilename)

    def OnCustMgmtButton(self, event):
        dlg = CustMgmtSystem.CustMgmtSystem('Member', self.parent, self.mainwin, self.mainpagefile, self.mainpage,
                                            self.mainpagesize, self.custpicturefile, self.custpicture,
                                            self.custpicturesize, self.imagedir, self.imginfo, self.tablename)
        dlg.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnNonCustMgmtButton(self, event):
        dlg = CustMgmtSystem.CustMgmtSystem('Nonmember', self.parent, self.mainwin, self.mainpagefile, self.mainpage,
                                            self.mainpagesize, self.custpicturefile, self.custpicture,
                                            self.custpicturesize, self.imagedir, self.imginfo, self.tablename)
        dlg.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnProductMgmtButton(self, event):
        dlg = ProductMgmtSystem.ProductMgmtSystem(self.parent, self.mainwin, self.mainpagefile, self.mainpage,
                                                  self.mainpagesize)
        dlg.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnFollowUpButton(self, event):
        dlg = FollowUpSystem.FollowUpSystem(self.parent, self.mainwin, self.mainpagefile, self.mainpage,
                                            self.mainpagesize)
        dlg.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def GetDriver(self):
        import pyodbc
        drivers = pyodbc.drivers()
        mdb_driver = [d for d in drivers if 'Microsoft Access Driver (*.mdb' in d]

        return mdb_driver[0]

