# -*- coding: utf-8 -*-
#Boa:Dialog:CMSMainDialog

from os import path
import wx

import GetImageInfo
import CustMgmtSystem
import ProductMgmtSystem
import PurchseMgmtSystem
import FollowUpSystem

def create(parent):
    return CMSMainDialog(parent)

[wxID_CMSMAINDIALOG, wxID_CUSTMGMTBUTTON,
 wxID_NONCUSTMGMTBUTTON, wxID_PRODUCTMGMTBUTTON, 
 wxID_PURCHSEMGMTBUTTON, 
 wxID_FOLLOWUPBUTTON, wxID_EXITBUTTON,
 wxID_CMSMAINPANEL, wxID_BITMAPCMSMAINPAGE,
 wxID_CMSMAINDIALOGWARNINGTEXT, wxID_CHANGEBUTTON,
] = [wx.NewId() for _init_ctrls in range(11)]

class CMSMainDialog(wx.Dialog):
    def _init_ctrls(self, prnt, maintitle, custlabel, noncustlabel, productlabel, purchselabel, followlabel, exitlabel, changelabel):
        buttonsize = (300, 50)
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_CMSMAINDIALOG, name='CMSMainDialog',
              parent=prnt, pos=wx.Point(456, 150), size=self.mainwin,
              style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=maintitle)
        self.SetClientSize(self.mainwin)

        self.CMSMainPanel = wx.Panel(id=wxID_CMSMAINPANEL, name='CMSMainPanel',
              parent=self, pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.CMSMainPanel,
              pos=wx.Point(0, 0), size=self.bgimagesize, style=wx.ALIGN_CENTRE|wx.TAB_TRAVERSAL)

        ### 會員資料
        custpoint = (50, 30)
        self.CustMgmtButton = wx.Button(id=wxID_CUSTMGMTBUTTON, label=custlabel,
              name='CustMgmtButton', parent=self.CMSMainPage, pos=custpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.CustMgmtButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 非會員資料
        noncustpoint = (50, 110)
        self.NonCustMgmtButton = wx.Button(id=wxID_NONCUSTMGMTBUTTON, label=noncustlabel,
              name='NonCustMgmtButton', parent=self.CMSMainPage, pos=noncustpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.NonCustMgmtButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 產品內容維護
        prodpoint = (50, 190)
        self.ProductMgmtButton = wx.Button(id=wxID_PRODUCTMGMTBUTTON, label=productlabel,
              name='ProductMgmtButton', parent=self.CMSMainPage, pos=prodpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.ProductMgmtButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 產品購買及消費查詢
        purchsepoint = (50, 270)
        self.PurchseMgmtButton = wx.Button(id=wxID_PURCHSEMGMTBUTTON, label=purchselabel,
              name='PurchseMgmtButton', parent=self.CMSMainPage, pos=purchsepoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.PurchseMgmtButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 跟進內容
        followpoint = (50, 350)
        self.FollowUpButton = wx.Button(id=wxID_FOLLOWUPBUTTON, label=followlabel,
              name='FollowUpButton', parent=self.CMSMainPage, pos=followpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.FollowUpButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 離開
        exitpoint = (50, 430)
        self.ExitButton = wx.Button(id=wxID_EXITBUTTON, label=exitlabel,
              name='ExitButton', parent=self.CMSMainPage, pos=exitpoint,
              size=buttonsize, style=wx.BU_LEFT)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### 變更底圖
        changepoint = (20, self.mainwin[1] - 50)
        self.ChangeButton = wx.Button(id=wxID_CHANGEBUTTON, label=changelabel,
              name='ChangeButton', parent=self.CMSMainPage, pos=changepoint,
              size=wx.Size(80, 25), style=wx.ALIGN_RIGHT)
        self.ChangeButton.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
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

    def __init__(self, parent, workdir, dbdata, imgdata):
        self.parent  = parent
        self.workdir = workdir
        self.dbdata  = dbdata
        self.imgdata = imgdata

        self.dbdir      = self.dbdata['DBDIR']
        self.dbfilename = self.dbdata['DBNAME']
        self.custtable  = self.dbdata['CUSTTABLE']
        self.prodtable  = self.dbdata['PRODTABLE']
        self.saletable  = self.dbdata['SALETABLE']

        self.imagedir        = self.imgdata['IMGDIR']
        self.mainpagefile    = self.imgdata['MAIN']['FILENAME']
        self.csmainpagefile  = self.imgdata['MAIN']['CSFILENAME']
        self.custpicturefile = self.imgdata['CUST']['FILENAME']
        self.prodpicturefile = self.imgdata['PROD']['FILENAME']

        self.custtitle      = u'會員資料'
        self.noncusttitle   = u'非會員資料'
        self.producttitle   = u'產品維護'
        self.purchsetitle   = u'產品訂購及消費積分查詢'
        self.followtitle    = u'跟進內容'

        maintitle      = u'客戶資料管理系統'
        custlabel      = u'  1. %s'%self.custtitle
        noncustlabel   = u'  2. %s'%self.noncusttitle
        productlabel   = u'  3. %s'%self.producttitle
        purchselabel   = u'  4. %s'%self.purchsetitle
        followlabel    = u'  5. %s'%self.followtitle
        exitlabel      = u'  6. 離開'
        changelabel    = u'變更底圖'
        self.warntext  = u'軟體版權為 陳智凱 所有，有著作權、侵害必究'

        self.imginfo = GetImageInfo.GetImageInfo(self.imgdata)
            #(self.imagedir, picwidth, picheight, maxwidth, maxheight)
        if path.isfile(self.csmainpagefile):
            self.bgimagefile = self.csmainpagefile
        else:
            self.bgimagefile = self.mainpagefile
        self.bgimagefilename, self.bgimage, self.bgimagesize = self.imginfo.GetImageInfo('mainpage', self.bgimagefile)
        #print self.bgimagesize
        #self.mainwin = (500, 500)
        self.mainwin = self.bgimagesize
        #print self.mainwin

        self._init_ctrls(parent, maintitle, custlabel, noncustlabel, productlabel,
                         purchselabel, followlabel, exitlabel, changelabel)
        self.Center()
        self.CMSMainPage.SetBitmap(self.bgimage)

        self.Bind(wx.EVT_BUTTON, self.OnCustMgmtButton,    self.CustMgmtButton)
        self.Bind(wx.EVT_BUTTON, self.OnNonCustMgmtButton, self.NonCustMgmtButton)
        self.Bind(wx.EVT_BUTTON, self.OnProductMgmtButton, self.ProductMgmtButton)
        self.Bind(wx.EVT_BUTTON, self.OnPurchseMgmtButton, self.PurchseMgmtButton)
        self.Bind(wx.EVT_BUTTON, self.OnFollowUpButton,    self.FollowUpButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,        self.ExitButton)
        self.Bind(wx.EVT_BUTTON, self.OnChangeButton,      self.ChangeButton)
        self.SetEscapeId(wxID_EXITBUTTON)
        self.CustMgmtButton.SetFocus()

        mdb_driver = self.GetDriver()
        self.dbname = 'DRIVER={%s};DBQ=%s;ExtendedAnsiSQL=1'%(mdb_driver, self.dbfilename)

    def OnCustMgmtButton(self, event):
        dlg = CustMgmtSystem.CustMgmtSystem('Member', self.custtitle, self.parent, self.mainwin, self.bgimagefile, self.bgimage,
                                            self.bgimagesize, self.custpicturefile, self.imagedir, self.imginfo,
                                            self.dbname, self.custtable, self.warntext)
        dlg.SetIcon(wx.Icon(self.bgimagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnNonCustMgmtButton(self, event):
        dlg = CustMgmtSystem.CustMgmtSystem('Nonmember', self.noncusttitle, self.parent, self.mainwin, self.bgimagefile, self.bgimage,
                                            self.bgimagesize, self.custpicturefile, self.imagedir, self.imginfo,
                                            self.dbname, self.custtable, self.warntext)
        dlg.SetIcon(wx.Icon(self.bgimagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnProductMgmtButton(self, event):
        dlg = ProductMgmtSystem.ProductMgmtSystem('All', self.producttitle, self.parent, self.mainwin, self.bgimagefile, self.bgimage,
                                                  self.bgimagesize, self.prodpicturefile, self.imagedir, self.imginfo,
                                                  self.dbname, self.prodtable, self.warntext)
        dlg.SetIcon(wx.Icon(self.bgimagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnPurchseMgmtButton(self, event):
        dlg = PurchseMgmtSystem.PurchseMgmtSystem('All', self.purchsetitle, self.parent, self.mainwin, self.bgimagefile, self.bgimage,
                                                  self.bgimagesize, self.prodpicturefile, self.imagedir, self.imginfo,
                                                  self.dbname, self.custtable, self.prodtable, self.saletable, self.warntext)
        dlg.SetIcon(wx.Icon(self.bgimagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnFollowUpButton(self, event):
        dlg = FollowUpSystem.FollowUpSystem(self.followtitle, self.parent, self.mainwin, self.bgimagefile, self.bgimage,
                                            self.bgimagesize, self.imagedir, self.imginfo,
                                            self.warntext)
        dlg.SetIcon(wx.Icon(self.bgimagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def OnChangeButton(self, event):
        selectfilename = self.imginfo.GetNewImageFile()
        if selectfilename != '':
            self.CMSMainPage.SetBitmap(wx.NullBitmap)
            self.csmainpagefile = self.imginfo.CopyNewImageFile(selectfilename, self.csmainpagefile)
            #print selectfilename, self.csmainpagefile
            self.bgimagefilename, self.bgimage, self.bgimagesize = \
                                  self.imginfo.GetImageInfo('mainpage', self.csmainpagefile)
            #print self.bgimagesize
            self.CMSMainPage.SetBitmap(self.bgimage)

        return

    def GetDriver(self):
        import pyodbc

        drivers = pyodbc.drivers()
        #print drivers
        mdb_driver = [d for d in drivers if 'Microsoft Access Driver (*.mdb' in d]
        if mdb_driver:
            mdb_driver = mdb_driver[0]
        else:
            print 'Microsoft Access Driver (*.mdb) does not installed'

        return mdb_driver

