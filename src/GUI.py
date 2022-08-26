from .property import *
from .eval_value import *
import wx


class GUI(wx.Frame):
    def __init__(self, parent, title, properties_array):
        self.properties = properties_array
        height = 600
        width = 800
        height_half = height//2
        width_half = width//2

        wx.Frame.__init__(self, parent, title=title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        # add panel
        self.panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0),
                              size=(width_half, height))
        panel1 = wx.Panel(self, wx.ID_ANY, pos=(width_half, 0),
                          size=(width_half, height))

        self.Ypos = 10
        for cathegory in self.properties.get_cathegories():
            if self.properties.contains_cathegory(cathegory):
                cathegory_properties = self.properties.get_in_cathegory(cathegory)

                wx.StaticText(self.panel, label=cathegory, pos=(10, self.Ypos), 
                        size=(100, 20), style=wx.SIMPLE_BORDER)
                self.Ypos += 35

                for name in cathegory_properties.get_names():
                    self.drawProp(cathegory_properties.get_with_name(name))


        self.button = wx.Button(self.panel, label="Save", pos=(10, self.Ypos))
        self.button.Bind(wx.EVT_BUTTON, self.save)

        self.panel.Fit()

        self.Show(True)

    def drawProp(self, props):
        assert props.all_same_cathegory()
        assert props.all_same_name()

        prop0 = props.list[0]
        ui_element = None

        if prop0.data_type == 'length' or prop0.data_type == 'length_unsigned':
            wx.StaticText(self.panel, label=prop0.name, pos=(10, self.Ypos),
                                        size=(100, 20), style=wx.SIMPLE_BORDER)

            ui_element = wx.TextCtrl(self.panel, pos=(110, self.Ypos - 5),
                                        size=(140, -1))

            wx.StaticText(self.panel, label="mm", pos=(250, self.Ypos),
                                        size=(40, 20), style=wx.SIMPLE_BORDER)

        if prop0.data_type == 'angle':
            wx.StaticText(self.panel, label=prop0.name, pos=(10, self.Ypos),
                                        size=(100, 20), style=wx.SIMPLE_BORDER)

            ui_element = wx.TextCtrl(self.panel, pos=(110, self.Ypos - 5),
                                        size=(140, -1))


        self.Ypos += 35

        if props.all_same_value():
            ui_element.SetValue(str(prop0.value))
        else:
            ui_element.SetValue("x")

        for prop in props.list:
            prop.ui_element = ui_element
                


    def save(self, e):
        for prop in self.properties.list:
            if not prop.eval():
                return

        self.Close(True)  # Close the frame.

