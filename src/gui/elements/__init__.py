import wx
import os
from .python import *
from .checkbox import *
from .dropdown import *
from .string import *
from .category import *

class Type_layer:
    def __init__(self, choices):
        self.choices = choices


#TODO: this stuff should move to Control.__init__
def add_control(parent_window, parent, category, name, varname, value, Type, item_types, enter_func = None):
    ui_name = wx.StaticText(parent_window, wx.ID_ANY, name + ":", wx.DefaultPosition, wx.DefaultSize, 0)
    parent.Add(ui_name, 0, wx.ALL, 5)
    
    if type(Type) == Type_python:
        control = python_control(parent_window, parent, category, name, varname, Type, enter_func)

    elif type(Type) == Type_checkbox:
        control = checkbox_control(parent_window, parent, category, name, varname, Type)

    elif type(Type) == Type_string:
        control = string_control(parent_window, parent, category, name, varname, Type, enter_func)

    elif type(Type) == Type_dropdown or type(Type) == Type_layer: # Bitmap combo box for fancy colors with layers not yet implemented, therefore it is treated as a normal dropdown
        control = dropdown_control(parent_window, parent, category, name, varname, Type)

    control.wx_elements.append(ui_name)
    control.set_value(value)

    control.add_icons(parent_window, parent, item_types)

    return control


