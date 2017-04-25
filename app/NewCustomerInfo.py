# -*- coding: utf-8 -*-
#Boa:Dialog:NewCustomerInfo

from os import path
from glob import glob
import string, re
import wx

import ConnectDB

def create(parent):
    return NewCustomerInfo(parent)

[wxID_NEWCUSTOMERINFO, wxID_BITMAPCMSMAINPAGE, 
 wxID_NEWCUSTOMERINFOPANEL1, wxID_NEWCUSTOMERINFOPAGEHEADER, 
 wxID_NEWCUSTOMERINFODEALERHEADER, wxID_NEWCUSTOMERINFODEALERTEXT, 
 wxID_NEWCUSTOMERINFOJOBLEVELHEADER, wxID_NEWCUSTOMERINFOJOBLEVELTEXT, 
 wxID_NEWCUSTOMERINFONAMEHEADER, wxID_NEWCUSTOMERINFONAMETEXT,
 wxID_NEWCUSTOMERINFOJOBTITLEHEADER, wxID_NEWCUSTOMERINFOJOBTITLETEXT,
 wxID_NEWCUSTOMERINFOSPOUSEHEADER, wxID_NEWCUSTOMERINFOSPOUSETEXT, 
 wxID_NEWCUSTOMERINFOTELEPHONEHEADER, wxID_NEWCUSTOMERINFOTELEPHONETEXT1,
 wxID_NEWCUSTOMERINFOTELEPHONESPLITER1, wxID_NEWCUSTOMERINFOTELEPHONETEXT2,
 wxID_NEWCUSTOMERINFOTELEPHONESPLITER2, wxID_NEWCUSTOMERINFOTELEPHONETEXT3,
 wxID_NEWCUSTOMERINFOCELLPHONEHEADER, wxID_NEWCUSTOMERINFOCELLPHONETEXT1,
 wxID_NEWCUSTOMERINFOCELLPHONESPLITER1, wxID_NEWCUSTOMERINFOCELLPHONETEXT2,
 wxID_NEWCUSTOMERINFOAREAHEADER, wxID_NEWCUSTOMERINFOAREATEXT, 
 wxID_NEWCUSTOMERINFOADDRESSHEADER, wxID_NEWCUSTOMERINFOADDRESSTEXT, 
 wxID_NEWCUSTOMERINFOBIRTHDAYHEADER, wxID_NEWCUSTOMERINFOBIRTHDAYTEXT, 
 wxID_NEWCUSTOMERINFOMAILHEADER, wxID_NEWCUSTOMERINFOMAILTEXT, 
 wxID_NEWCUSTOMERINFORECOMMENDEDHEADER, wxID_NEWCUSTOMERINFORECOMMENDEDTEXT, 
 wxID_NEWCUSTOMERINFOADDBUTTON, wxID_NEWCUSTOMERINFOEXITBUTTON,
 wxID_NEWCUSTOMERINFOBIRTHDAYYEARTEXT, wxID_NEWCUSTOMERINFOBIRTHDAYYEARHEADER,
 wxID_NEWCUSTOMERINFOBIRTHDAYMONTHTEXT, wxID_NEWCUSTOMERINFOBIRTHDAYMONTHHEADER,
 wxID_NEWCUSTOMERINFOBIRTHDAYDAYTEXT, wxID_NEWCUSTOMERINFOBIRTHDAYDAYHEADER,
 wxID_BITMAPCUSTPICTURE, wxID_CMSMAINDIALOGWARNINGTEXT, 
] = [wx.NewId() for _init_ctrls in range(44)]

