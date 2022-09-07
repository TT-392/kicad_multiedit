import pcbnew
import wx
import random
import os


#MyFrame: Frame
#    outer_sizer: BoxSizer
#        self.scroll_box: ScrolledWindow
#            main_grid: flexGridSizer
#        toolbar: ToolBar

class GUI(wx.Frame):
    def __init__(self, parent, title, selected):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(784,372), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(outer_sizer)
        self.Layout()

        self.scroll_box = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        self.scroll_box.SetScrollRate(5, 5)

        outer_sizer.Add(self.scroll_box, 1, wx.EXPAND |wx.ALL, 5)

        toolbar = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL)
        toolbar.Realize()

        outer_sizer.Add(toolbar, 0, wx.ALIGN_RIGHT, 5)

        main_grid = wx.FlexGridSizer(0, 3, 0, 0)
        main_grid.SetFlexibleDirection(wx.BOTH)
        main_grid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        main_grid.Fit(self.scroll_box)

        self.scroll_box.SetSizer(main_grid)
        self.scroll_box.Layout()

        ##########################################



        button_cancel = wx.Button(toolbar, wx.ID_ANY, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_cancel)

        button_apply = wx.Button(toolbar, wx.ID_ANY, "Apply", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_apply)

        button_save = wx.Button(toolbar, wx.ID_ANY, "Save", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_save)


        self.add_category(main_grid, "position")

        self.add_value(main_grid, "X", "mm")
        self.add_checkboxes(main_grid, 4, [True, False, False, True])

        self.add_value(main_grid, "Y", "mm")
        self.add_checkboxes(main_grid, 4, [True, False, False, True])

        self.add_category(main_grid, "Orientation")

        self.add_value(main_grid, "Angle")
        self.add_checkboxes(main_grid, 4, [True, False, False, False])

        self.add_category(main_grid, "Footprint")

        self.add_value(main_grid, "Ref")
        self.add_checkboxes(main_grid, 4, [True, False, False, False])

        self.add_category(main_grid, "Line")
        self.add_value(main_grid, "StartX", "mm")
        self.add_checkboxes(main_grid, 4, [False, True, True, False])

        self.add_value(main_grid, "StartY", "mm")
        self.add_checkboxes(main_grid, 4, [False, True, True, False])

        self.add_value(main_grid, "EndX", "mm")
        self.add_checkboxes(main_grid, 4, [False, True, True, False])

        self.add_value(main_grid, "EndY", "mm")
        self.add_checkboxes(main_grid, 4, [False, True, True, False])

        self.add_value(main_grid, "Width", "mm")
        self.add_checkboxes(main_grid, 4, [False, True, True, True])

        self.add_category(main_grid, "Arc")
        self.add_value(main_grid, "Arc angle")
        self.add_checkboxes(main_grid, 4, [False, False, True, False])

        self.add_category(main_grid, "Circle")
        self.add_value(main_grid, "Radius", "mm")
        self.add_checkboxes(main_grid, 4, [False, False, False, True])




        self.Show()

    def add_category(self, parent, name):
        m_staticText12 = wx.StaticText(self.scroll_box, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(m_staticText12, 0, wx.ALL, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)

    def add_value(self, parent, name, unit = None):
        m_staticText12 = wx.StaticText(self.scroll_box, wx.ID_ANY, name + ":", wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(m_staticText12, 0, wx.ALL, 5)

        if unit != None:
            box_unit_grid = wx.FlexGridSizer(0, 2, 0, 0)
            box_unit_grid.SetFlexibleDirection(wx.BOTH)
            box_unit_grid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

            m_textCtrl7 = wx.TextCtrl(self.scroll_box, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            box_unit_grid.Add(m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5)


            m_staticText14 = wx.StaticText(self.scroll_box, wx.ID_ANY, unit, wx.DefaultPosition, wx.DefaultSize, 0)
            m_staticText14.Wrap(-1)

            box_unit_grid.Add(m_staticText14, 0, wx.ALL, 5)

            parent.Add(box_unit_grid, 1, wx.EXPAND, 5)
        else:
            print("None")
            m_textCtrl7 = wx.TextCtrl(self.scroll_box, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            parent.Add(m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5)



    def draw_icons(self, images):
        icon_sizer = wx.BoxSizer(wx.HORIZONTAL)

        images = ("add_footprint", "add_line", "add_arc", "add_circle")

        for img in range(0, size):
            bitmap = wx.StaticBitmap(self.scroll_box, wx.ID_ANY, wx.Bitmap(os.path.join(os.path.dirname(__file__), "../resources/output/" + bmps[i] + ".png"), wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(20,20), 0)
            icon_sizer.Add(bitmap, 0, wx.ALL, 0)

        parent.Add(icon_sizer, 1, wx.EXPAND, 5)

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
                                        size=(180, -1))

        elif prop0.data_type == 'string':
            wx.StaticText(self.panel, label=prop0.name, pos=(10, self.Ypos),
                                        size=(100, 20), style=wx.SIMPLE_BORDER)

            ui_element = wx.TextCtrl(self.panel, pos=(110, self.Ypos - 5),
                                        size=(180, -1))


        if random.randint(0, 40) > 1:
            wx.CheckBox(self.panel, -1, '', (300+10, self.Ypos))
        if random.randint(0, 40) > 2:
            wx.CheckBox(self.panel, -1, '', (300+30, self.Ypos))
        if random.randint(0, 40) > 3:
            wx.CheckBox(self.panel, -1, '', (300+50, self.Ypos))
        if random.randint(0, 40) > 4:
            wx.CheckBox(self.panel, -1, '', (300+70, self.Ypos))
        if random.randint(0, 40) > 5:
            wx.CheckBox(self.panel, -1, '', (300+90, self.Ypos))
        if random.randint(0, 40) > 6:
            wx.CheckBox(self.panel, -1, '', (300+110, self.Ypos))
        if random.randint(0, 40) > 7:
            wx.CheckBox(self.panel, -1, '', (300+130, self.Ypos))
        if random.randint(0, 40) > 8:
            wx.CheckBox(self.panel, -1, '', (300+150, self.Ypos))
        if random.randint(0, 40) > 11:
            wx.CheckBox(self.panel, -1, '', (300+170, self.Ypos))
        if random.randint(0, 40) > 13:
            wx.CheckBox(self.panel, -1, '', (300+190, self.Ypos))
        if random.randint(0, 40) > 17:
            wx.CheckBox(self.panel, -1, '', (300+210, self.Ypos))
        if random.randint(0, 40) > 27:
            wx.CheckBox(self.panel, -1, '', (300+230, self.Ypos))



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
