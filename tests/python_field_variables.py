from src.kicad.kicad import *
from src.kicad.footprint import *
from src.item import *
from tests.resources.kicad_footprint import *
from src.GUI import *
from src.ui_elements import *
from src.field_evaluation.python_env import *
import wx

def python_field_variables():
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

    selected.get_properties()
    python_env = Python_env(selected, footprint1, 5)
    python_env.update()

    print("x:", python_env.eval("x"))
    print("y:", python_env.eval("y"))
    print("rot:", python_env.eval("y"))
    print("900*(y*x + 5):", python_env.eval("900*(y*x + 5)"))



