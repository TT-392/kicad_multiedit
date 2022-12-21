from src.kicad.kicad import *
from src.kicad.footprint import *
from src.item import *
from src.config import *
from src.selected import *
from tests.resources.kicad_footprint import *
from src.GUI import *
import wx

def gui():
    kicad_info.update()

    print("getting selected")
    currently_selected.update(True)

    print("initting python envs")
    i = 0
    for item in currently_selected.items.list:
        item.init_python_env(currently_selected.items, i)
        i += 1

    print("starting gui")
    app = wx.App(0)
    dialog = GUI(None)
    dialog.ShowModal()
    app.MainLoop()


