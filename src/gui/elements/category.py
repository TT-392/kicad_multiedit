import wx

class passive_category():
    def __init__(self, parent_window, parent, title):
        self.visible_controls = set([])
        self.wx_elements = set([])

        staticText = wx.StaticText(parent_window, wx.ID_ANY, title, wx.DefaultPosition, wx.DefaultSize, 0)

        spacer1 = wx.StaticText(parent_window, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0)
        spacer2 = wx.StaticText(parent_window, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0)

        parent.Add(staticText)
        parent.Add(spacer1)
        parent.Add(spacer2)
        self.wx_elements.add(staticText)
        self.wx_elements.add(spacer1)
        self.wx_elements.add(spacer2)
        
        self.__set_visibility(False)

    def add_visible_control(self, control):
        self.visible_controls.add(control)
        self.__set_visibility(True)

    def drop_visible_control(self, control):
        if not control in self.visible_controls:
            return

        self.visible_controls.remove(control)

        self.__set_visibility(False)

    def __set_visibility(self, value):
        if value:
            for element in self.wx_elements:
                element.Show()
        else:
            for element in self.wx_elements:
                element.Hide()
