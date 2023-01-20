import wx
from .control import *
from ...kicad.kicad import *

class Type_python:
    def __init__(self, unit=None):
        self.unit = unit

    def get_unit(self):
        if self.unit == "unit user length":
            kicad_info.update()
            return kicad_info.unit_string

        else:
            return None



class python_control(Control):
    def __init__(self, parent_window, parent, category, name, varname, Type, enter_func = None):
        Control.__init__(self)

        self.category = category

        if Type.unit != None: 
             ui_grid = wx.FlexGridSizer(0, 2, 0, 0)
             ui_grid.SetFlexibleDirection(wx.BOTH)
             ui_grid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
             self.control = wx.TextCtrl(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
             self.wx_elements.append(self.control)

             ui_grid.Add(self.control, 0, wx.ALL|wx.EXPAND, 5)

             ui_unit = wx.StaticText(parent_window, wx.ID_ANY, Type.get_unit(), wx.DefaultPosition, wx.DefaultSize, 0)
             ui_unit.Wrap(-1)
             self.wx_elements.append(ui_unit)

             ui_grid.Add(ui_unit, 0, wx.ALL, 5)

             parent.Add(ui_grid, 1, wx.EXPAND, 5)

        else:
            self.control = wx.TextCtrl(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
            parent.Add(self.control, 1, wx.ALL|wx.EXPAND, 5)
            self.wx_elements.append(self.control)

        self.control.SetToolTip(varname)
        if enter_func != None:
            self.control.Bind(wx.EVT_TEXT_ENTER, enter_func)

    def set_value(self, value):
        self.control.SetValue(value)

    def get_value(self):
        return self.control.GetValue()

