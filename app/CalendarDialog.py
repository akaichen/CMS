#Boa:Dialog:CalendarDialog

import os, sys
import string, re
import time
import wx
import wx.calendar

def create(parent):
    return CalendarDialog(parent)

[wxID_CALENDARDIALOG, wxID_CALENDARDIALOGCALENDARCTRL1, 
 wxID_CALENDARDIALOGEXITBUTTON, wxID_CALENDARDIALOGPANEL1, 
 wxID_CALENDARDIALOGSUBMITBUTTON, 
] = [wx.NewId() for _init_ctrls in range(5)]

class CalendarDialog(wx.Dialog):
    def _init_ctrls(self, prnt, currenttime):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_CALENDARDIALOG, name='CalendarDialog',
              parent=prnt, pos=wx.Point(570, 212), size=wx.Size(440, 310),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='\xbf\xef\xbe\xdc\xa4\xe9\xb4\xc1')
        self.SetClientSize(wx.Size(440, 310))

        self.panel1 = wx.Panel(id=wxID_CALENDARDIALOGPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(440, 310),
              style=wx.TAB_TRAVERSAL)

        self.calendarCtrl1 = wx.calendar.CalendarCtrl(date=currenttime,
              id=wxID_CALENDARDIALOGCALENDARCTRL1, name='calendarCtrl1',
              parent=self.panel1, pos=wx.Point(10, 10), size=wx.Size(420, 245),
              style=wx.calendar.CAL_SHOW_HOLIDAYS)
        self.calendarCtrl1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, '\xb7L\xb3n\xa5\xbf\xb6\xc2\xc5\xe9'))

        self.SubmitButton = wx.Button(id=wxID_CALENDARDIALOGSUBMITBUTTON,
              label='\xbf\xef\xbe\xdc', name='SubmitButton', parent=self.panel1,
              pos=wx.Point(50, 270), size=wx.Size(80, 30), style=0)
        self.SubmitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, '\xb7L\xb3n\xa5\xbf\xb6\xc2\xc5\xe9'))

        self.ExitButton = wx.Button(id=wxID_CALENDARDIALOGEXITBUTTON,
              label='\xc2\xf7\xb6}', name='ExitButton', parent=self.panel1,
              pos=wx.Point(230, 270), size=wx.Size(80, 30), style=0)
        self.ExitButton.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, '\xb7L\xb3n\xa5\xbf\xb6\xc2\xc5\xe9'))

    def __init__(self, parent, selectdate):
        self.parent = parent
        self.selectdate = selectdate
        Y, M, D = string.split(self.selectdate, '-')
        currenttime = wx.DateTimeFromDMY(int(D), int(M) - 1, int(Y))

        self._init_ctrls(self.parent, currenttime)
        self.Center()

        self.Bind(wx.EVT_LEFT_DCLICK, self.OnCalendarClick, self.calendarCtrl1)
        self.Bind(wx.EVT_BUTTON, self.OnSubmitButton, self.SubmitButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton, self.ExitButton)
        self.SetEscapeId(wxID_CALENDARDIALOGEXITBUTTON)

    def OnSubmitButton(self, event):
        DateSplit = string.split('%s'%self.calendarCtrl1.GetDate())
        M,D,Y = string.split(DateSplit[0], '/')
        self.selectdate = '20%s-%s-%s'%(Y, M, D)

        self.Close()
        event.Skip()

    def OnExitButton(self, event):
        self.Close()
        event.Skip()

    def OnCalendarClick(self, event):
        self.OnSubmitButton(self.SubmitButton)
        #self.Close()
        #event.Skip()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "TEST")
        frame.Show()
        self.SetTopWindow(frame)
        dlg = CalendarDialog(frame, "")
        dlg.Show()
        return True
        
def main():
    app=MyApp()
    app.MainLoop()
    
if __name__ == '__main__':
    main()