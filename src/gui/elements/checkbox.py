import wx

class Type_checkbox:
    def __init__(self):
        pass

class checkbox_control:
    def __init__(self, parent_window, parent, name, varname, Type):
        self.control = wx.CheckBox(parent_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.CHK_3STATE)
        parent.Add(self.control, 1, wx.ALL|wx.EXPAND, 5)

        self.control.SetToolTip(varname)

    def set_value(self, value):
        self.old_value = value

        if value == "True":
            self.control.Set3StateValue(1)
        elif value == "False":
            self.control.Set3StateValue(0)
        else:
            self.control.Set3StateValue(2)

    def get_value(self):
        value = self.control.Get3StateValue()
        if value == 1:
            return "True"
        elif value == 0:
            return "False"
        else:
            return self.old_value
