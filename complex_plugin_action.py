import pcbnew
import os
import wx

class ComplexPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "A complex action plugin"
        self.category = "A descriptive category name"
        self.description = "A description of the plugin"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional

    def Run(self):
        # The entry function of the plugin that is executed on user action
        print("Hello World")

        try:
            start_GUI2()
        except (Exception, ArithmeticError) as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print (message)

def start_GUI2():
    app = wx.App(False)
    frame = MyFrame(None, 'Small editor')
    app.MainLoop() # I don't think this actually ever ends, no idea if that is a problem

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        height = 600
        width = 800
        height_half = height//2
        width_half = width//2

        wx.Frame.__init__(self, parent, title=title, size=(width, height), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        # add panel
        self.panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0),
                              size=(width_half, height))
        panel1 = wx.Panel(self, wx.ID_ANY, pos=(width_half, 0),
                          size=(width_half, height))

        # text
        self.output = wx.StaticText(self.panel, label="X:", pos=(10, 10),
                                    size=(100, 20), style=wx.SIMPLE_BORDER)
        self.aaa = wx.TextCtrl(self.panel, pos=(110, 10),
                                    size=(140, -1))

        self.input = wx.StaticText(self.panel, label="Y:", pos=(10, 40),
                                   size=(100, 20), style=wx.SIMPLE_BORDER)
        self.editname = wx.TextCtrl(self.panel, pos=(110, 40),
                                    size=(140, -1))

        self.button = wx.Button(self.panel, label="Save", pos=(10, 70))
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

        self.Show(True)


    def OnButton(self, e):
        self.Close(True)  # Close the frame.
