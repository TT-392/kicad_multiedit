from .GUI import *
from .property import *
import pcbnew
import os
import wx

def open_properties():
    app = wx.App(False)
    frame = GUI(None, 'Small editor', [Property("X", "Position", 'float', 4), Property("X", "Position", 'float', 5), Property("Y", "Position", 'float', 4), Property("Y", "Position", 'float', 4)])
    app.MainLoop() # I don't think this actually ever ends, no idea if that is a problem


