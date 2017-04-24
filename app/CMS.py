#!/usr/bin/env python
#Boa:App:BoaApp

import os
import wx, time
#import string, re
#import decimal

import CMSMain

class BoaApp(wx.App):
    def __init__(self, parent):
        self.parent = parent
        #self.workdir = os.getcwd()
        self.workdir = '.'
        self.imagedir = '%s\\imgdir'%self.workdir
        self.dbdir = '%s\\dbdir'%self.workdir
        #self.dbdir = '.\\dbdir'
        self.mainpagefile = '%s\\mainpage.png'%self.imagedir
        self.csmainpagefile = '%s\\mainpage-cs.png'%self.imagedir
        self.custpicturefile = '%s\\custpicture.png'%self.imagedir
        self.dbfilename = 'customerinfo.mdb'
        self.tablename = 'CustomerInformation'
        self.maxwidth  = 1024
        self.maxheight = 650
        self.picwidth  = 200
        self.picheight = 200

    def Start(self):
        mainsystem = CMSMain.CMSMainDialog(self.parent, self.workdir, self.imagedir, self.dbdir, self.mainpagefile, 
                                           self.csmainpagefile, self.custpicturefile, self.picwidth, self.picheight, 
                                           self.dbfilename, self.tablename, self.maxwidth, self.maxheight)
        mainsystem.SetIcon(wx.Icon(self.mainpagefile, wx.BITMAP_TYPE_PNG))
        try:
            mainsystem.ShowModal()
        finally:
            mainsystem.Destroy()

def main():
    #app = wx.PySimpleApp()
    app = wx.App(False)
    mainApp = BoaApp(None)
    mainApp.Start()
    app.MainLoop()

if __name__ == '__main__':
    main()