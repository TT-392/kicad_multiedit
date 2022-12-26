import wx
import os
from ...utils import *

class draw_bitmap_button:
    def __init__(self, parent_window, parent, icon_type, depressed, update_func):
        icon_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.depressed = depressed
        self.hover = False
        self.click = False
        self.update_func = update_func
        
        wSizer0 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        parent.Add(wSizer0, 10)
        
        self.edge = wx.Panel(parent_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        wSizer0.Add(self.edge, 10)
        
        wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        self.edge.SetSizer(wSizer1)

        self.button = wx.Panel(self.edge, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        wSizer1.Add(self.button, 1, wx.EXPAND|wx.ALL, 1)

        self.button.Bind(wx.EVT_ENTER_WINDOW, self.mouse_enter)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.mouse_leave)
        self.button.Bind(wx.EVT_LEFT_DOWN, self.mouse_down)
        self.button.Bind(wx.EVT_LEFT_UP, self.mouse_up)

        self.render_passive()

        wSizer2 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        self.button.SetSizer(wSizer2)

        path = utils.get_item_icon_path(icon_type)
        icon = wx.StaticBitmap(self.button, wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(20,20), 0)

        icon.Bind(wx.EVT_LEFT_DOWN, self.mouse_down)
        icon.Bind(wx.EVT_LEFT_UP, self.mouse_up)

        wSizer2.Add(icon, 0, wx.EXPAND|wx.ALL, 2)

    def get_value(self):
        return self.depressed


    def mouse_enter(self, e):
        self.hover = True
        self.render_update()


    def mouse_leave(self, e):
        self.hover = False
        self.render_update()


    def mouse_down(self, e):
        self.click = True
        self.render_update()


    def mouse_up(self, e):
        self.click = False 
        self.render_update()

        if self.hover:
            self.depressed = not self.depressed
            self.update_func()


    def render_update(self):
        if self.hover and self.click:
            self.render_click()

        elif self.hover and not self.click:
            self.render_hover()

        elif not self.hover:
            self.render_passive()


    def render_hover(self):
        if self.depressed:
            self.edge.SetBackgroundColour(wx.Colour(0x15, 0x53, 0x9e))
            self.button.SetBackgroundColour(wx.Colour(0x0A, 0x29, 0x4f))
        else:
            self.button.SetBackgroundColour(wx.Colour(0x08, 33, 63))
            self.edge.SetBackgroundColour(wx.Colour(0x15, 0x53, 0x9e))

    def render_click(self):
        self.button.SetBackgroundColour(wx.Colour(0x04, 0x10, 0x1f))
        self.edge.SetBackgroundColour(wx.Colour(0x15, 0x53, 0x9e))

    def render_passive(self):
        if self.depressed:
            self.button.SetBackgroundColour(wx.Colour(0x08, 33, 63))
            self.edge.SetBackgroundColour(wx.Colour(0x15, 0x53, 0x9e))
        else:
            self.button.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
            self.edge.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
