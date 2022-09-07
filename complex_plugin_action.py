from .src.get_selected import *
from .src.GUI import *
from .src.ui_properties import *
import os
import wx
import traceback
import sys

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
            print(selected.list)
            print(selected.get_properties())
            print()
            print(Ui_elements(selected.get_properties()))

            #app = wx.App(False)
            #frame = GUI(None, 'Properties', selected)
            #app.MainLoop()

        except (Exception, ArithmeticError) as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print (message)

            exc_type, exc_value, exc_tb = sys.exc_info()

            stack_summary = traceback.extract_tb(exc_tb)
            end = stack_summary[-1]

            err_type = type(exc_value).__name__
            err_msg = str(exc_value)

            print(f"\n{err_type}")
            print(f"{err_msg}.")
            print(f"file: {end.filename}")
            print(f"method: {end.name}")
            print(f"linenr: {end.lineno}")
            print(f"{end.line!r}")




