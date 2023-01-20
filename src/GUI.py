import wx
import wx.xrc
import os
import pcbnew
from .kicad.circle import *
from .gui.elements import *
from .ui_layout import *
from .selected import *


#GUI: Frame
#    outer_sizer: BoxSizer
#        self.scroll_box: ScrolledWindow
#            main_grid: flexGridSizer
#        toolbar: ToolBar


class GUI(wx.Dialog):
    def __init__(self, parent):
        #TODO: abstract away a bunch of wx stuff, also, move to gui

        wx.Dialog.__init__(self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(400,800), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)

        xml_resource = wx.xrc.XmlResource()
        xml_resource.Load(os.path.join(os.path.dirname(__file__), 'gui/gui.xrc'))


        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        
        panel = xml_resource.LoadObject(self, 'panel', 'wxPanel')
        outer_sizer.Add(panel, 1, wx.EXPAND)

        self.SetSizer(outer_sizer)


        button_cancel = wx.xrc.XRCCTRL(self, 'button_cancel')
        button_apply = wx.xrc.XRCCTRL(self, 'button_apply')
        button_ok = wx.xrc.XRCCTRL(self, 'button_ok')

        button_cancel.Bind(wx.EVT_BUTTON, self.cancel_pressed)
        button_apply.Bind(wx.EVT_BUTTON, self.apply_pressed)
        button_ok.Bind(wx.EVT_BUTTON, self.ok_pressed)



        self.scroll_box = wx.xrc.XRCCTRL(self, 'properties_scrollwindow')

        main_grid = wx.FlexGridSizer(0, 3, 0, 0)
        main_grid.SetFlexibleDirection(wx.BOTH)
        main_grid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        main_grid.Fit(self.scroll_box)

        self.scroll_box.SetSizer(main_grid)
        self.scroll_box.Layout()

        self.place_elements(main_grid)



        self.Show()

    def update_origin(self, e):
        #TODO: getting all items can be done using currently_selected
        for category in ui_layout:
            for name in ui_layout[category]:
                prop = ui_layout[category][name]
                if prop.is_active():
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

                if prop.is_active():
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

                prop.ui_element = add_control(self.scroll_box, parent, category_element, name, prop.varname, prop.get_ui_value(), prop.widget_type, prop.get_item_types())

                visibility = prop.is_active()

                prop.ui_element.set_visibility(visibility)


    def add_category(self, parent, name):
        staticText = wx.StaticText(self.scroll_box, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(staticText, 0, wx.ALL, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)
        parent.Add((0, 0), 1, wx.EXPAND, 5)


    def __del__(self):
        pass


