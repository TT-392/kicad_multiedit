import os
import wx
import wx.xrc
import pcbnew
from .gui.elements import *
from .ui_layout import *


#GUI: Frame
#    outer_sizer: BoxSizer
#        self.scroll_box: ScrolledWindow
#            main_grid: flexGridSizer
#        toolbar: ToolBar


class GUI(wx.Dialog):
    def __init__(self, parent, ui_elements):
        #TODO: abstract away a bunch of wx stuff
        self.ui_elements = ui_elements

        wx.Dialog.__init__(self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(400,800), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)

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
        button_cancel.Bind(wx.EVT_BUTTON, self.cancel_pressed)

        button_apply = wx.Button(toolbar, wx.ID_ANY, "Apply", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_apply)
        button_apply.Bind(wx.EVT_BUTTON, self.apply_pressed)

        button_ok = wx.Button(toolbar, wx.ID_ANY, "Ok", wx.DefaultPosition, wx.DefaultSize, 0)
        toolbar.AddControl(button_ok)
        button_ok.Bind(wx.EVT_BUTTON, self.ok_pressed)


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

    def cancel_pressed(self, e):
        print("cancel")
        self.Close()

    def apply(self):
        update = False
        for element in self.ui_elements.list:
            if type(element) != str:
                if element.field_value != element.widget_obj.GetValue():
                    update = True
                    element.put(element.widget_obj.GetValue())

        if update:
            pcbnew.Refresh()

    def apply_pressed(self, e):
        self.apply()

    def ok_pressed(self, e):
        self.apply()
        self.Close()

    def place_elements(self, parent):
        for category in ui_layout:
            self.add_category(parent, category)

            for name in ui_layout[category]:
                prop = ui_layout[category][name]
                add_control(self.scroll_box, parent, name, prop.varname, prop.get_ui_value(), prop.widget_type)
                self.add_icons(parent, prop.get_icons())


        #for element in self.ui_elements.list:
        #    self.place_element(parent, element)

    def place_element(self, parent, ui_element):
        if type(ui_element) == str:
            self.add_category(parent, ui_element)
        else:
            ui_element.widget_obj = add_control(self.scroll_box, parent, ui_element.name, "aa", ui_element.field_value, ui_element.widget_type)
            self.add_icons(parent, ui_element.items.get_icons())

    def add_category(self, parent, name):
        staticText = wx.StaticText(self.scroll_box, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(staticText, 0, wx.ALL, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)

    def add_icons(self, parent, icons):
        icon_sizer = wx.BoxSizer(wx.HORIZONTAL)


        for icon in icons:
            sys_appearance = wx.SystemSettings.GetAppearance()
            theme = "dark" if sys_appearance.IsDark() else "light"

            path = os.path.join(os.path.dirname(__file__), "../resources/output/" + theme + "/" + icon + ".png")
            bitmap = wx.StaticBitmap(self.scroll_box, wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(20,20), 0)
            icon_sizer.Add(bitmap, 0, wx.ALL, 0)

        parent.Add(icon_sizer, 1, wx.EXPAND, len(icons))



    def __del__(self):
        pass


