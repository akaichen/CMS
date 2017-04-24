#!/usr/bin/env python
#Boa:App:BoaApp

from os import path
import wx, time
#import string, re
#import decimal

import CMSMain

class BoaApp(wx.App):
    def __init__(self, parent):
        self.parent = parent
        self.workdir = '.'

        self.dbdata = {}
        self.dbdata['DBDIR']     = '%s\\dbdir'%self.workdir
        self.dbdata['DBNAME']    = '%s\\customerinfo.mdb'%self.dbdata['DBDIR']
        self.dbdata['CUSTTABLE'] = 'CustomerInformation'
        self.dbdata['PRODTABLE'] = 'ProductInformation'

        self.imgdata = {}
        self.imgdata['IMGDIR'] = '%s\\imgdir'%self.workdir
        self.imgdata['MAIN']               = {}
        self.imgdata['MAIN']['FILENAME']   = '%s\\mainpage.png'%self.imgdata['IMGDIR']
        self.imgdata['MAIN']['WIDTH']      = 1024
        self.imgdata['MAIN']['HEIGHT']     = 650
        self.imgdata['MAIN']['CSFILENAME'] = '%s\\mainpage-cs.png'%self.imgdata['IMGDIR']
        self.imgdata['CUST']               = {}
        self.imgdata['CUST']['FILENAME']   = '%s\\custpicture.png'%self.imgdata['IMGDIR']
        self.imgdata['CUST']['WIDTH']      = 200
        self.imgdata['CUST']['HEIGHT']     = 200
        self.imgdata['PROD']               = {}
        self.imgdata['PROD']['FILENAME']   = '%s\\prodpicture.png'%self.imgdata['IMGDIR']
        self.imgdata['PROD']['WIDTH']      = 300
        self.imgdata['PROD']['HEIGHT']     = 300

        csmainpagefile = self.imgdata['MAIN']['CSFILENAME']
        if path.isfile(csmainpagefile):
            self.iconimagefile = csmainpagefile
        else:
            self.iconimagefile = self.imgdata['MAIN']['FILENAME']

    def Start(self):
        mainsystem = CMSMain.CMSMainDialog(self.parent, self.workdir, self.dbdata, self.imgdata)
        mainsystem.SetIcon(wx.Icon(self.iconimagefile, wx.BITMAP_TYPE_PNG))
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