from .GUI import *
from .properties import *
from .property import *
from .eval_value import *
from .get_selected import *
import pcbnew
import os
import wx

properties = Properties_array([
        Property("X", "Position", "length", 2),
        Property("X", "Position", "length", 2),
        Property("Y", "Position", "length", 3),
        Property("Y", "Position", "length", 4),
        Property("Ref", "Strings", "string", "aaa"),
        Property("Ref", "Strings", "string", "bbb"),
        Property("datasheet", "Strings", "string", "datasheet"),
        Property("Angle", "Orientation", "angle", 90)
        ])

def open_properties():
    selected = get_selected()
    
    app = wx.App(False)
    frame = GUI(None, 'Properties', selected)
    app.MainLoop()

