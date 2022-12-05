import wx
from .control import *
from ...kicad.kicad import *

class Type_dropdown:
    def __init__(self, choices):
        self.choices = choices

    def get_choices(self):
        if self.choices == "all layers":
            kicad_info.update()
            return kicad_info.get_layers()

        else:
            return []

class dropdown_control(Control):
    def __init__(self, parent_window, parent, category, name, varname, Type):
        Control.__init__(self)

        self.varname = varname
        self.category = category
        self.type = Type

        self.control = wx.Choice(parent_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.type.get_choices(), 0)
        parent.Add(self.control, 1, wx.ALL|wx.EXPAND, 5)
        self.wx_elements.append(self.control)

        self.control.SetToolTip(varname)

    def set_value(self, value):
        print(value)
        if value[:1] == "\"" and value[-1:] == "\"":
            isString = True
        else:
            isString = False

        if not (isString and value[1:-1] in self.type.get_choices()):
            self.control.Append("-- mixed values --") #TODO: this only works once
            self.control.SetSelection(len(self.type.get_choices()))
        else:
            self.control.SetSelection(self.type.get_choices().index(value[1:-1]))

    def get_value(self):
        if self.control.GetString(self.control.GetSelection()) == "-- mixed values --":
            return self.varname

        return "\"" + self.control.GetString(self.control.GetSelection()) + "\""
