import wx

class Test_kicad_footprint:
    def __init__(self):
        self.ref = ""
        self.x = 0
        self.y = 0
        self.rot = 0

    def SetReference(self, value):
        self.ref = value

    def GetReference(self):
        return self.ref

    def SetPosition(self, value):
        self.x = value.x

    def GetPosition(self):
        return wx.Point((self.x, self.y))

    def SetOrientation(self, value):
        self.rot = value

    def GetOrientation(self):
        return self.rot

