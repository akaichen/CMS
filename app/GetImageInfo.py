# -*- coding: utf-8 -*-

from os import path
import re
import wx
from Tkinter import Tk
from tkFileDialog import askopenfilename
#from shutil import copyfile
from PIL import Image

class GetImageInfo:
    #def __init__(self, imagedir, picwidth, picheight, maxwidth, maxheight):
    def __init__(self, imgdata):
        self.imgdata    = imgdata
        self.imagedir   = self.imgdata['IMGDIR']
        self.maxwidth   = self.imgdata['MAIN']['WIDTH']
        self.maxheight  = self.imgdata['MAIN']['HEIGHT']
        self.picwidth   = self.imgdata['CUST']['WIDTH']
        self.picheight  = self.imgdata['CUST']['HEIGHT']
        self.prodwidth  = self.imgdata['PROD']['WIDTH']
        self.prodheight = self.imgdata['PROD']['HEIGHT']

    def GetImageInfo(self, imagetype, image_file):
        if imagetype == 'mainpage':
            if image_file == '':
                image_file = 'mainpage.png'
        elif imagetype == 'custpicture':
            if image_file == '':
                image_file = 'custpicture.png'
        elif imagetype == 'prodpicture':
            if image_file == '':
                image_file = 'prodpicture.png'
        #else:
        #    if image_file == '':
        #        image_file = 'mainpage.png'

        if not path.isfile(image_file):
            image_file = '%s\\%s'%(self.imagedir, image_file)
        if not path.isfile(image_file):
            image_file = '..\\windows_dll\\%s'%image_file

        openimage, imagefile, imagesize = self.ImageInfo(imagetype, image_file)

        return openimage, imagefile, imagesize

    def ImageInfo(self, imagetype, image_file):
        if re.compile(r'\.png').findall(image_file):
            image = wx.Image(image_file, wx.BITMAP_TYPE_PNG)
        elif re.compile(r'\.gif').findall(image_file):
            image = wx.Image(image_file, wx.BITMAP_TYPE_GIF)
        elif re.compile(r'\.jpg').findall(image_file) or re.compile(r'\.jpeg').findall(image_file):
            image = wx.Image(image_file, wx.BITMAP_TYPE_JPEG)
        elif re.compile(r'\.tif').findall(image_file):
            image = wx.Image(image_file, wx.BITMAP_TYPE_TIF)
        else:
            image = wx.Image(image_file, wx.BITMAP_TYPE_ANY)

        ### Get image size
        imagefile   = image.ConvertToBitmap()
        imagewidth  = imagefile.GetWidth() 
        imageheight = imagefile.GetHeight()
        imagesize   = imagewidth, imageheight
        if imagetype in ['', 'mainpage']:
            maxwidth = self.maxwidth
            maxheight = self.maxheight            
        elif imagetype == 'custpicture':
            maxwidth = self.picwidth
            maxheight = self.picheight
        elif imagetype == 'prodpicture':
            maxwidth = self.prodwidth
            maxheight = self.prodheight

        #print 'org:  ', imagewidth, imageheight
        #print 'max:  ', maxwidth, maxheight
        if 1:
            if imagewidth <= imageheight:
                #if imageheight < maxheight:
                if 1:
                    newimage = wx.ImageFromBitmap(imagefile)
                    new_height = maxheight
                    new_width = ( float(maxheight) / imageheight ) * imagewidth
                    imagesize = new_width, new_height
                    #print imagewidth, imageheight
                    #print new_width, new_height
                    newimage = newimage.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
                    imagefile = wx.BitmapFromImage(newimage)
                    imagesize = maxwidth, maxheight
                else:
                    imagesize = maxwidth, maxheight
            else:
                imagewidth, imageheight = imagesize
                #if imageheight < maxwidth:
                if 1:
                    newimage = wx.ImageFromBitmap(imagefile)
                    new_width = maxwidth
                    new_height = ( float(maxwidth) / imagewidth ) * imageheight
                    #new_height = maxheight
                    #new_width = ( float(maxheight) / imageheight ) * imagewidth
                    imagesize = new_width, new_height
                    #print imagewidth, imageheight
                    #print new_width, new_height
                    newimage = newimage.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
                    imagefile = wx.BitmapFromImage(newimage)
                    imagesize = maxwidth, maxheight
                else:
                    imagesize = maxwidth, maxheight

        return image_file, imagefile, imagesize

    def GetNewImageFile(self):
        # we don't want a full GUI, so keep the root window from appearing
        # show an "Open" dialog box and return the path to the selected file
        Tk().withdraw()
        selectfilename = askopenfilename(initialdir = self.imagedir, title = "Select Picture",
                                   filetypes = (("JPEG files", "*.jpg"),
                                                ("PNG files", "*.png"),
                                                ("All files", "*.*"))
                                   )
        #print selectfilename

        return selectfilename

    def CopyNewImageFile(self, orgfilename, newfilename):
        openimage = Image.open(orgfilename)
        filename, fileext = path.splitext(orgfilename)
        newfilename, newfileext = path.splitext(newfilename)
        print filename, fileext, newfilename, newfileext
        savefilename = '%s%s'%(newfilename, fileext)
        saveimage = openimage.save(savefilename)
        #saveimage = openimage.save(newfilename, 'PNG')
        #newfilename = '%s/aaa.png'%self.imagedir
        #copyfile(filename, newfilename)
        #print u'Copy from %s to %s'%(repr(filename), repr(newfilename))

        return newfilename

    def GetCustImageDir(self):
        custimgdir = self.imgdata['CUST']['CUSTDIR']

        return custimgdir

    def GetProdImageDir(self):
        prodimgdir = self.imgdata['PROD']['PRODDIR']

        return prodimgdir
