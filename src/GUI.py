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
    def __init__(self, parent):
        #TODO: abstract away a bunch of wx stuff, also, move to gui

        wx.Dialog.__init__(self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(400,800), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(outer_sizer)
        self.Layout()

        self.draw_selector_buttons(self, outer_sizer, ["add_circle"])
        self.draw_selector_buttons(self, outer_sizer, ["add_circle"])
        self.draw_selector_buttons(self, outer_sizer, ["add_circle"])


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
        #TODO: getting all items can be abstracted
        for category in ui_layout:
            for name in ui_layout[category]:
                prop = ui_layout[category][name]
                if prop.is_visible():
                    for item in prop.get_items():
                        item.set_origin(item.python_eval(self.origin_field.GetValue()))


                    prop.update_ui_value()

    def cancel_pressed(self, e):
        print("cancel")
        self.Close()

    def apply(self):
        update = False

        props_needing_update = []

        for category in ui_layout:
            for name in ui_layout[category]:
                prop = ui_layout[category][name]

                if prop.is_visible():
                    new_ui_value = prop.ui_element.get_value()

                    if prop.get_ui_value() != new_ui_value:
                        props_needing_update.append(prop)

        for prop in props_needing_update:
            for item in prop.get_items():
                item.python_env.reset()

        for prop in props_needing_update:
            new_ui_value = prop.ui_element.get_value()
            prop.prepare_variables(new_ui_value)

        for prop in props_needing_update:
            print("new ui val", new_ui_value)
            prop.put_ui_value(new_ui_value)
                            
        if len(props_needing_update) > 0:
            pcbnew.Refresh()

    def apply_pressed(self, e):
        self.apply()

    def ok_pressed(self, e):
        self.apply()
        self.Close()

    def place_elements(self, parent):
        for category in ui_layout:
            first_prop_in_category = True

            for name in ui_layout[category]:
                prop = ui_layout[category][name]

                if first_prop_in_category:
                    category_element = passive_category(self.scroll_box, parent, category)
                    first_prop_in_category = False

                prop.ui_element = add_control(self.scroll_box, parent, category_element, name, prop.varname, prop.get_ui_value(), prop.widget_type, prop.get_icons())

                visibility = prop.is_visible()

                prop.ui_element.set_visibility(visibility)


    def add_category(self, parent, name):
        staticText = wx.StaticText(self.scroll_box, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(staticText, 0, wx.ALL, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)


    def draw_selector_buttons(self, parent_window, parent, icons):
        icon_sizer = wx.BoxSizer(wx.HORIZONTAL)

        icon = icons[0]
        sys_appearance = wx.SystemSettings.GetAppearance()
        theme = "dark" if sys_appearance.IsDark() else "light"

        
        #button thing
        wSizer2 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        parent.Add(wSizer2, 10)
        
        m_panel1 = wx.Panel(parent_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        m_panel1.SetBackgroundColour(wx.Colour(21, 81, 158))
        wSizer2.Add(m_panel1, 10)
        
        wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        m_panel1.SetSizer(wSizer1)

        m_panel0 = wx.Panel(m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        m_panel0.SetBackgroundColour(wx.Colour(8, 33, 63))
        wSizer1.Add(m_panel0, 1, wx.EXPAND|wx.ALL, 1)


        wSizer2 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        m_panel0.SetSizer(wSizer2)

        path = os.path.join(os.path.dirname(__file__), "../resources/output/" + theme + "/" + icon + ".png")
        icon = wx.StaticBitmap(m_panel0, wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(20,20), 0)

        wSizer2.Add(icon, 0, wx.EXPAND|wx.ALL, 2)

    def __del__(self):
        pass


