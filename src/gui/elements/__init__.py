import wx
from .python import *
from .checkbox import *
from .dropdown import *
from .string import *

class Type_layer:
    def __init__(self, choices):
        self.choices = choices

def add_control(parent_window, parent, name, varname, value, Type):
    ui_name = wx.StaticText(parent_window, wx.ID_ANY, name + ":", wx.DefaultPosition, wx.DefaultSize, 0)
    parent.Add(ui_name, 0, wx.ALL, 5)
    
    if type(Type) == Type_python:
        control = python_control(parent_window, parent, name, varname, Type)

    elif type(Type) == Type_checkbox:
        control = checkbox_control(parent_window, parent, name, varname, Type)

    elif type(Type) == Type_string:
        control = string_control(parent_window, parent, name, varname, Type)

    elif type(Type) == Type_dropdown or type(Type) == Type_layer: # Bitmap combo box for fancy colors with layers not yet implemented, therefore it is treated as a normal dropdown
        control = dropdown_control(parent_window, parent, name, varname, Type)

    control.SetValue(value)


    return control
