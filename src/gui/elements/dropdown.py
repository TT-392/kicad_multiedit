import wx

class Type_dropdown:
    def __init__(self, choices):
        self.choices = choices

class dropdown_control:
    def __init__(self, parent_window, parent, name, varname, Type):
        self.type = Type

        self.control = wx.Choice(parent_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.type.choices, 0)
        parent.Add(self.control, 1, wx.ALL|wx.EXPAND, 5)

        self.control.SetToolTip(varname)

    def set_value(self, value):
        if value[:1] == "\"" and value[-1:] == "\"":
            isString = True
        else:
            isString = False

        if not (isString and value[1:-1] in self.type.choices):
            self.control.Append("-- mixed values --") #TODO: this only works once
            self.control.SetSelection(len(self.type.choices))
        else:
            self.control.SetSelection(self.type.choices.index(value[1:-1]))

    def get_value(self):
        return "\"" + self.control.GetString(self.control.GetSelection()) + "\""
