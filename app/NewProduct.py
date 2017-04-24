# -*- coding: utf-8 -*-
#Boa:Dialog:NewProduct

from os import path
import wx

import ConnectDB

def create(parent):
    return NewProduct(parent)

[wxID_NEWPRODUCT, wxID_NEWPRODUCTPANEL1,
 wxID_BITMAPCMSMAINPAGE, wxID_NEWPRODUCTSTATICBITMAP2,
 wxID_NEWPRODUCTSNHEADER, wxID_NEWPRODUCTSNTEXT,
 wxID_NEWPRODUCTNAMEHEADER, wxID_NEWPRODUCTNAMETEXT,
 wxID_NEWPRODUCTSPECHEADER, wxID_NEWPRODUCTSPECTEXT, 
 wxID_NEWPRODUCTLISTPRICEHEADER, wxID_NEWPRODUCTLISTPRICETEXT, 
 wxID_NEWPRODUCTSALEPRICEHEADER, wxID_NEWPRODUCTSALEPRICETEXT, 
 wxID_NEWPRODUCTADDBUTTON, wxID_NEWPRODUCTEXITBUTTON,
 wxID_CMSMAINDIALOGWARNINGTEXT, wxID_NEWPRODUCTPAGEHEADER,
 wxID_BITMAPPRODPICTURE,
] = [wx.NewId() for _init_ctrls in range(19)]

