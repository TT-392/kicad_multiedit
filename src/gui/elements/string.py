import wx
from ...utils import *

class Type_string:
    def __init__(self):
        pass

class string_control:
    def __init__(self, parent_window, parent, name, varname, Type):
        self.type = Type

        self.control = wx.TextCtrl(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        parent.Add(self.control, 1, wx.ALL|wx.EXPAND, 5)

        self.control.SetToolTip(varname)

    def set_value(self, value):
        self.old_value = value

        if value[:1] == "\"" and value[-1:] == "\"":
            self.control.SetValue(eval(value))
        else:
            self.control.SetValue("*")

    def get_value(self):
        if self.control.GetValue() == "*":
            return self.old_value
        else:
            return utils.to_parseable_string(self.control.GetValue())

