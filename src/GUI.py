import os
import wx
import wx.xrc

#GUI: Frame
#    outer_sizer: BoxSizer
#        self.scroll_box: ScrolledWindow
#            main_grid: flexGridSizer
#        toolbar: ToolBar



class GUI(wx.Frame):
    def __init__(self, parent, ui_elements):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(400,800), style = wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)

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



        button_cancel = wx.Button(toolbar, wx.ID_ANY, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_cancel)

        button_apply = wx.Button(toolbar, wx.ID_ANY, "Apply", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_apply)

        button_save = wx.Button(toolbar, wx.ID_ANY, "Save", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_save)





        for element in ui_elements.list:
            if type(element) == str:
                self.add_category(main_grid, element)
            else:
                self.add_value(main_grid, element.name, element.ui_value, element.unit)
                self.add_icons(main_grid, element.items.get_icons())





        self.Show()

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
            print("None")
            input_field = wx.TextCtrl(self.scroll_box, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            parent.Add(input_field, 0, wx.ALL|wx.EXPAND, 5)

        input_field.SetValue(value)



    def add_icons(self, parent, icons):
        icon_sizer = wx.BoxSizer(wx.HORIZONTAL)


        for icon in icons:
            path = os.path.join(os.path.dirname(__file__), "../resources/output/" + icon + ".png")
            bitmap = wx.StaticBitmap(self.scroll_box, wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(20,20), 0)
            icon_sizer.Add(bitmap, 0, wx.ALL, 0)

        parent.Add(icon_sizer, 1, wx.EXPAND, len(icons))



    def __del__(self):
        pass