class NewProduct(wx.Dialog):
    def _init_ctrls(self, prnt, producttitle):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_NEWPRODUCT,
              name='NewProduct', parent=prnt, pos=wx.Point(453, 154),
              size=self.mainwin, style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=producttitle)
        self.SetClientSize(self.mainwin)

        self.panel1 = wx.Panel(id=wxID_NEWPRODUCTPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.panel1,
              pos=wx.Point(0, 0), size=self.mainpagesize, style=wx.TAB_TRAVERSAL)

        header_x = 20
        header_y = 20
        self.PageHeader = wx.StaticText(id=wxID_NEWPRODUCTPAGEHEADER,
              label=producttitle, name='PageHeader', parent=self.CMSMainPage,
              pos=wx.Point(header_x, header_y), size=wx.Size(250, 40),
              style=wx.ALIGN_CENTER)
        self.PageHeader.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        split_x_1 = 20
        col2_extend = 150
        snlabel = u'%s'%self.ProductHeaderList[0]
        self.SNHeader = wx.StaticText(id=wxID_NEWPRODUCTSNHEADER,
              label=snlabel, name='SNHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 80), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.SNHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.SNText = wx.TextCtrl(id=wxID_NEWPRODUCTSNTEXT,
              name='SNText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 80),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.SNText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### Product Picture
        prodpicture_x = split_x_1 + col2_extend + 200 + 20
        prodpicture_y = 20
        self.ProdPicture = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_BITMAPPRODPICTURE, name='BitmapProdPicture', parent=self.CMSMainPage,
              pos=wx.Point(prodpicture_x, prodpicture_y), size=self.fgimagesize, 
              style=wx.BU_AUTODRAW)

        namelabel = u'%s'%self.ProductHeaderList[1]
        self.NameHeader = wx.StaticText(id=wxID_NEWPRODUCTNAMEHEADER,
              label=namelabel, name='NameHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 120), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.NameHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.NameText = wx.TextCtrl(id=wxID_NEWPRODUCTNAMETEXT,
              name='NameText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 120),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.NameText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        speclabel = u'%s'%self.ProductHeaderList[2]
        self.SpecHeader = wx.StaticText(id=wxID_NEWPRODUCTSPECHEADER,
              label=speclabel, name='SpecHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 160), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.SpecHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.SpecText = wx.TextCtrl(id=wxID_NEWPRODUCTSPECTEXT,
              name='SpecText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 160),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.SpecText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        listpricelabel = u'%s'%self.ProductHeaderList[3]
        self.ListPriceHeader = wx.StaticText(id=wxID_NEWPRODUCTLISTPRICEHEADER,
              label=listpricelabel, name='ListPriceHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 200), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.ListPriceHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.ListPriceText = wx.TextCtrl(id=wxID_NEWPRODUCTLISTPRICETEXT,
              name='ListPriceText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 200),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.ListPriceText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        salepricelabel = u'%s'%self.ProductHeaderList[4]
        self.SalePriceHeader = wx.StaticText(id=wxID_NEWPRODUCTSALEPRICEHEADER,
              label=salepricelabel, name='SalePriceHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 240), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.SalePriceHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.SalePriceText = wx.TextCtrl(id=wxID_NEWPRODUCTSALEPRICETEXT,
              name='SalePriceText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 240),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.SalePriceText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        add_x = 60
        add_y = 280
        self.AddButton = wx.Button(id=wxID_NEWPRODUCTADDBUTTON,
              label=u'確認', name='AddButton', parent=self.CMSMainPage,
              pos=wx.Point(add_x, add_y), size=wx.Size(80, 30), style=0)
        self.AddButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        exit_x = add_x + 140
        exit_y = add_y
        self.ExitButton = wx.Button(id=wxID_NEWPRODUCTEXITBUTTON,
              label=u'離開', name='ExitButton', parent=self.CMSMainPage,
              pos=wx.Point(exit_x, exit_y), size=wx.Size(80, 30), style=0)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        warnpoint = (10, self.mainwin[1] - 15)
        self.WarningText = wx.StaticText(id=wxID_CMSMAINDIALOGWARNINGTEXT,
              label=self.warntext, name='WarningText', parent=self.CMSMainPage,
              pos=warnpoint, size=wx.Size(200, 13),
              style=wx.ALIGN_RIGHT)
        self.WarningText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))
        self.WarningText.SetForegroundColour((144, 144, 144))

    def __init__(self, parent, producttitle, mainwin, mainpagefile, mainpage, mainpagesize, imagedir, imginfo, ProductHeaderList, dbname, prodtable, warntext, prodpicturefile, action, prodinfo):
        self.prodpicture = ''
        self.newprodpicture = ''
        self.prodid = ''

        self.parent = parent
        self.producttitle = producttitle
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.ProductHeaderList = ProductHeaderList
        self.dbname = dbname
        self.prodtable = prodtable
        self.warntext = warntext
        self.prodpicturefile = prodpicturefile
        self.action = action
        self.prodinfo = prodinfo

        self.fgimagefilename, self.fgimage, self.fgimagesize = \
                              self.imginfo.GetImageInfo('prodpicture', self.prodpicturefile)
        #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.prodpicturefile

        self._init_ctrls(parent, self.producttitle)

        self.Bind(wx.EVT_BUTTON, self.OnAddButton,  self.AddButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton, self.ExitButton)
        self.Bind(wx.EVT_BUTTON, self.OnProdPicturePress, self.ProdPicture)
        self.SetEscapeId(wxID_NEWPRODUCTEXITBUTTON)

        if self.action == 'modify' and self.prodinfo:
            self.InsertProductInfo(self.prodinfo)
            prodid = self.prodinfo[0]
            self.prodpicture = '%s/%s.png'%(self.imagedir, prodid)
            if path.isfile(self.prodpicture):
                self.fgimagefilename, self.fgimage, self.fgimagesize = \
                                      self.imginfo.GetImageInfo('prodpicture', self.prodpicture)
            #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.prodpicture

        self.ProdPicture.SetBitmap(self.fgimage)

    def OnProdPicturePress(self, event):
        self.newprodpicture = self.imginfo.GetNewImageFile()
        if self.newprodpicture != '':
            self.ProdPicture.SetBitmap(wx.NullBitmap)
            self.fgimagefilename, self.fgimage, self.fgimagesize = \
                                  self.imginfo.GetImageInfo('prodpicture', self.newprodpicture)
            print self.fgimagefilename, self.fgimage, self.fgimagesize, self.newprodpicture
            self.ProdPicture.SetBitmap(self.fgimage)

        return

    def InsertProductInfo(self, prodinfo):
        self.prodid, sntext, nametext, spectext, listprice, saleprice = prodinfo
        self.SNText.SetValue(u'%s'%sntext)
        self.NameText.SetValue(u'%s'%nametext)
        self.SpecText.SetValue(u'%s'%spectext)
        self.ListPriceText.SetValue(u'%s'%listprice)
        self.SalePriceText.SetValue(u'%s'%saleprice)

        return

    def OnAddButton(self, event):
        sntext = self.SNText.GetValue()
        nametext = self.NameText.GetValue()
        spectext = self.SpecText.GetValue()
        listprice = self.ListPriceText.GetValue()
        saleprice = self.SalePriceText.GetValue()

        print 'Product Information:  '
        print sntext, nametext, spectext, listprice, saleprice
        if self.action == 'add':
            sqlaction = 'insert'
            sqlcmd  = '''INSERT INTO %s '''%(self.prodtable, )
            sqlcmd += '''   (
                            Product_SerialNo, Product_Name, Product_Spec,
                            Product_ListPrice, Product_SalePrice
                            )
                        VALUES (
                            '%s', '%s', '%s',
                            '%s', '%s'
                            )
                    '''%(sntext, nametext, spectext, listprice, saleprice)
            addsqlcmd = ''
        elif self.action == 'modify':
            sqlaction = 'update'
            sqlcmd  = '''UPDATE %s SET '''%(self.prodtable, )
            sqlcmd += '''   
                            Product_SerialNo  ='%s', Product_Name      ='%s',
                            Product_Spec      ='%s', Product_ListPrice ='%s', 
                            Product_SalePrice ='%s'
                    '''%(sntext, nametext, spectext, listprice, saleprice)
            addsqlcmd = '''WHERE Product_ItemNo = %s '''%(self.prodid)
        sqlcmd += addsqlcmd

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
        except:
            print 'Insert into database error'
            print sqlcmd
            info = 'error'

        if info != 'error':
            if self.newprodpicture != '':
                self.newprodpicture = self.imginfo.CopyNewImageFile(self.newprodpicture, self.prodpicture)

        self.Close()
        event.Skip()

    def OnExitButton(self, event):
        self.Close()
        event.Skip()


