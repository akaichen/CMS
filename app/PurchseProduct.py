# -*- coding: utf-8 -*-
#Boa:Dialog:PurchseProduct

from os import path
from glob import glob
from datetime import datetime
import wx

import ConnectDB

def create(parent):
    return PurchseProduct(parent)

[wxID_PURCHSEPRODUCT, 
 wxID_BITMAPCMSMAINPAGE, wxID_PURCHSEPRODUCTPAGEHEADER,
 wxID_PURCHSEPRODUCTSNHEADER, wxID_PURCHSEPRODUCTSNTEXT,
 wxID_BITMAPPRODPICTURE, wxID_PURCHSEPRODUCTNAMEHEADER,
 wxID_PURCHSEPRODUCTNAMETEXT, wxID_PURCHSEPRODUCTPURCHSEHEADER,
 wxID_PURCHSEPRODUCTPURCHSETEXT, wxID_PURCHSEPRODUCTADDBUTTON,
 wxID_PURCHSEPRODUCTEXITBUTTON, wxID_CMSMAINDIALOGWARNINGTEXT,
 wxID_PURCHSEPRODUCTSPECHEADER, wxID_PURCHSEPRODUCTSPECTEXT,
 wxID_PURCHSEPRODUCTLISTPRICEHEADER, wxID_PURCHSEPRODUCTLISTPRICETEXT,
 wxID_PURCHSEPRODUCTSALEPRICEHEADER, wxID_PURCHSEPRODUCTSALEPRICETEXT,
 wxID_PURCHSEPRODUCTTOTALPRICEHEADER, wxID_PURCHSEPRODUCTTOTALPRICETEXT,
 wxID_PURCHSEPRODUCTCUSTHEADER, wxID_PURCHSEPRODUCTCUSTTEXT,
] = [wx.NewId() for _init_ctrls in range(23)]

