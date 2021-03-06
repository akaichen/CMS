# -*- coding: utf-8 -*-
#Boa:Dialog:ProductMgmtSystem

from os import path
from glob import glob
import wx
import wx.lib.buttons

import GetSysInfo
import NewProduct

def create(parent):
    return ProductMgmtSystem(parent)

[wxID_PRODUCTMGMTSYSTEM, wxID_PRODUCTMGMTSYSTEMEXITBUTTON, 
 wxID_PRODUCTMGMTSYSTEMPRODLIST, 
 wxID_BITMAPCMSMAINPAGE, wxID_CMSMAINDIALOGWARNINGTEXT,
 wxID_PRODUCTMGMTSYSTEMNEWPRODUCT, wxID_PRODUCTMGMTSYSTEMMODIFYPRODUCT,
 wxID_PRODUCTMGMTSYSTEMPRODIMAGEBUTTON, 
] = [wx.NewId() for _init_ctrls in range(8)]

class ProductMgmtSystem(wx.Dialog):
    def _init_ctrls(self, prnt, producttitle):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PRODUCTMGMTSYSTEM,
              name='ProductMgmtSystem', parent=prnt, pos=wx.Point(284, 86),
              size=self.mainwin, style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=producttitle)
        self.SetClientSize(self.mainwin)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self,
              pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.ALIGN_CENTRE|wx.TAB_TRAVERSAL)

        self.NewProduct = wx.lib.buttons.GenButton(id=wxID_PRODUCTMGMTSYSTEMNEWPRODUCT,
              label=self.newprodlabel, name='NewProduct', parent=self.CMSMainPage,
              pos=wx.Point(20, 10), size=wx.Size(140, 30), style=0)
        self.NewProduct.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.ModifyProduct = wx.lib.buttons.GenButton(id=wxID_PRODUCTMGMTSYSTEMMODIFYPRODUCT,
              label=self.modprodlabel, name='ModifyProduct', parent=self.CMSMainPage,
              pos=wx.Point(180, 10), size=wx.Size(140, 30), style=0)
        self.ModifyProduct.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        prodimage_size_x, prodimage_size_y = self.fgimagesize
        prodlist_size_x = self.mainwin[0] - 40 - prodimage_size_x - 20
        prodlist_size_y = self.mainwin[1] - 20 - 40 - 40
        self.ProdList = wx.ListCtrl(id=wxID_PRODUCTMGMTSYSTEMPRODLIST,
              name='ProdList', parent=self.CMSMainPage, pos=wx.Point(20, 50),
              size=wx.Size(prodlist_size_x, prodlist_size_y), style=wx.LC_REPORT | wx.SUNKEN_BORDER |
              wx.LC_VRULES | wx.LC_HRULES | wx.LC_SINGLE_SEL)
        self.ProdList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        prodimage_x = self.mainwin[0] - 20 - prodimage_size_x
        prodimage_y = 50
        self.ProdImageButton = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_PRODUCTMGMTSYSTEMPRODIMAGEBUTTON, name='ProdImageButton',
              parent=self.CMSMainPage, pos=wx.Point(prodimage_x, prodimage_y),
              size=wx.Size(prodimage_size_x, prodimage_size_y),
              style=wx.BU_AUTODRAW)
        self.ProdImageButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
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
              style=wx.ALIGN_LEFT)
        self.WarningText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))
        self.WarningText.SetForegroundColour((144, 144, 144))

    def __init__(self, membertype, producttitle, parent, mainwin, mainpagefile, mainpage, mainpagesize, prodpicturefile, imagedir, imginfo, dbname, prodtable, warntext):
        self.newprodlabel = u'新增產品'
        self.modprodlabel = u'異動產品'
        self.currentItem = -1

        self.membertype = membertype
        self.producttitle = producttitle
        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.prodpicturefile = prodpicturefile
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.dbname = dbname
        self.prodtable = prodtable
        self.warntext = warntext

        self.fgimagefilename, self.fgimage, self.fgimagesize, self.fgimagetype = \
                              self.imginfo.GetImageInfo('prodpicture', self.prodpicturefile)
        #print self.fgimagefilename, self.fgimage, self.fgimagesize
        self.mainpagetype = self.imginfo.GetImageType(self.mainpagefile)
        self.prodimgdir = self.imginfo.GetProdImageDir()

        self.sysinfo = GetSysInfo.GetSysInfo()
        self.ProductHeaderList, self.ProductHeaderId = self.sysinfo.GetProductHeaderList()

        self._init_ctrls(parent, self.producttitle)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnNewProduct,   self.NewProduct)
        self.Bind(wx.EVT_BUTTON, self.OnModifyProduct, self.ModifyProduct)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,   self.ExitButton)
        self.Bind(wx.EVT_BUTTON, self.OnProdImageButton, self.ProdImageButton)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelect, self.ProdList)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.OnItemFocus, self.ProdList)
        self.ProdList.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.ProdList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRightClick)
        self.SetEscapeId(wxID_PRODUCTMGMTSYSTEMEXITBUTTON)
        #self.ExitButton.SetFocus()

        self.ProdImageButton.SetBitmap(self.fgimage)

        self.allprodinfo = self.sysinfo.GetAllProductInfo(self.dbname, self.prodtable)
        #print self.allprodinfo
        self.CreateHeader()
        self.InitData(self.membertype, self.allprodinfo)

    def OnNewProduct(self, event):
        prodinfo = []
        action = 'add'
        dlg = NewProduct.NewProduct(self.parent, self.newprodlabel, self.mainwin, self.mainpagefile, 
                                    self.mainpage, self.mainpagesize, self.prodimgdir, self.imginfo, 
                                    self.ProductHeaderList, self.dbname, self.prodtable, self.warntext,
                                    self.prodpicturefile, action, prodinfo)
        dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

        self.allprodinfo = self.sysinfo.GetAllProductInfo(self.dbname, self.prodtable)
        #print self.allprodinfo
        self.InitData(self.membertype, self.allprodinfo)

        return

    def OnModifyProduct(self, event):
        self.OnItemSelect(self.ProdList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('PRODMODIFY')
        else:
            prodinfo = self.allprodinfo[self.currentItem]
            action = 'modify'
            dlg = NewProduct.NewProduct(self.parent, self.modprodlabel, self.mainwin, self.mainpagefile,
                                        self.mainpage, self.mainpagesize, self.prodimgdir, self.imginfo,
                                        self.ProductHeaderList, self.dbname, self.prodtable, self.warntext,
                                        self.prodpicturefile, action, prodinfo)
            dlg.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

            self.allprodinfo = self.sysinfo.GetAllProductInfo(self.dbname, self.prodtable)
            #print self.allprodinfo
            self.InitData(self.membertype, self.allprodinfo)

        return

    def OnItemSelect(self, event):
        self.currentItem = self.ProdList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)

        if self.currentItem != -1:
            prodinfo = self.allprodinfo[self.currentItem]
            prodid = prodinfo[1]
            #prodpicture = '%s/%s.png'%(self.prodimgdir, prodid)
            listpictures = glob('%s/%s.*'%(self.prodimgdir, prodid))
            #print self.prodimgdir, listpictures
            if listpictures:
                prodpicture = listpictures[0]
                if not path.isfile(prodpicture):
                    prodpicture = self.prodpicturefile
            else:
                prodpicture = self.prodpicturefile

            self.fgimagefilename, self.fgimage, self.fgimagesize, self.fgimagetype = \
                                  self.imginfo.GetImageInfo('prodpicture', prodpicture)
            #print fgimagefilename, fgimage, fgimagesize, prodpicture
            self.ProdImageButton.SetBitmap(self.fgimage)

        return

    def OnItemFocus(self, event):

        return

    def OnRightClick(self, event):

        return

    def OnDoubleClick(self, event):
        self.OnModifyProduct(self.ModifyProduct)

        return

    def OnProdImageButton(self, event):

        return

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def CreateHeader(self):
        #print 'Create list header'
        cid = 0
        for id in range(0, len(self.ProductHeaderList)):
            hidlist = self.ProductHeaderId.keys()
            hidlist.sort()
            if id in hidlist:
                titlename = self.ProductHeaderList[id]
                colwidth  = self.ProductHeaderId[id]
                #print id, titlename, colwidth
                if cid in [3, 4]:
                    self.ProdList.InsertColumn(cid, titlename, wx.LIST_FORMAT_RIGHT, width=colwidth)
                else:
                    self.ProdList.InsertColumn(cid, titlename, width=colwidth)
                cid += 1

        return

    def InitData(self, membertype, showprodinfo):
        #print 'Clean all data'
        self.ProdList.DeleteAllItems()

        if showprodinfo:
            listid = 0
            for prodinfo in showprodinfo:
                cid = 0
                hidlist = self.ProductHeaderId.keys()
                hidlist.sort()
                for id in hidlist:
                    #print id, cid
                    if hidlist.index(id) == 0:
                        self.ProdList.InsertStringItem(listid, u'%s'%prodinfo[id + 1])
                    else:
                        if id in [3, 4]:
                            self.ProdList.SetStringItem(listid, cid, u'%s'%format(int('%s'%prodinfo[id + 1]), ','))
                        else:
                            self.ProdList.SetStringItem(listid, cid, u'%s'%prodinfo[id + 1])
                    cid += 1
                listid += 1

        return

    def ShowNoItemSelectMessage(self, type):
        if type == 'PRODMODIFY':
            msg = u'請先選擇一個產品進行修改！'

        dialog = wx.MessageDialog(self, msg, u'警告', wx.OK | wx.ICON_INFORMATION)
        dialog.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        result = dialog.ShowModal()

        return

