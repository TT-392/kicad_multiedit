import wx

class Type_python:
    def __init__(self, unit=None):
        self.unit = unit

class python_control:
    def __init__(self, parent_window, parent, name, varname, Type):
        if Type.unit != None: 
            ui_grid = wx.FlexGridSizer(0, 2, 0, 0)
            ui_grid.SetFlexibleDirection(wx.BOTH)
            ui_grid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
            self.control = wx.TextCtrl(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)

            ui_grid.Add(self.control, 0, wx.ALL|wx.EXPAND, 5)

            ui_unit = wx.StaticText(parent_window, wx.ID_ANY, Type.unit, wx.DefaultPosition, wx.DefaultSize, 0)
            ui_unit.Wrap(-1)

            ui_grid.Add(ui_unit, 0, wx.ALL, 5)

            parent.Add(ui_grid, 1, wx.EXPAND, 5)

        else:
            self.control = wx.TextCtrl(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            parent.Add(self.control, 1, wx.ALL|wx.EXPAND, 5)

        self.control.SetToolTip(varname)


    def SetValue(self, value):
        self.control.SetValue(value)

    def GetValue(self):
        return self.control.GetValue()

