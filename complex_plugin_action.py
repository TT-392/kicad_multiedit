from .src.get_selected import *
from .src.GUI import *
import os
import wx

pcb = pcbnew.GetBoard()

class ComplexPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "A complex action plugin"
        self.category = "A descriptive category name"
        self.description = "A description of the plugin"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional


    def Run(self):
        # The entry function of the plugin that is executed on user action
        try:
            selected = get_selected()

            app = wx.App(False)
            frame = GUI(None, 'Properties', selected)
            app.MainLoop()

        except (Exception, ArithmeticError) as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print (message)