class PurchseProduct(wx.Dialog):
    def _init_ctrls(self, prnt, title, prodlist):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PURCHSEPRODUCT, name='PurchseProduct',
              parent=prnt, pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=title)
        self.SetClientSize(self.mainwin)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self,
              pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.ALIGN_CENTRE|wx.TAB_TRAVERSAL)

        header_x = 20
        header_y = 20
        self.PageHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTPAGEHEADER,
              label=title, name='PageHeader', parent=self.CMSMainPage,
              pos=wx.Point(header_x, header_y), size=wx.Size(250, 40),
              style=wx.ALIGN_CENTER)
        self.PageHeader.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        split_x_1 = 20
        col2_extend = 150
        custlabel = u'%s'%self.CustomerHeaderList[2]
        self.CustHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTCUSTHEADER,
              label=custlabel, name='CustHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 80), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.CustHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.CustText = wx.TextCtrl(id=wxID_PURCHSEPRODUCTCUSTTEXT,
              name='NameText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 80),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.CustText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        snlabel = u'%s'%self.ProductHeaderList[0]
        self.SNHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTSNHEADER,
              label=snlabel, name='SNHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 120), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.SNHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.SNText = wx.Choice(choices=prodlist,
              id=wxID_PURCHSEPRODUCTSNTEXT, name='SNText',
              parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 120),
              size=wx.Size(200, 25), style=0)
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
        self.NameHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTNAMEHEADER,
              label=namelabel, name='NameHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 160), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.NameHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.NameText = wx.TextCtrl(id=wxID_PURCHSEPRODUCTNAMETEXT,
              name='NameText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 160),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.NameText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        speclabel = u'%s'%self.ProductHeaderList[2]
        self.SpecHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTSPECHEADER,
              label=speclabel, name='SpecHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 200), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.SpecHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.SpecText = wx.TextCtrl(id=wxID_PURCHSEPRODUCTSPECTEXT,
              name='SpecText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 200),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.SpecText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        '''
        listpricelabel = u'%s'%self.ProductHeaderList[3]
        self.ListPriceHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTLISTPRICEHEADER,
              label=listpricelabel, name='ListPriceHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 220), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.ListPriceHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.ListPriceText = wx.TextCtrl(id=wxID_PURCHSEPRODUCTLISTPRICETEXT,
              name='ListPriceText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 220),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.ListPriceText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))
        '''

        salepricelabel = u'%s'%self.ProductHeaderList[4]
        self.SalePriceHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTSALEPRICEHEADER,
              label=salepricelabel, name='SalePriceHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 240), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.SalePriceHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.SalePriceText = wx.TextCtrl(id=wxID_PURCHSEPRODUCTSALEPRICETEXT,
              name='SalePriceText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 240),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.SalePriceText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        purchselabel = u'購買數量'
        self.PurchseHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTPURCHSEHEADER,
              label=purchselabel, name='PurchseHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 280), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.PurchseHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.PurchseText = wx.TextCtrl(id=wxID_PURCHSEPRODUCTPURCHSETEXT,
              name='PurchseText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 280),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.PurchseText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        totalpricelabel = u'購買總價'
        self.TotalPriceHeader = wx.StaticText(id=wxID_PURCHSEPRODUCTTOTALPRICEHEADER,
              label=totalpricelabel, name='TotalPriceHeader', parent=self.CMSMainPage,
              pos=wx.Point(split_x_1, 320), size=wx.Size(140, 25), 
              style=wx.ALIGN_CENTRE)
        self.TotalPriceHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.TotalPriceText = wx.TextCtrl(id=wxID_PURCHSEPRODUCTTOTALPRICETEXT,
              name='TotalPriceText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 320),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.TotalPriceText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        add_x = 60
        add_y = 360
        self.AddButton = wx.Button(id=wxID_PURCHSEPRODUCTADDBUTTON,
              label=u'確認', name='AddButton', parent=self.CMSMainPage,
              pos=wx.Point(add_x, add_y), size=wx.Size(80, 30), style=0)
        self.AddButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        exit_x = add_x + 140
        exit_y = add_y
        self.ExitButton = wx.Button(id=wxID_PURCHSEPRODUCTEXITBUTTON,
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

    def __init__(self, parent, mainwin, purprodlabel, mainpagefile, mainpage, mainpagesize, ProductHeaderList, CustomerHeaderList, prodpicturefile, imagedir, imginfo, dbname, saletable, userinfo, allprodinfo, warntext):
        self.prodpicture = ''

        self.parent = parent
        self.mainwin = mainwin
        self.title = purprodlabel
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.ProductHeaderList = ProductHeaderList
        self.CustomerHeaderList = CustomerHeaderList
        self.prodpicturefile = prodpicturefile
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.dbname = dbname
        self.saletable = saletable
        self.userinfo = userinfo
        self.allprodinfo = allprodinfo
        self.warntext = warntext

        self.fgimagefilename, self.fgimage, self.fgimagesize, self.fgimagetype = \
                              self.imginfo.GetImageInfo('prodpicture', self.prodpicturefile)
        #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.prodpicturefile

        self.prodlist = self.allprodinfo.keys()
        self.prodlist.sort()

        self._init_ctrls(self.parent, self.title, self.prodlist)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnAddButton,  self.AddButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton, self.ExitButton)
        #self.Bind(wx.EVT_BUTTON, self.OnProdPicturePress, self.ProdPicture)
        self.Bind(wx.EVT_CHOICE, self.OnQueryProduct, self.SNText)
        self.Bind(wx.EVT_TEXT, self.TotalPriceUpdate, self.PurchseText)
        self.SetEscapeId(wxID_PURCHSEPRODUCTEXITBUTTON)

        self.SNText.SetSelection(0)

        self.InitData()

    '''
    def OnProdPicturePress(self, event):
        self.newprodpicture = self.imginfo.GetNewImageFile()
        if self.newprodpicture != '':
            self.ProdPicture.SetBitmap(wx.NullBitmap)
            self.fgimagefilename, self.fgimage, self.fgimagesize, self.fgimagetype = \
                                  self.imginfo.GetImageInfo('prodpicture', self.newprodpicture)
            #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.newprodpicture
            self.ProdPicture.SetBitmap(self.fgimage)

        return
    '''

    def TotalPriceUpdate(self, event):
        purchseno = self.PurchseText.GetValue()
        if purchseno != '':
            try:
                purchseno = int(purchseno)
            except:
                purchseno = ''

            if purchseno != '':
                saleprice = int(self.SalePriceText.GetValue())
                totalprice = saleprice * purchseno
                self.TotalPriceText.SetValue('%s'%totalprice)
                #self.TotalPriceText.SetValue('%s'%format(totalprice))
            else:
                self.TotalPriceText.SetValue('')
        else:
            self.TotalPriceText.SetValue('')

        return

    def OnAddButton(self, event):
        userid = self.userinfo[0]
        snselect = self.SNText.GetSelection()
        sntext = self.prodlist[snselect]
        nametext = self.NameText.GetValue()
        specttext = self.SpecText.GetValue()
        saleprice = self.SalePriceText.GetValue()
        purchseno = self.PurchseText.GetValue()
        totalprice = self.TotalPriceText.GetValue()
        purchsetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print 'Purchse Product Information:  '
        print userid, sntext, nametext, saleprice, purchseno, totalprice, purchsetime
        sqlaction = 'insert'
        sqlcmd  = '''INSERT INTO %s '''%(self.saletable, )
        sqlcmd += '''   (
                        Sale_CustomerId, Sale_ProductId,
                        Sale_ProductPrice, Sale_PurchseNo,
                        Sale_TotalPrice, Sale_PurchseTime
                        )
                    VALUES (
                        '%s',   '%s', '%s',
                        '%s', '%s', '%s'
                        )
                '''%(userid, sntext, saleprice, purchseno, totalprice,
                     purchsetime)

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
        except:
            print 'Insert into database error'
            print sqlcmd
            info = 'error'

        self.Close()
        event.Skip()

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def InitData(self):
        self.OnQueryProduct(self.SNText)

        return

    def OnQueryProduct(self, event):
        custname = self.userinfo[4]
        self.CustText.SetValue(custname)

        snselect = int(self.SNText.GetSelection())
        #print snselect
        sntext = self.prodlist[snselect]
        #print sntext
        nametext, spectext, listprice, saleprice = self.allprodinfo[sntext]
        self.NameText.SetValue(nametext)
        self.SpecText.SetValue(spectext)
        self.SalePriceText.SetValue(saleprice)

        prodid = sntext
        #self.prodpicture = '%s/%s.png'%(self.imagedir, prodid)
        listpictures = glob('%s/%s.*'%(self.imagedir, prodid))
        #print self.imagedir, listpictures
        if listpictures:
            self.prodpicture = listpictures[0]
            if not path.isfile(self.prodpicture):
                self.prodpicture = self.prodpicturefile
        else:
            self.prodpicture = self.prodpicturefile

        self.fgimagefilename, self.fgimage, self.fgimagesize, self.fgimagetype = \
                              self.imginfo.GetImageInfo('prodpicture', self.prodpicture)
        #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.prodpicture
        self.ProdPicture.SetBitmap(self.fgimage)

        return


