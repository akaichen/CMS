# -*- coding: utf-8 -*-
from distutils.core import setup
from py2exe.build_exe import py2exe

import sys
sys.path.append('C:\Python27\Lib\site-packages\PIL')
#import glob
#import os
#import zlib
#import shutil
#import decimal

# Remove the build folder
#shutil.rmtree("build", ignore_errors=True)

class Target(object):
    """ A simple class that holds information on our executable file. """
    def __init__(self, **kw):
        """ Default class constructor. Update as you need. """
        self.__dict__.update(kw)

data_files = [] ## ignored for this paste

'''
includes = ['HTMLParser', 'markupbase', 'subprocess',
            'wx.lib.embeddedimage']
excludes = ['_ctypes', '_gtkagg',  '_imagingft', '_ssl',
            '_tkagg', 'bsddb', 'bz2', 'comtypes',
            'ctypes', 'curses', 'difflib', 'difflib',
            'doctest', 'email', 'hashlib', 'imaging', 'inspect',
            'logging', 'mailbox', 'numpy', 'optparse', 'pdb',
            'PIL', 'pydoc', 'pythonwin', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'subprocess',
            'tcl', 'test', 'Tkconstants', 'Tkinter', 'unicodedata',
            'unittest', 'urllib2', 'win32api', 'win32com',
            'win32con', 'win32gui', 'win32ui', 'win32uiole',
            'winxpgui', 'wxPython', 'xml', 'xmllib', 'xmlrpclib']
packages = ['encodings', 'wx.media']
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll',
                'pythoncom25.dll',
                'pywintypes25.dll', 'sqlite3.dll', 'tcl84.dll',
                'tix84.dll', 'tk84.dll', 'wxbase28uh_xml_vc.dll',
                'wxmsw28uh_aui_vc.dll', 'wxmsw28uh_gl_vc.dll',
                'wxmsw28uh_stc_vc.dll', 'wxmsw28uh_xrc_vc.dll']
icon_resources = []
bitmap_resources = []
other_resources = []
'''
includes = ['Tkinter', 'Tkconstants', 'PIL', 'Image', 'decimal',
            '_imaging', 'Image']
excludes = ['_ctypes', '_gtkagg',  '_imagingft', '_ssl',
            '_tkagg', 'bsddb', 'bz2', 'comtypes',
            'ctypes', 'curses', 'difflib', 'difflib',
            'doctest', 'email', 'hashlib',  'inspect',
            'logging', 'mailbox', 'numpy', 'optparse', 'pdb',
            'pydoc', 'pythonwin', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'subprocess',
            'tcl', 'test',   'unicodedata',
            'unittest', 'urllib2', 'win32api', 'win32com',
            'win32con', 'win32gui', 'win32ui', 'win32uiole',
            'winxpgui', 'wxPython', 'xml', 'xmllib', 'xmlrpclib']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll',
                'pythoncom25.dll',
                'pywintypes25.dll', 'sqlite3.dll', 'tcl84.dll',
                'tix84.dll', 'tk84.dll', 'wxbase28uh_xml_vc.dll',
                'wxmsw28uh_aui_vc.dll', 'wxmsw28uh_gl_vc.dll',
                'wxmsw28uh_stc_vc.dll', 'wxmsw28uh_xrc_vc.dll',
                ]

icon_resources = []
bitmap_resources = []
other_resources = []

GUI2Exe_Target_1 = Target(
    # what to build
    script = "CMS.pyw",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "CMS",   
    version = "v1.0",
    company_name = u'陳智凱',
    copyright = u'陳智凱',
    name = u'客戶資料管理系統',
    )

setup(
    # No UPX or Inno Setup
    data_files = data_files,
    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 3,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },
    zipfile = None,
    console = [],
    windows = [GUI2Exe_Target_1],
    service = [],
    com_server = [],
    ctypes_com_server = []
    )
