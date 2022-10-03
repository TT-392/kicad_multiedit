import os
import wx
import wx.xrc
import pcbnew


#GUI: Frame
#    outer_sizer: BoxSizer
#        self.scroll_box: ScrolledWindow
#            main_grid: flexGridSizer
#        toolbar: ToolBar


class GUI(wx.Frame):
    def __init__(self, parent, ui_elements):
        self.ui_elements = ui_elements

        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(400,800), style = wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(outer_sizer)
        self.Layout()

        m_toolBar1 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL)
        m_staticText2 = wx.StaticText(m_toolBar1, wx.ID_ANY, "Origin:", wx.DefaultPosition, wx.DefaultSize, 0)
        m_staticText2.Wrap(-1)
        
        m_toolBar1.AddControl(m_staticText2)
        self.origin_field = wx.TextCtrl(m_toolBar1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.origin_field.SetValue("(0, 0), 0")

        m_toolBar1.AddControl(self.origin_field)
        update_button = wx.Button(m_toolBar1, wx.ID_ANY, "update", wx.DefaultPosition, wx.DefaultSize, 0)

        m_toolBar1.AddControl(update_button)
        m_toolBar1.Realize()

        update_button.Bind(wx.EVT_BUTTON, self.update_origin)
        
        
        outer_sizer.Add(m_toolBar1, 0, wx.ALIGN_RIGHT, 5)


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



        button_cancel = wx.Button(toolbar, wx.ID_ANY, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_cancel)
        button_cancel.Bind(wx.EVT_BUTTON, self.cancel)

        button_apply = wx.Button(toolbar, wx.ID_ANY, "Apply", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_apply)
        button_apply.Bind(wx.EVT_BUTTON, self.apply)

        button_ok = wx.Button(toolbar, wx.ID_ANY, "Ok", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_ok)
        button_ok.Bind(wx.EVT_BUTTON, self.ok)


        self.place_elements(main_grid)


        self.Show()

    def update_origin(self, e):
        for element in self.ui_elements.list:
            if type(element) != str:
                for item in element.properties.get_items():
                    item.set_origin(item.python_eval(self.origin_field.GetValue()))

                element.update()

        #TODO: this has become a real mess
        for element in self.ui_elements.list:
            if type(element) != str:
                for item in element.properties.get_items():
                    item.python_env.update()

    def cancel(self, e):
        print("cancel")
        pass

    def apply(self, e):
        for element in self.ui_elements.list:
            if type(element) != str:
                if element.field_value != element.wx_field.GetValue():
                    element.put(element.wx_field.GetValue())

        pcbnew.Refresh()

    def ok(self, e):
        print("ok")
        pass

    def place_elements(self, parent):
        for element in self.ui_elements.list:
            self.place_element(parent, element)

    def place_element(self, parent, ui_element):
        if type(ui_element) == str:
            self.add_category(parent, ui_element)
        else:
            ui_element.wx_field = self.add_value(parent, ui_element.name, ui_element.field_value, ui_element.unit)
            self.add_icons(parent, ui_element.items.get_icons())

    def add_category(self, parent, name):
        staticText = wx.StaticText(self.scroll_box, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(staticText, 0, wx.ALL, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)


    def add_value(self, parent, name, value, unit = None):
        staticText = wx.StaticText(self.scroll_box, wx.ID_ANY, name + ":", wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(staticText, 0, wx.ALL, 5)

        if unit != None:
            box_unit_grid = wx.FlexGridSizer(0, 2, 0, 0)
            box_unit_grid.SetFlexibleDirection(wx.BOTH)
            box_unit_grid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

            input_field = wx.TextCtrl(self.scroll_box, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            box_unit_grid.Add(input_field, 0, wx.ALL|wx.EXPAND, 5)


            staticText = wx.StaticText(self.scroll_box, wx.ID_ANY, unit, wx.DefaultPosition, wx.DefaultSize, 0)
            staticText.Wrap(-1)

            box_unit_grid.Add(staticText, 0, wx.ALL, 5)

            parent.Add(box_unit_grid, 1, wx.EXPAND, 5)
        else:
            input_field = wx.TextCtrl(self.scroll_box, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            parent.Add(input_field, 0, wx.ALL|wx.EXPAND, 5)

        input_field.SetValue(value)

        return input_field


    def add_icons(self, parent, icons):
        icon_sizer = wx.BoxSizer(wx.HORIZONTAL)


        for icon in icons:
            path = os.path.join(os.path.dirname(__file__), "../resources/output/" + icon + ".png")
            bitmap = wx.StaticBitmap(self.scroll_box, wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(20,20), 0)
            icon_sizer.Add(bitmap, 0, wx.ALL, 0)

        parent.Add(icon_sizer, 1, wx.EXPAND, len(icons))




    def __del__(self):
        pass


