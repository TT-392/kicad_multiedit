from src.kicad.kicad import *
from src.kicad.footprint import *
from src.item import *
from tests.resources.kicad_footprint import *
from src.GUI import *
from src.ui_properties import *
import wx

def  gui():
    kicad_info.update()

    test_footprint = Test_kicad_footprint()
    test_footprint.ref = "aaa"
    test_footprint.x = kicad_info.fromUnit(4)
    test_footprint.y = kicad_info.fromUnit(9)
    test_footprint.rot = 900

    footprint1 = Footprint(test_footprint)

    test_footprint = Test_kicad_footprint()
    test_footprint.ref = "aba"
    test_footprint.x = kicad_info.fromUnit(3)
    test_footprint.y = kicad_info.fromUnit(9)
    test_footprint.rot = 800

    footprint2 = Footprint(test_footprint)

    selected = Items([footprint1, footprint2])

    app = wx.App(0)
    GUI(None, Ui_elements(selected.get_properties()))
    app.MainLoop()

