# -*- coding: utf-8 -*-
#Boa:Dialog:ProductMgmtSystem

import wx
import wx.lib.buttons

import GetSysInfo
import ConnectDB

def create(parent):
    return ProductMgmtSystem(parent)

[wxID_PRODUCTMGMTSYSTEM, wxID_PRODUCTMGMTSYSTEMEXITBUTTON, 
 wxID_PRODUCTMGMTSYSTEMCUSTLIST, wxID_PRODUCTMGMTSYSTEMPANEL1,
 wxID_BITMAPCMSMAINPAGE, wxID_CMSMAINDIALOGWARNINGTEXT,
 wxID_PRODUCTMGMTSYSTEMNEWPRODUCT, wxID_PRODUCTMGMTSYSTEMMODIFYPRODUCT, 
] = [wx.NewId() for _init_ctrls in range(8)]

class ProductMgmtSystem(wx.Dialog):
    def _init_ctrls(self, prnt, producttitle):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PRODUCTMGMTSYSTEM,
              name='ProductMgmtSystem', parent=prnt, pos=wx.Point(284, 86),
              size=self.mainwin, style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=producttitle)
        self.SetClientSize(self.mainwin)

        self.panel1 = wx.Panel(id=wxID_PRODUCTMGMTSYSTEMPANEL1, name='panel1',
              parent=self, pos=wx.Point(8, 0), size=self.mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.panel1,
              pos=wx.Point(0, 0), size=self.mainpagesize, style=wx.TAB_TRAVERSAL)

        self.NewProduct = wx.lib.buttons.GenButton(id=wxID_PRODUCTMGMTSYSTEMNEWPRODUCT,
              label=u'新增產品組合', name='NewProduct', parent=self.CMSMainPage,
              pos=wx.Point(20, 10), size=wx.Size(120, 30), style=0)
        self.NewProduct.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.ModifyProduct = wx.lib.buttons.GenButton(id=wxID_PRODUCTMGMTSYSTEMMODIFYPRODUCT,
              label=u'異動產品組合', name='ModifyProduct', parent=self.CMSMainPage,
              pos=wx.Point(160, 10), size=wx.Size(120, 30), style=0)
        self.ModifyProduct.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        custlist_x = self.mainwin[0] - 40
        custlist_y = self.mainwin[1] - 20 - 40 - 40
        self.CustList = wx.ListCtrl(id=wxID_PRODUCTMGMTSYSTEMCUSTLIST,
              name='CustList', parent=self.CMSMainPage, pos=wx.Point(20, 50),
              size=wx.Size(custlist_x, custlist_y), style=wx.LC_REPORT | wx.SUNKEN_BORDER |
              wx.LC_VRULES | wx.LC_HRULES | wx.LC_SINGLE_SEL)
        self.CustList.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        exit_x = self.mainwin[0] / 2 - 40
        exit_y = self.mainwin[1] - 40
        self.ExitButton = wx.Button(id=wxID_PRODUCTMGMTSYSTEMEXITBUTTON, label=u'離開',
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

    def __init__(self, membertype, producttitle, parent, mainwin, mainpagefile, mainpage, mainpagesize, dbname, tablename, warntext):
        self.membertype = membertype
        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.dbname = dbname
        self.tablename = tablename
        self.warntext = warntext

        sysinfo = GetSysInfo.GetSysInfo(self.membertype)
        self.ProductHeaderList, self.ProductHeaderId = sysinfo.GetProductHeaderList()

        self._init_ctrls(parent, producttitle)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnNewProduct,   self.NewProduct)
        self.Bind(wx.EVT_BUTTON, self.OnModifyProduct, self.ModifyProduct)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,   self.ExitButton)
        self.SetEscapeId(wxID_PRODUCTMGMTSYSTEMEXITBUTTON)
        #self.ExitButton.SetFocus()

        self.allprodinfo = self.GetAllProductInfo()
        #print self.allprodinfo
        self.CreatHeader()
        self.InitData(self.membertype, self.allprodinfo)
        
    def OnNewProduct(self, event):

        return

    def OnModifyProduct(self, event):

        return

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def GetAllProductInfo(self):
        allprodinfo = []
        sqlaction = 'select'
        searchname = ''
        if searchname == '':
            sqlcmd = '''SELECT * FROM %s
                    '''%(self.tablename)

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
            allprodinfo = info
            #print 'Query user info:  '
            #print allprodinfo
        except:
            print 'Query database error'
            print sqlcmd
            info = 'error'
        
        return allprodinfo

    def CreatHeader(self):
        #print 'Create list header'
        cid = 0
        for id in range(0, len(self.HeaderList)):
            if id in self.HeaderId:
                titlename = self.HeaderList[id]
                if id == 0:
                    colwidth = 120
                elif id == 1:
                    colwidth = 130
                elif id == 2:
                    colwidth = 130
                elif id == 6:
                    colwidth = 130
                elif id == 7:
                    colwidth = 130
                elif id == 8:
                    colwidth = 130
                else:
                    colwidth = 150

                #print id, titlename, colwidth
                self.CustList.InsertColumn(cid, titlename, width=colwidth)
                cid += 1

        return

    def InitData(self, membertype, showuserinfo):
        print 'Clean all data'
        self.CustList.DeleteAllItems()

        if showuserinfo:
            listid = 0
            for userinfo in showuserinfo:
                cid = 0
                for id in self.HeaderId:
                    #print self.HeaderId.index(id), cid
                    if self.HeaderId.index(id) == 0:
                        self.CustList.InsertStringItem(listid, '%s'%userinfo[id + 2])
                    else:
                        self.CustList.SetStringItem(listid, cid, '%s'%userinfo[id + 2])
                    cid += 1
                listid += 1
        return

