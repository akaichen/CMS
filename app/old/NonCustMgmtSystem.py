#Boa:Dialog:NonCustMgmtSystem

import wx
import wx.lib.buttons

import NewCustomerInfo

def create(parent):
    return NonCustMgmtSystem(parent)

[wxID_NONCUSTMGMTSYSTEM, wxID_NONCUSTMGMTSYSTEMEXITBUTTON, 
 wxID_NONCUSTMGMTSYSTEMNEWCUSTOMER, wxID_NONCUSTMGMTSYSTEMMODIFYCUSTOMER, 
 wxID_NONCUSTMGMTSYSTEMGENQUERYCUSTOMER, wxID_NONCUSTMGMTSYSTEMCUSTLIST, 
 wxID_NONCUSTMGMTSYSTEMPANEL1, wxID_BITMAPCMSMAINPAGE,
] = [wx.NewId() for _init_ctrls in range(8)]

class NonCustMgmtSystem(wx.Dialog):
    def _init_ctrls(self, prnt, title, mainwin):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_NONCUSTMGMTSYSTEM, name='NonCustMgmtSystem',
              parent=prnt, pos=wx.Point(314, 167), size=mainwin,
              style=wx.DEFAULT_DIALOG_STYLE, title=title)
        self.SetClientSize(mainwin)

        self.panel1 = wx.Panel(id=wxID_NONCUSTMGMTSYSTEMPANEL1, name='panel1',
              parent=self, pos=wx.Point(8, 8), size=mainwin,
              style=wx.TAB_TRAVERSAL)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self.panel1,
              pos=wx.Point(0, 0), size=self.mainpagesize, style=0)

        self.NewCustomer = wx.lib.buttons.GenButton(id=wxID_NONCUSTMGMTSYSTEMNEWCUSTOMER,
              label='\xb7s\xbcW', name='NewCustomer', parent=self.CMSMainPage,
              pos=wx.Point(20, 20), size=wx.Size(80, 30), style=0)
        self.NewCustomer.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        self.ModifyCustomer = wx.lib.buttons.GenButton(id=wxID_NONCUSTMGMTSYSTEMMODIFYCUSTOMER,
              label='\xbds\xbf\xe8', name='ModifyCustomer', parent=self.CMSMainPage,
              pos=wx.Point(120, 20), size=wx.Size(80, 30), style=0)
        self.ModifyCustomer.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        self.QueryCustomer = wx.lib.buttons.GenButton(id=wxID_NONCUSTMGMTSYSTEMGENQUERYCUSTOMER,
              label='\xacd\xb8\xdf', name='QueryCustomer', parent=self.CMSMainPage,
              pos=wx.Point(220, 20), size=wx.Size(80, 30), style=0)
        self.QueryCustomer.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        custlist_x = mainwin[0] - 40
        custlist_y = mainwin[1] - 40 - 50 - 50
        self.CustList = wx.ListCtrl(id=wxID_NONCUSTMGMTSYSTEMCUSTLIST,
              name='CustList', parent=self.CMSMainPage, pos=wx.Point(20, 70),
              size=wx.Size(custlist_x, custlist_y), style=wx.LC_ICON)
        self.CustList.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

        exit_x = mainwin[0] / 2 - 40
        exit_y = mainwin[1] - 50
        self.ExitButton = wx.Button(id=wxID_NONCUSTMGMTSYSTEMEXITBUTTON, label='\xc2\xf7\xb6}',
              name='ExitButton', parent=self.CMSMainPage, pos=wx.Point(exit_x, exit_y),
              size=wx.Size(80, 30), style=0)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xb7s\xb2\xd3\xa9\xfa\xc5\xe9'))

    def __init__(self, parent, mainwin, mainpagefile, mainpage, mainpagesize, custpicturefile, custpicture, custpicturesize, imagedir, imginfo):
        title = '\xabD\xb7|\xad\xfb\xa4\xce\xae\xf8\xb6O\xaa\xcc\xba\xde\xb2z\xa8t\xb2\xce'
        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.custpicturefile = custpicturefile
        self.custpicture = custpicture
        self.custpicturesize = custpicturesize
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.currentItem = -1

        self._init_ctrls(parent, title, mainwin)
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.OnNewCustomer,    self.NewCustomer)
        self.Bind(wx.EVT_BUTTON, self.OnModifyCustomer, self.ModifyCustomer)
        self.Bind(wx.EVT_BUTTON, self.OnQueryCustomer,  self.QueryCustomer)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton,     self.ExitButton)
        self.SetEscapeId(wxID_NONCUSTMGMTSYSTEMEXITBUTTON)
        self.NewCustomer.SetFocus()

    def OnNewCustomer(self, event):
        addtype = 'customer'
        action = 'add'
        dlg = NewCustomerInfo.NewCustomerInfo(self.parent, self.mainwin, self.mainpagefile, self.mainpage,
                                              self.mainpagesize, self.custpicturefile, self.custpicture,
                                              self.custpicturesize, self.currentItem, self.imagedir, self.imginfo,
                                              addtype, action)
        dlg.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnModifyCustomer(self, event):
        self.OnItemSelect(self.CustList)
        addtype = 'customer'
        action = 'modify'
        dlg = NewCustomerInfo.NewCustomerInfo(self.parent, self.mainwin, self.mainpagefile, self.mainpage,
                                              self.mainpagesize, self.custpicturefile, self.custpicture,
                                              self.custpicturesize, self.currentItem, self.imagedir, self.imginfo,
                                              addtype, action)
        dlg.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnQueryCustomer(self, event):
        print 'Query Customer'

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def onItemSelect(self, event):
        self.currentItem = self.CustList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)

        return
