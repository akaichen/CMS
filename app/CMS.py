#!/usr/bin/env python
#Boa:App:BoaApp

from os import path, mkdir
import wx, time
#import string, re
#import decimal

import CMSMain

class BoaApp(wx.App):
    def __init__(self, parent):
        self.parent = parent
        self.workdir = '.'

        dbdir = '%s\\dbdir'%self.workdir
        if not path.isdir(dbdir):
            mkdir(dbdir)

        self.dbdata = {}
        self.dbdata['DBDIR']     = dbdir
        self.dbdata['DBNAME']    = '%s\\customerinfo.mdb'%self.dbdata['DBDIR']
        self.dbdata['CUSTTABLE'] = 'CustomerInformation'
        self.dbdata['PRODTABLE'] = 'ProductInformation'
        self.dbdata['SALETABLE'] = 'SaleInformation'

        imgdir = '%s\\imgdir'%self.workdir
        if not path.isdir(imgdir):
            mkdir(imgdir)
        custdir = '%s\\cust'%imgdir
        if not path.isdir(custdir):
            mkdir(custdir)
        proddir = '%s\\prod'%imgdir
        if not path.isdir(proddir):
            mkdir(proddir)

        self.imgdata = {}
        self.imgdata['IMGDIR'] = imgdir
        self.imgdata['MAIN']               = {}
        self.imgdata['MAIN']['FILENAME']   = '%s\\mainpage.png'%self.imgdata['IMGDIR']
        self.imgdata['MAIN']['WIDTH']      = 1024
        self.imgdata['MAIN']['HEIGHT']     = 650
        self.imgdata['MAIN']['CSFILENAME'] = '%s\\mainpage-cs.png'%self.imgdata['IMGDIR']
        self.imgdata['CUST']               = {}
        self.imgdata['CUST']['FILENAME']   = '%s\\custpicture.png'%self.imgdata['IMGDIR']
        self.imgdata['CUST']['WIDTH']      = 200
        self.imgdata['CUST']['HEIGHT']     = 200
        self.imgdata['CUST']['CUSTDIR']    = custdir
        self.imgdata['PROD']               = {}
        self.imgdata['PROD']['FILENAME']   = '%s\\prodpicture.png'%self.imgdata['IMGDIR']
        self.imgdata['PROD']['WIDTH']      = 300
        self.imgdata['PROD']['HEIGHT']     = 300
        self.imgdata['PROD']['PRODDIR']    = proddir

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