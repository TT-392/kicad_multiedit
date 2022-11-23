import wx
import os

class Control:
    def __init__(self):
        self.wx_elements = []

    def set_visibility(self, value):
        if value:
            for element in self.wx_elements:
                element.Show()

            self.category.add_visible_control(self)

        else:
            for element in self.wx_elements:
                element.Hide()

            self.category.drop_visible_control(self)


    def add_icons(self, parent_window, parent, icons):
        icon_sizer = wx.BoxSizer(wx.HORIZONTAL)

        for icon in icons:
            sys_appearance = wx.SystemSettings.GetAppearance()
            theme = "dark" if sys_appearance.IsDark() else "light"

            path = os.path.join(os.path.dirname(__file__), "../../../resources/output/" + theme + "/" + icon + ".png")
            icon = wx.StaticBitmap(parent_window, wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(20,20), 0)
            icon_sizer.Add(icon, 0, wx.ALL, 0)
            self.wx_elements.append(icon)

        parent.Add(icon_sizer, 1, wx.EXPAND, len(icons))


