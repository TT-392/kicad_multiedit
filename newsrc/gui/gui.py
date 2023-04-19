import wx
import wx.xrc
import os
import pcbnew



class Gui(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(400,800), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)

        # xml file containing the gui shell, except for the outer dialog box
        xml_resource = wx.xrc.XmlResource()
        xml_resource.Load(os.path.join(os.path.dirname(__file__), 'gui.xrc'))
        
        # we need a sizer to put the outer panel from the xml file into
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



        self.properties_scroll_box = wx.xrc.XRCCTRL(self, 'properties_scrollwindow')

        self.properties_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        self.properties_sizer.SetFlexibleDirection(wx.BOTH)
        self.properties_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.properties_sizer.Fit(self.properties_scroll_box)

        self.properties_scroll_box.SetSizer(self.properties_sizer)
        self.properties_scroll_box.Layout()



        self.test = wx.TextCtrl(self.properties_scroll_box)
        self.properties_sizer.Add(self.test, 0, wx.ALL|wx.EXPAND, 5)



        self.Show()


    def cancel_pressed(self, e):
        pass

    def apply_pressed(self, e):
        pass

    def ok_pressed(self, e):
        pass

        