class NewCustomerInfo(wx.Dialog):
    def _init_ctrls(self, prnt, title, joblist, yearlist, monthlist, daylist):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_NEWCUSTOMERINFO,
              name='NewCustomerInfo', parent=prnt, pos=wx.Point(453, 154),
              size=self.mainwin, style=wx.DEFAULT_DIALOG_STYLE | wx.CAPTION | wx.THICK_FRAME,
              title=title)
        self.SetClientSize(self.mainwin)

        self.panel1 = wx.Panel(id=wxID_NEWCUSTOMERINFOPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.panel1,
              pos=wx.Point(0, 0), size=self.mainpagesize, style=wx.TAB_TRAVERSAL)

        #header_x = self.mainwin[0] / 2 - 75
        header_x = 20
        header_y = 20
        self.PageHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOPAGEHEADER,
              label=title, name='PageHeader', parent=self.CMSMainPage,
              pos=wx.Point(header_x, header_y), size=wx.Size(150, 40),
              style=wx.ALIGN_CENTER)
        self.PageHeader.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        split_x_1 = 20
        col2_extend = 150
        dealerlabel = u'%s：'%self.CustomerHeaderList[0]
        self.DealerHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFODEALERHEADER,
              label=dealerlabel, name='DealerHeader',
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 80), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.DealerHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.DealerText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFODEALERTEXT,
              name='DealerText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 80),
              size=wx.Size(150, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.DealerText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        ### Customer Head Picture
        custpicture_x = split_x_1 + col2_extend + 170
        custpicture_y = 20
        self.CustPicture = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_BITMAPCUSTPICTURE, name='BitmapCustPicture', parent=self.CMSMainPage,
              pos=wx.Point(custpicture_x, custpicture_y), size=self.fgimagesize, 
              style=wx.BU_AUTODRAW)

        joblevellabel = u'%s：'%self.CustomerHeaderList[1]
        self.JobLevelHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOJOBLEVELHEADER,
              label=joblevellabel, name='JobLevelHeader',
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 120), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.JobLevelHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.JobLevelText = wx.Choice(choices=joblist,
              id=wxID_NEWCUSTOMERINFOJOBLEVELTEXT, name='JobLevelText',
              parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 120),
              size=wx.Size(150, 25), style=0)
        self.JobLevelText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        namelabel = u'%s：'%self.CustomerHeaderList[2]
        self.NameHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFONAMEHEADER,
              label=namelabel, name='NameHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 160), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.NameHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.NameText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFONAMETEXT,
              name='NameText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 160),
              size=wx.Size(150, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.NameText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        spouselabel = u'%s：'%self.CustomerHeaderList[3]
        self.SpouseHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOSPOUSEHEADER,
              label=spouselabel, name='SpouseHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 200), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.SpouseHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.SpouseText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOSPOUSETEXT,
              name='SpouseText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 200),
              size=wx.Size(150, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.SpouseText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        birthdaylabel = u'%s：'%self.CustomerHeaderList[4]
        self.BirthdayHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOBIRTHDAYHEADER,
              label=birthdaylabel, name='BirthdayHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 240), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.BirthdayHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        yeartext_x = split_x_1 + col2_extend
        self.BirthdayYearText = wx.Choice(choices=yearlist,
              id=wxID_NEWCUSTOMERINFOBIRTHDAYYEARTEXT, name='BirthdayYearText',
              parent=self.CMSMainPage, pos=wx.Point(yeartext_x, 240), size=wx.Size(80, 25),
              style=0)
        self.BirthdayYearText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        yearheader_x = yeartext_x + 82
        self.BirthdayYearHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOBIRTHDAYYEARHEADER,
              label=u'年', name='BirthdayYearHeader', 
              parent=self.CMSMainPage, pos=wx.Point(yearheader_x, 240), size=wx.Size(30, 25),
              style=wx.ALIGN_CENTRE)
        self.BirthdayYearHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        monthtext_x = yearheader_x + 32
        self.BirthdayMonthText = wx.Choice(choices=monthlist,
              id=wxID_NEWCUSTOMERINFOBIRTHDAYMONTHTEXT, name='BirthdayMonthText',
              parent=self.CMSMainPage, pos=wx.Point(monthtext_x, 240), size=wx.Size(80, 25),
              style=0)
        self.BirthdayMonthText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        monthheader_x = monthtext_x + 82
        self.BirthdayMonthHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOBIRTHDAYMONTHHEADER,
              label=u'月', name='BirthdayMonthHeader', 
              parent=self.CMSMainPage, pos=wx.Point(monthheader_x, 240), size=wx.Size(30, 25),
              style=wx.ALIGN_CENTRE)
        self.BirthdayMonthHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        daytext_x = monthheader_x + 32
        self.BirthdayDayText = wx.Choice(choices=daylist,
              id=wxID_NEWCUSTOMERINFOBIRTHDAYDAYTEXT, name='BirthdayDayText',
              parent=self.CMSMainPage, pos=wx.Point(daytext_x, 240), size=wx.Size(80, 25),
              style=0)
        self.BirthdayDayText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        dayheader_x = daytext_x + 82
        self.BirthdayDayHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOBIRTHDAYDAYHEADER,
              label=u'日', name='BirthdayDayHeader', 
              parent=self.CMSMainPage, pos=wx.Point(dayheader_x, 240), size=wx.Size(30, 25),
              style=wx.ALIGN_CENTRE)
        self.BirthdayDayHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        jobtitlelabel = u'%s：'%self.CustomerHeaderList[5]
        self.JobtitleHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOJOBTITLEHEADER,
              label=jobtitlelabel, name='JobtitleHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 280), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.JobtitleHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.JobtitleText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOJOBTITLETEXT,
              name='JobtitleText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 280),
              size=wx.Size(200, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.JobtitleText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        tellabel = u'%s：'%self.CustomerHeaderList[6]
        self.TelephoneHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOTELEPHONEHEADER,
              label=tellabel, name='TelephoneHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 320), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.TelephoneHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        teltext1_x = split_x_1 + col2_extend
        self.TelephoneText1 = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOTELEPHONETEXT1,
              name='TelephoneText1', parent=self.CMSMainPage, pos=wx.Point(teltext1_x, 320),
              size=wx.Size(60, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.TelephoneText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        telspliter1_x = teltext1_x + 62
        self.TelephoneSpliter1 = wx.StaticText(id=wxID_NEWCUSTOMERINFOTELEPHONESPLITER1,
              label=u'－', name='TelephoneSpliter1', 
              parent=self.CMSMainPage, pos=wx.Point(telspliter1_x, 320), size=wx.Size(20, 25),
              style=wx.ALIGN_CENTRE)
        self.TelephoneSpliter1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        teltext2_x = telspliter1_x + 22
        self.TelephoneText2 = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOTELEPHONETEXT2,
              name='TelephoneText2', parent=self.CMSMainPage, pos=wx.Point(teltext2_x, 320),
              size=wx.Size(150, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.TelephoneText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        telspliter2_x = teltext2_x + 152
        self.TelephoneSpliter2 = wx.StaticText(id=wxID_NEWCUSTOMERINFOTELEPHONESPLITER2,
              label=u'分機', name='TelephoneSpliter2', 
              parent=self.CMSMainPage, pos=wx.Point(telspliter2_x, 320), size=wx.Size(60, 25),
              style=wx.ALIGN_CENTRE)
        self.TelephoneSpliter2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))
 
        teltext3_x = telspliter2_x + 62
        self.TelephoneText3 = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOTELEPHONETEXT3,
              name='TelephoneText3', parent=self.CMSMainPage, pos=wx.Point(teltext3_x, 320),
              size=wx.Size(70, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.TelephoneText3.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        celllabel = u'%s：'%self.CustomerHeaderList[7]
        self.CellphoneHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOCELLPHONEHEADER,
              label=celllabel, name='CellphoneHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 360), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.CellphoneHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        celltext1_x = split_x_1 + col2_extend
        self.CellphoneText1 = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOCELLPHONETEXT1,
              name='CellphoneText1', parent=self.CMSMainPage, pos=wx.Point(celltext1_x, 360),
              size=wx.Size(60, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.CellphoneText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        cellspliter1_x = celltext1_x + 62
        self.CellphoneSpliter1 = wx.StaticText(id=wxID_NEWCUSTOMERINFOCELLPHONESPLITER1,
              label=u'－', name='CellphoneSpliter1', 
              parent=self.CMSMainPage, pos=wx.Point(cellspliter1_x, 360), size=wx.Size(20, 25),
              style=wx.ALIGN_CENTRE)
        self.CellphoneSpliter1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        celltext2_x = cellspliter1_x + 22
        self.CellphoneText2 = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOCELLPHONETEXT2,
              name='CellphoneText2', parent=self.CMSMainPage, pos=wx.Point(celltext2_x, 360),
              size=wx.Size(150, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.CellphoneText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        arealabel = u'%s：'%self.CustomerHeaderList[8]
        self.AreaHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOAREAHEADER,
              label=arealabel, name='AreaHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 400), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.AreaHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.AreaText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOAREATEXT,
              name='AreaText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 400),
              size=wx.Size(150, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.AreaText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        addresslabel = u'%s：'%self.CustomerHeaderList[9]
        self.AddressHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOADDRESSHEADER,
              label=addresslabel, name='AddressHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 440), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.AddressHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        #address_size = self.mainwin[0] - 40 - 150
        address_size = 500
        self.AddressText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOADDRESSTEXT,
              name='AddressText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 440),
              size=wx.Size(address_size, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.AddressText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        maillabel = u'%s：'%self.CustomerHeaderList[10]
        self.MailHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFOMAILHEADER,
              label=maillabel, name='MailHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 480), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.MailHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.MailText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFOMAILTEXT,
              name='MailText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 480),
              size=wx.Size(350, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.MailText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        recommendedlabel = u'%s：'%self.CustomerHeaderList[11]
        self.RecommendedHeader = wx.StaticText(id=wxID_NEWCUSTOMERINFORECOMMENDEDHEADER,
              label=recommendedlabel, name='RecommendedHeader', 
              parent=self.CMSMainPage, pos=wx.Point(split_x_1, 520), size=wx.Size(140, 25),
              style=wx.ALIGN_CENTRE)
        self.RecommendedHeader.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        self.RecommendedText = wx.TextCtrl(id=wxID_NEWCUSTOMERINFORECOMMENDEDTEXT,
              name='RecommendedText', parent=self.CMSMainPage, pos=wx.Point(split_x_1 + col2_extend, 520),
              size=wx.Size(150, 25), style=wx.TE_PROCESS_ENTER | wx.TE_RICH, value='')
        self.RecommendedText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        add_x = 100
        add_y = 550
        self.AddButton = wx.Button(id=wxID_NEWCUSTOMERINFOADDBUTTON,
              label=u'確認', name='AddButton', parent=self.CMSMainPage,
              pos=wx.Point(add_x, add_y), size=wx.Size(80, 30), style=0)
        self.AddButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'新細明體'))

        exit_x = add_x + 140
        exit_y = add_y
        self.ExitButton = wx.Button(id=wxID_NEWCUSTOMERINFOEXITBUTTON,
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

    def __init__(self, parent, membertype, mainwin, title, mainpagefile, mainpage, mainpagesize, custpicturefile, currentItem, imagedir, imginfo, dbname, custtable, warntext, CustomerHeaderList, joblist, yearlist, monthlist, daylist, action, userinfo):
        self.custpicture = ''
        self.newcustpicture = ''
        self.userid = ''

        self.parent = parent
        self.membertype = membertype
        self.mainwin = mainwin
        self.title = title
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.custpicturefile = custpicturefile
        self.currentItem = currentItem
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.dbname = dbname
        self.custtable = custtable
        self.warntext = warntext
        self.CustomerHeaderList = CustomerHeaderList
        self.action = action
        self.userinfo = userinfo

        self.joblist = joblist
        self.yearlist = yearlist
        self.monthlist = monthlist
        self.daylist = daylist

        self.fgimagefilename, self.fgimage, self.fgimagesize = \
                              self.imginfo.GetImageInfo('custpicture', self.custpicturefile)
        #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.custpicturefile

        self._init_ctrls(parent, title, self.joblist, self.yearlist, self.monthlist, self.daylist)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnAddButton,  self.AddButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton, self.ExitButton)
        self.Bind(wx.EVT_BUTTON, self.OnCustPicturePress, self.CustPicture)
        self.Bind(wx.EVT_TEXT, self.ChkCustTelValue1, self.TelephoneText1)
        self.Bind(wx.EVT_TEXT, self.ChkCustTelValue2, self.TelephoneText2)
        self.Bind(wx.EVT_TEXT, self.ChkCustTelValue3, self.TelephoneText3)
        self.Bind(wx.EVT_TEXT, self.ChkCustCellValue1, self.CellphoneText1)
        self.Bind(wx.EVT_TEXT, self.ChkCustCellValue2, self.CellphoneText2)
        self.SetEscapeId(wxID_NEWCUSTOMERINFOEXITBUTTON)
        self.JobLevelText.SetSelection(0)
        self.BirthdayYearText.SetSelection(0)
        self.BirthdayMonthText.SetSelection(0)
        self.BirthdayDayText.SetSelection(0)
        self.DealerText.SetFocus()

        if self.membertype == 'Member':
            pass
        elif self.membertype == 'Nonmember':
            self.DealerHeader.Hide()
            self.DealerText.Hide()
            self.JobLevelHeader.Hide()
            self.JobLevelText.Hide()

        if self.action == 'modify' and self.userinfo:
            self.InsertUserInfo(self.userinfo)
            userid_pic = string.zfill(self.userinfo[0], 6)
            listpictures = glob('%s/%s.*'%(self.imagedir, userid_pic))
            if listpictures:
                self.custpicture = listpictures[0]
                if path.isfile(self.custpicture):
                    self.fgimagefilename, self.fgimage, self.fgimagesize = \
                                          self.imginfo.GetImageInfo('custpicture', self.custpicture)
                    #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.custpicture
            else:
                self.custpicture = '%s/%s.png'%(self.imagedir, self.custpicturefile)

        self.CustPicture.SetBitmap(self.fgimage)

    def ChkCustTelValue1(self, event):
        self.TelephoneText1.SetMaxLength(2)
        chklen = len(self.TelephoneText1.GetValue())
        if chklen == 2:
            self.TelephoneText2.SetFocus()

        return

    def ChkCustTelValue2(self, event):
        areacode = self.TelephoneText1.GetValue()
        if areacode in ['02', '04']:
            maxlen = 8
        else:
            maxlen = 7

        self.TelephoneText2.SetMaxLength(maxlen)
        chklen = len(self.TelephoneText2.GetValue())
        if chklen == maxlen:
            self.TelephoneText3.SetFocus()

        return

    def ChkCustTelValue3(self, event):
        chklen = len(self.TelephoneText3.GetValue())
        if chklen == 5:
            self.CellphoneText1.SetFocus()
        self.TelephoneText3.SetMaxLength(5)

        return

    def ChkCustCellValue1(self, event):
        chklen = len(self.CellphoneText1.GetValue())
        if chklen == 4:
            self.CellphoneText2.SetFocus()
        self.CellphoneText1.SetMaxLength(4)

        return

    def ChkCustCellValue2(self, event):
        chklen = len(self.CellphoneText2.GetValue())
        if chklen == 6:
            self.AreaText.SetFocus()
        self.CellphoneText2.SetMaxLength(6)

        return

    def OnCustPicturePress(self, event):
        self.newcustpicture = self.imginfo.GetNewImageFile()
        if self.newcustpicture != '':
            self.CustPicture.SetBitmap(wx.NullBitmap)
            self.fgimagefilename, self.fgimage, self.fgimagesize = \
                                  self.imginfo.GetImageInfo('custpicture', self.newcustpicture)
            #print self.fgimagefilename, self.fgimage, self.fgimagesize, self.newcustpicture
            self.CustPicture.SetBitmap(self.fgimage)

        return

    def InsertUserInfo(self, userinfo):
        self.userid, saletype, dealer, joblevel, name, spouse, birthday, \
                jobtitle, telephone, cellphone, area, address, email, recommended = userinfo
        print self.userid
        if self.membertype == 'Member':
            self.DealerText.SetValue(dealer)
            if joblevel == '':
                self.JobLevelText.SetSelection(0)
            else:
                joblevel = int(self.joblist.index(joblevel))
                print 'Job level selection:  ', joblevel
                self.JobLevelText.SetSelection(joblevel)
        elif self.membertype == 'Nonmember':
            self.DealerText.SetValue('')
            self.JobLevelText.SetSelection(0)
        self.NameText.SetValue(name)
        self.SpouseText.SetValue(spouse)
        if birthday != '':
            birthday_year, birthday_month, birthday_day = string.split(birthday, '-')
            print birthday_year, birthday_month, birthday_day
            birthday_year = int(self.yearlist.index('%s'%int(birthday_year)))
            birthday_month = int(self.monthlist.index('%s'%int(birthday_month)))
            birthday_day = int(self.daylist.index('%s'%int(birthday_day)))
            self.BirthdayYearText.SetSelection(birthday_year)
            self.BirthdayMonthText.SetSelection(birthday_month)
            self.BirthdayDayText.SetSelection(birthday_day)
        self.JobtitleText.SetValue(jobtitle)
        if telephone != '':
            chkext = re.compile(r'-')
            if chkext.findall(telephone):
                phoneno, tel_extno = string.split(telephone, '-')
                tel_areacode = phoneno[0:2]
                tel_phoneno  = phoneno[2:]
            else:
                tel_areacode = telephone[0:2]
                tel_phoneno  = telephone[2:]
                tel_extno = ''
            self.TelephoneText1.SetValue(tel_areacode)
            self.TelephoneText2.SetValue(tel_phoneno)
            self.TelephoneText3.SetValue(tel_extno)
        if cellphone != '':
            cell_areacode, cell_phoneno = string.split(cellphone, '-')
            self.CellphoneText1.SetValue(cell_areacode)
            self.CellphoneText2.SetValue(cell_phoneno)
        self.AreaText.SetValue(area)
        self.AddressText.SetValue(address)
        self.MailText.SetValue(email)
        self.RecommendedText.SetValue(recommended)

        return

    def OnAddButton(self, event):
        print 'New'
        dealer = self.DealerText.GetValue()
        joblevel = self.JobLevelText.GetSelection()
        print 'Job level selection:  ', joblevel
        if joblevel == 0:
            joblevel = ''
        else:
            joblevel = self.joblist[joblevel]
        print joblevel
        custname = self.NameText.GetValue()
        custspouse = self.SpouseText.GetValue()
        birthday_year = self.BirthdayYearText.GetSelection()
        print 'Birthday year  selection:  ', birthday_year
        if birthday_year == 0:
            birthday_year = ''
        else:
            birthday_year = self.yearlist[birthday_year]
        birthday_month = self.BirthdayMonthText.GetSelection()
        print 'Birthday month selection:  ', birthday_month
        if birthday_month == 0:
            birthday_month = ''
        else:
            birthday_month = self.monthlist[birthday_month]
        birthday_day = self.BirthdayDayText.GetSelection()
        print 'Birthday day   selection:  ', birthday_day
        if birthday_day == 0:
            birthday_day = ''
        else:
            birthday_day = self.daylist[birthday_day]
        if birthday_year == '':
            birthday = ''
        else:
            birthday = '%s-%s-%s'%(birthday_year, string.zfill(birthday_month, 2), string.zfill(birthday_day, 2))
        jobtitle = self.JobtitleText.GetValue()
        tel_areacode = self.TelephoneText1.GetValue()
        tel_phoneno  = self.TelephoneText2.GetValue()
        tel_extno    = self.TelephoneText3.GetValue()
        if tel_areacode != '' or tel_phoneno != '':
            if tel_extno != '':
                telephone = '%s%s-%s'%(tel_areacode, tel_phoneno, tel_extno)
            else:
                telephone = '%s%s'%(tel_areacode, tel_phoneno)
        else:
            telephone = ''
        cell_areacode = self.CellphoneText1.GetValue()
        cell_phoneno  = self.CellphoneText2.GetValue()
        if cell_areacode != '' or cell_phoneno != '':
            cellphone = '%s-%s'%(cell_areacode, cell_phoneno)
        else:
            cellphone = ''
        area = self.AreaText.GetValue()
        address = self.AddressText.GetValue()
        email = self.MailText.GetValue()
        recommended = self.RecommendedText.GetValue()

        print 'User Information:  '
        print dealer, joblevel, custname, custspouse, birthday, jobtitle, telephone, cellphone, area, address, email, recommended
        if self.action == 'add':
            sqlaction = 'insert'
            sqlcmd  = '''INSERT INTO %s '''%(self.custtable, )
            sqlcmd += '''   (
                            Customer_SaleType, Customer_Dealer, Customer_JobLevel,
                            Customer_Name, Customer_Spouse, Customer_Birthday,
                            Customer_JobTitle, Customer_Telephone, Customer_Cellphone,
                            Customer_Area, Customer_Address, Customer_Email,
                            Customer_Recommended
                            )
                        VALUES (
                            '%s', '%s', '%s',
                            '%s', '%s', '%s',
                            '%s', '%s', '%s',
                            '%s', '%s', '%s',
                            '%s'
                            )
                    '''%(self.membertype, dealer, joblevel, custname, custspouse, birthday, jobtitle, telephone, cellphone, area, address, email, recommended)
            addsqlcmd = ''
        elif self.action == 'modify':
            sqlaction = 'update'
            sqlcmd  = '''UPDATE %s SET '''%(self.custtable, )
            sqlcmd += '''   
                            Customer_SaleType   ='%s', Customer_Dealer   ='%s',
                            Customer_JobLevel   ='%s', Customer_Name     ='%s',
                            Customer_Spouse     ='%s', Customer_Birthday ='%s',
                            Customer_JobTitle   ='%s', Customer_Telephone='%s',
                            Customer_Cellphone  ='%s', Customer_Area     ='%s', 
                            Customer_Address    ='%s', Customer_Email    ='%s',
                            Customer_Recommended='%s'
                    '''%(self.membertype, dealer, joblevel, custname, custspouse, birthday, jobtitle, telephone, cellphone, area, address, email, recommended)
            addsqlcmd = '''WHERE Customer_ItemNo = %s '''%(self.userid)
        sqlcmd += addsqlcmd

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
        except:
            print 'Insert into database error'
            print sqlcmd
            info = 'error'
        
        if info != 'error':
            if self.newcustpicture != '':
                if self.custpicture == '':
                    userid = self.GetNewUserId()
                    print userid
                    if userid != '':
                        userid_pic = string.zfill(userid, 6)
                        self.custpicture = '%s/%s.png'%(self.imagedir, userid_pic)
                    else:
                        self.custpicture = self.custpicturefile
                #print self.newcustpicture, self.custpicture
                self.newcustpicture = self.imginfo.CopyNewImageFile(self.newcustpicture, self.custpicture)

        self.Close()
        event.Skip()

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def GetNewUserId(self):
        userid = ''

        sqlaction = 'select'
        sqlcmd  = '''SELECT TOP 1 Customer_ItemNo
                        FROM %s
                        ORDER BY Customer_ItemNo DESC;
                '''%(self.custtable, )

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
            if info:
                userid = info[0][0]
            #print info, userid
        except:
            print 'Insert into database error'
            print sqlcmd

        return userid
