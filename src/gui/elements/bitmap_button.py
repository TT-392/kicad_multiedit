def draw_bitmap_button(parent_window, parent, icon):
    icon_sizer = wx.BoxSizer(wx.HORIZONTAL)

    icon = icon
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


