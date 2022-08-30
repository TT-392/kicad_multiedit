import pcbnew
import wx


class GUI(wx.Frame):
    def __init__(self, parent, title, selected):
        self.selected = selected
        self.properties = selected.get_properties()
        height = 600
        width = 800
        height_half = height//2
        width_half = width//2

        wx.Frame.__init__(self, parent, title=title, size=(height, width), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        # add panel
        self.panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0),
                              size=(width_half, height))
        panel1 = wx.Panel(self, wx.ID_ANY, pos=(width_half, 0),
                          size=(width_half, height))

        self.Ypos = 10
        for category in self.properties.get_cathegories():
            if self.properties.contains_category(category):
                category_properties = self.properties.get_in_category(category)

                wx.StaticText(self.panel, label=category, pos=(10, self.Ypos), 
                        size=(100, 20), style=wx.SIMPLE_BORDER)
                self.Ypos += 35

                for name in category_properties.get_names():
                    self.drawProp(category_properties.get_with_name(name))


        self.button = wx.Button(self.panel, label="Save", pos=(10, self.Ypos))
        self.button.Bind(wx.EVT_BUTTON, self.save)

        self.panel.Fit()

        self.Show(True)

    def drawProp(self, props):
        # TODO: probably desirable to split this off into its own file
        assert props.all_same_category()
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

        elif prop0.data_type == 'angle':
            wx.StaticText(self.panel, label=prop0.name, pos=(10, self.Ypos),
                                        size=(100, 20), style=wx.SIMPLE_BORDER)

            ui_element = wx.TextCtrl(self.panel, pos=(110, self.Ypos - 5),
                                        size=(140, -1))

        elif prop0.data_type == 'string':
            wx.StaticText(self.panel, label=prop0.name, pos=(10, self.Ypos),
                                        size=(100, 20), style=wx.SIMPLE_BORDER)

            ui_element = wx.TextCtrl(self.panel, pos=(110, self.Ypos - 5),
                                        size=(140, -1))




        self.Ypos += 35

        if props.all_same_value():
            print(prop0.get_ui_value())
            ui_element.SetValue(str(prop0.get_ui_value()))
        else:
            if prop0.data_type == 'string':
                ui_element.SetValue("*")
            else:
                ui_element.SetValue("x")

        for prop in props.list:
            prop.ui_element = ui_element
                


    def save(self, e):
        for item in self.selected.list:
            for prop in item.properties.list:
                prop.update_value()
            
        pcbnew.Refresh()
        self.Close(True)  # Close the frame.
