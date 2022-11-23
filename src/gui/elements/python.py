import wx
from .control import *

class Type_python:
    def __init__(self, unit=None):
        self.unit = unit

class python_control(Control):
    def __init__(self, parent_window, parent, category, name, varname, Type):
        Control.__init__(self)

        self.category = category

        if Type.unit != None: 
             ui_grid = wx.FlexGridSizer(0, 2, 0, 0)
             ui_grid.SetFlexibleDirection(wx.BOTH)
             ui_grid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
             self.control = wx.TextCtrl(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
             self.wx_elements.append(self.control)

             ui_grid.Add(self.control, 0, wx.ALL|wx.EXPAND, 5)

             ui_unit = wx.StaticText(parent_window, wx.ID_ANY, Type.unit, wx.DefaultPosition, wx.DefaultSize, 0)
             ui_unit.Wrap(-1)
             self.wx_elements.append(ui_unit)

             ui_grid.Add(ui_unit, 0, wx.ALL, 5)

             parent.Add(ui_grid, 1, wx.EXPAND, 5)

        else:
            self.control = wx.TextCtrl(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            parent.Add(self.control, 1, wx.ALL|wx.EXPAND, 5)
            self.wx_elements.append(self.control)

        self.control.SetToolTip(varname)


    def set_value(self, value):
        self.control.SetValue(value)

    def get_value(self):
        return self.control.GetValue()

