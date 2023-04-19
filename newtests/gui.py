import wx
import sys
from .test import *
sys.path.append("..")
from newsrc.gui.gui import *


print("starting gui")
app = wx.App(0)
dialog = Gui(None)
dialog.ShowModal()
app.MainLoop()

