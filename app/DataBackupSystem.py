# -*- coding: utf-8 -*-
#Boa:Dialog:DataBackupSystem

from os import walk as oswalk
from os import path, stat, remove
import sys
from glob import glob
from datetime import datetime
from time import strftime
import zipfile

import wx
import wx.lib.buttons

import GetSysInfo
import ConnectDB

def create(parent):
    return DataBackupSystem(parent)

[wxID_DATABACKUPSYSTEM, wxID_BITMAPCMSMAINPAGE, 
 wxID_DATABACKUPSYSTEMBACKUPTYPE, wxID_DATABACKUPSYSTEMDELETEBACKUP,
 wxID_DATABACKUPSYSTEMRESTOREBACKUP, wxID_DATABACKUPSYSTEMBACKUPLIST,
 wxID_DATABACKUPSYSTEMEXITBUTTON, wxID_CMSMAINDIALOGWARNINGTEXT,
] = [wx.NewId() for _init_ctrls in range(8)]

class DataBackupSystem(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DATABACKUPSYSTEM,
              name='DataBackupSystem', parent=prnt, pos=wx.Point(358, 286),
              size=self.mainwin,
              style=wx.DEFAULT_DIALOG_STYLE|wx.CAPTION|wx.THICK_FRAME,
              title=self.backuptitle)
        self.SetClientSize(self.mainwin)

        self.CMSMainPage = wx.StaticBitmap(bitmap=self.mainpage,
              id=wxID_BITMAPCMSMAINPAGE, name='BitmapCMSMainPage', parent=self,
              pos=wx.Point(0, 0), size=self.mainwin,
              style=wx.ALIGN_CENTRE|wx.TAB_TRAVERSAL)

        ### Button size
        buttonsize = (150, 30)

        self.BackupType = wx.Choice(choices=self.backuptype,
              id=wxID_DATABACKUPSYSTEMBACKUPTYPE, name='BackupType', parent=self.CMSMainPage,
              pos=wx.Point(20, 10), size=buttonsize, style=0)
        self.BackupType.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        self.RestoreBackup = wx.lib.buttons.GenButton(id=wxID_DATABACKUPSYSTEMRESTOREBACKUP,
              label=self.restorebackuplabel, name='RestoreBackup', parent=self.CMSMainPage,
              pos=wx.Point(190, 10), size=buttonsize, style=wx.ALIGN_CENTRE)
        self.RestoreBackup.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        self.DeleteBackup = wx.lib.buttons.GenButton(id=wxID_DATABACKUPSYSTEMDELETEBACKUP,
              label=self.deletebackuplabel, name='DeleteBackup', parent=self.CMSMainPage,
              pos=wx.Point(360, 10), size=buttonsize, style=wx.ALIGN_CENTRE)
        self.DeleteBackup.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        listsize = (400, 200)
        backuplist_size_x = self.mainwin[0] - 40
        backuplist_size_y = self.mainwin[1] - 20 - 40 - 40
        self.BackupList = wx.ListCtrl(id=wxID_DATABACKUPSYSTEMBACKUPLIST,
              name='BackupList', parent=self.CMSMainPage, pos=wx.Point(20, 50),
              size=wx.Size(backuplist_size_x, backuplist_size_y), style=wx.LC_REPORT|wx.SUNKEN_BORDER|
              wx.LC_VRULES|wx.LC_HRULES|wx.LC_SINGLE_SEL)
        self.BackupList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'新細明體'))

        ### 離開
        exit_x = self.mainwin[0] / 2 - 40
        exit_y = self.mainwin[1] - 40
        self.ExitButton = wx.Button(id=wxID_DATABACKUPSYSTEMEXITBUTTON, label=u'離開',
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


    def __init__(self, backuptitle, parent, mainwin, mainpagefile, mainpage, mainpagesize, imagedir, imginfo, dbname, backuptable, workdir, warntext):
        self.currentItem = -1
        self.deletebackuplabel = u'刪除備份'
        self.restorebackuplabel = u'回復備份'

        self.backuptitle = backuptitle
        self.parent = parent
        self.mainwin = mainwin
        self.mainpagefile = mainpagefile
        self.mainpage = mainpage
        self.mainpagesize = mainpagesize
        self.imagedir = imagedir
        self.imginfo = imginfo
        self.dbname = dbname
        self.backuptable = backuptable
        self.workdir = workdir
        self.warntext = warntext

        self.mainpagetype = self.imginfo.GetImageType(self.mainpagefile)
        self.sysinfo = GetSysInfo.GetSysInfo()
        self.backuptype = self.sysinfo.GetBackupTypeList()
        self.HeaderList, self.HeaderId = self.sysinfo.GetBackupHeaderList()

        self._init_ctrls(parent)
        self.Center()

        self.Bind(wx.EVT_CHOICE, self.OnBackupType, self.BackupType)
        self.Bind(wx.EVT_BUTTON, self.OnDeleteBackup, self.DeleteBackup)
        self.Bind(wx.EVT_BUTTON, self.OnRestoreBackup, self.RestoreBackup)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnBackupItemSelect, self.BackupList)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.OnBackupItemFocus, self.BackupList)
        self.BackupList.Bind(wx.EVT_LEFT_DCLICK, self.OnBackupDoubleClick)
        self.BackupList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnBackupRightClick)
        self.SetEscapeId(wxID_DATABACKUPSYSTEMEXITBUTTON)
        self.BackupType.SetSelection(0)

        self.allbackupinfo = self.GetAllBackupInfo()
        self.CreateHeader()
        self.InitData(self.allbackupinfo)

    def DecompressData(self, backupfile):
        #print u'開始解壓縮資料'
        error = ''
        try:
            zf = zipfile.ZipFile(backupfile)
            zf.extractall(self.workdir)
        except:
            self.ShowNoItemSelectMessage('DECOMPRESSFAILED')
            error = 'Backup failed'
            print u'回復備份檔案失敗'

        if error == '':
            replace = self.ShowNoItemSelectMessage('RESTORECOMPLETE')

        return error

    def CompressData(self, backupfile):
        #print u'開始壓縮資料'
        error = ''
        try:
            zf = zipfile.ZipFile(backupfile, "w")
            datadirs = ['dbdir', 'imgdir']
            for topdir in datadirs:
                for dirname, subdirs, files in oswalk(topdir):
                    for file1 in files:
                        infile = '%s\\%s'%(dirname, file1)
                        #print infile
                        zf.write(infile)

            #print zf.namelist()
            zf.close()
            #print u'資料壓縮完成'
        except:
            self.ShowNoItemSelectMessage('BACKUPFAILED')
            error = 'Backup failed'
            print u'資料壓縮失敗'

        return error

    def OnBackupLocal(self, backupselect):
        backupdest = self.backuptype[backupselect]
        replace = False
        error = ''

        import win32ui

        while 1:
            try:
                #print u'選擇備份儲存路徑'
                # 1 -> 表示打開文件對話窗
                dlg = win32ui.CreateFileDialog(1)
                # 設定初始目錄
                dlg.SetOFNInitialDir('')
                dlg.DoModal()
                # 取得儲存的文件名稱 [我的資料備份檔案.zip]
                backupfile = dlg.GetPathName()
                #print u'備份檔案：'
                #print backupfile
                if backupfile != '':
                    #print backupfile
                    filename, ext = path.splitext(backupfile)
                    if ext not in ['.zip']:
                        backupfile = '%s.zip'%backupfile
                    if path.isfile(backupfile):
                        replace = self.ShowNoItemSelectMessage('FILEEXIST')
                        #print replace
                        if replace:
                            break
                    else:
                        break
                else:
                    error = u'取消'
                    break
            except:
                error = u'取得儲存的文件名稱錯誤'
                print error

        if error == '':
            error = self.CompressData(backupfile)
            if error == '':
                filetime = datetime.fromtimestamp(path.getmtime(backupfile))
                filetime = str(filetime)[0:16]
                filesize = stat(backupfile).st_size
                filesize = self.ConvertFileSize(filesize)

                ### 中文檔名轉換 ASCII --> Unicode
                #print isinstance(backupfile, unicode)
                backupfile = str(backupfile).decode(sys.getfilesystemencoding())
                #print backupfile
                #print isinstance(backupfile, unicode)

                error = self.InsertDB(replace, backupdest, filetime, backupfile, filesize)

        return error

    def InsertDB(self, replace, backuptype, backuptime, backupname, backupsize):
        #print u'儲存備份資訊於資料庫'
        #print backuptype, backuptime, backupname, backupsize
        if replace:
            sqlaction = 'update'
            sqlcmd  = '''UPDATE %s
                            SET Backup_Status = '1'
                            WHERE Backup_Filename = '%s'
                        '''%(self.backuptable, backupname)

            try:
                db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
                info = db.ConnectDB()
                #print u'備份資訊儲存完成'
            except:
                print 'Access database error %s'%sqlacion
                print sqlcmd
                info = 'error'
                print u'備份資訊儲存失敗'

        sqlaction = 'insert'
        sqlcmd  = '''INSERT INTO %s '''%(self.backuptable, )
        sqlcmd += '''   (
                        Backup_Destination, Backup_Filetime,
                        Backup_Filename, Backup_Filesize,
                        Backup_Status
                        )
                    VALUES (
                        '%s', '%s', 
                        '%s', '%s', 
                        '0'
                        )
                    '''%(backuptype, backuptime, backupname, backupsize)

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            info = db.ConnectDB()
            #print u'備份資訊儲存完成'
        except:
            print 'Access database error %s'%sqlacion
            print sqlcmd
            info = 'error'
            print u'備份資訊儲存失敗'

        return info

    def GetAllBackupInfo(self):
        allbackupinfo = []
        sqlaction = 'select'
        sqlcmd  = '''SELECT * FROM %s
                        WHERE Backup_Status = '0' '''%(self.backuptable, )

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            allbackupinfo = db.ConnectDB()
        except:
            print 'Access database error %s'%sqlacion
            print sqlcmd
            error = 'error'

        return allbackupinfo

    def DeteleFromDatabase(self, backupinfo):
        backupid = backupinfo[0]
        sqlaction = 'update'
        sqlcmd  = '''UPDATE %s
                        SET Backup_Status = '1'
                        WHERE Backup_ItemNo = %s
                    '''%(self.backuptable, backupid)

        try:
            db = ConnectDB.ConnectDB(self.dbname, sqlaction, sqlcmd)
            allbackupinfo = db.ConnectDB()
        except:
            print 'Access database error %s'%sqlacion
            print sqlcmd
            error = 'error'

        return

    def ConvertFileSize(self, filesize):
        bid = 0
        while 1:
            #print bid, filesize
            if filesize < 10240:
                break
            else:
                filesize = filesize / 1024
                bid += 1

        if bid == 0:
            base = ' B'
        elif bid == 1:
            base = 'KB'
        elif bid == 2:
            base = 'MB'
        elif bid == 3:
            base = 'GB'
        elif bid == 4:
            base = 'TB'
        return_filesize = '%s %s'%(format(filesize, ','), base)
                
        return return_filesize

    def DeleteFromLocaldisk(self, backupinfo):
        backupfile = backupinfo[3]
        if path.isfile(backupfile):
            remove(backupfile)

        return

    def OnBackupType(self, event):
        backupselect = self.BackupType.GetSelection()
        #print u'備份至：  ', self.backuptype[backupselect]
        if backupselect == 1:
            error = self.OnBackupLocal(backupselect)

        if error == '':
            self.allbackupinfo = self.GetAllBackupInfo()
            self.InitData(self.allbackupinfo)
        self.BackupType.SetSelection(0)

    def OnDeleteBackup(self, event):
        self.OnBackupItemSelect(self.BackupList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('MODIFY')
        else:
            backupinfo = self.allbackupinfo[self.currentItem]
            replace = self.ShowNoItemSelectMessage('DELETE')
            if replace:
                self.DeteleFromDatabase(backupinfo)
                self.DeleteFromLocaldisk(backupinfo)
            self.allbackupinfo = self.GetAllBackupInfo()
            self.InitData(self.allbackupinfo)

        return

    def OnRestoreBackup(self, event):
        self.OnBackupItemSelect(self.BackupList)
        #print self.currentItem
        if self.currentItem == -1:
            self.ShowNoItemSelectMessage('RESTORE')
        else:
            replace = self.ShowNoItemSelectMessage('RESTORECOMFIRM')
            if replace:
                backupinfo = self.allbackupinfo[self.currentItem]
                backupfile = backupinfo[3]
                if path.isfile(backupfile):
                    error = self.DecompressData(backupfile)

        return

    def OnBackupItemFocus(self, event):

        return

    def OnBackupDoubleClick(self, event):

        return

    def OnBackupRightClick(self, event):

        return

    def OnBackupItemSelect(self, event):
        self.currentItem = self.BackupList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)

        return

    def CreateHeader(self):
        #print 'Create list header'
        cid = 0
        for id in range(0, len(self.HeaderList)):
            hidlist = self.HeaderId.keys()
            hidlist.sort()
            if id in hidlist:
                titlename = self.HeaderList[id]
                colwidth  = self.HeaderId[id]
                #print id, titlename, colwidth
                self.BackupList.InsertColumn(cid, titlename, width=colwidth)
                cid += 1

        return

    def InitData(self, backupinfo):
        #print 'Clean all data'
        self.BackupList.DeleteAllItems()

        if backupinfo:
            listid = 0
            for backup in backupinfo:
                backupdest = backup[1]
                backupfile = backup[3]
                #print backupdest, backupfile
                #print self.backuptype.index(backupdest)
                if self.backuptype.index(backupdest) == 1:
                    if path.isfile(backupfile):
                        backupstat = u''
                        color = wx.WHITE
                    else:
                        backupstat = u'備份檔案已遺失'
                        color = wx.Colour(225, 75, 75)
                else:
                    backupstat = u''
                    color = wx.WHITE
                #print backup
                cid = 0
                hidlist = self.HeaderId.keys()
                hidlist.sort()
                #print hidlist
                for id in hidlist:
                    #print listid, id, cid, backup[id]
                    if hidlist.index(id) == 0:
                        self.BackupList.InsertStringItem(listid, '%s'%backup[id + 1])
                    else:
                        self.BackupList.SetStringItem(listid, cid, '%s'%backup[id + 1])
                    cid += 1
                #print listid, id, cid, backupstat
                self.BackupList.SetStringItem(listid, cid-1, '%s'%backupstat)
                self.BackupList.SetItemBackgroundColour(listid, color)
                listid += 1

        return

    def ShowNoItemSelectMessage(self, type):
        replace = False
        if type == 'MODIFY':
            msg = u'請先選擇一個備份檔案進行刪除！'
            dialog = wx.MessageDialog(self, msg, u'警告', wx.OK|wx.ICON_INFORMATION)
        elif type == 'BACKUPFAILED':
            msg = u'檔案備份失敗，請客服聯絡'
            dialog = wx.MessageDialog(self, msg, u'警告', wx.OK|wx.ICON_INFORMATION)
        elif type == 'DECOMPRESSFAILED':
            msg = u'回復備份檔案失敗，請客服聯絡'
            dialog = wx.MessageDialog(self, msg, u'警告', wx.OK|wx.ICON_INFORMATION)
        elif type == 'RESTORE':
            msg = u'請先選擇一個備份檔案進行資料回復'
            dialog = wx.MessageDialog(self, msg, u'警告', wx.OK|wx.ICON_INFORMATION)
        elif type == 'RESTORECOMPLETE':
            msg = u'回復備份完成，請重新開啟程式'
            dialog = wx.MessageDialog(self, msg, u'警告', wx.OK|wx.ICON_INFORMATION)
        elif type == 'FILEEXIST':
            msg = u'備份檔案已存在，確認要覆蓋備份檔案？'
            dialog = wx.MessageDialog(self, msg, u'提示', wx.YES_NO|wx.ICON_INFORMATION)
        elif type == 'DELETE':
            msg = u'刪除備份檔案，是否要繼續？'
            dialog = wx.MessageDialog(self, msg, u'提示', wx.YES_NO|wx.ICON_INFORMATION)
        elif type == 'RESTORECOMFIRM':
            msg = u'回復備份檔案，將會覆蓋掉所有已儲存的資料，是否要繼續？'
            dialog = wx.MessageDialog(self, msg, u'提示', wx.YES_NO|wx.ICON_INFORMATION)

        dialog.SetIcon(wx.Icon(self.mainpagefile, self.mainpagetype))
        result = dialog.ShowModal()
        if result == wx.ID_YES:
            replace = True
        elif result == wx.ID_NO:
            replace = False

        return replace


