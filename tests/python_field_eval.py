import math
from src.kicad.kicad import *
from src.utils import *
from src.kicad.footprint import *
from src.get_selected import *
from src.item import *
from tests.resources.kicad_footprint import *
from src.GUI import *
from src.field_evaluation.python_env import *
import wx

def check(expected, item, string):
    item.python_env.prepare_variables(string)
    result = item.python_eval(string)

    item.python_env.prepare_variables(string)
    result = item.python_eval(string)

    assert expected == result, "expected_result: " + utils.to_parseable_string(expected) + " but got: " + utils.to_parseable_string(result) + " when evaluating " + utils.to_parseable_string(string)


def expected_results(item):
    # defaults:
    retval = {
        "x" : 0,
        "y" : 0,
        "rot" : 0,
        "x1" : 0,
        "y1" : 0,
        "x2" : 0,
        "y2" : 0,
        "arcAngle" : 0,
        "width" : 0,
        "radius" : 0,
        "text" : 0,
        "width" : 0,
        "height" : 0,
        "ref" : 0,
        "not_in_schematic" : 0,
        "layer" : 0,
        "visible" : 0
    }

    if "x" in item.values:
        retval["x"] = item.x.get()

    if "y" in item.values:
        retval["y"] = item.y.get()

    if "rot" in item.values:
        retval["rot"] = item.orientation.get()

    if "x1" in item.values:
        retval["x1"] = item.startX.get()

    if "y1" in item.values:
        retval["y1"] = item.startY.get()

    if "x2" in item.values:
        retval["x2"] = item.endX.get()

    if "y2" in item.values:
        retval["y2"] = item.endY.get()

    if "arcAngle" in item.values:
        retval["arcAngle"] = item.ArcAngle.get()

    if "width" in item.values:
        retval["width"] = item.width.get()

    if "radius" in item.values:
        retval["radius"] = item.radius.get()

    if "text" in item.values:
        retval["text"] = item.text.get()

    if "width" in item.values:
        retval["width"] = item.width.get()

    if "height" in item.values:
        retval["height"] = item.textWidth.get()

    if "ref" in item.values:
        retval["ref"] = item.reference.get()

    if "not_in_schematic" in item.values:
        retval["not_in_schematic"] = item.not_in_schematic.get()

    if "layer" in item.values:
        retval["layer"] = item.layer.get()

    if "visible" in item.values:
        retval["visible"] = item.visible.get()

    return retval

def number_bounds(Min, Max, x):
    if x > Max:
        return Max
    elif x < Min:
        return Min
    else:
        return x

def python_field_eval():
    kicad_info.update()

    selected = get_selected(True)
    
    i = 0
    for item in selected.list:
        item.init_python_env(selected, i)
        i += 1


    i = 0
    for item in selected.list:
        expected = expected_results(item)

        for string in expected:
            check(expected[string], item, string)

        check(expected["x"] + expected["y"], item, "x+y")
        check(expected["x"] + expected["y"], item, " x  + y # fwlakfjwea ")

        expected_result = math.sqrt(expected["x1"])
        expected_result +=  math.sin(expected["x2"])
        expected_result +=  math.cos(expected["y1"])
        expected_result +=  math.tan(expected["y2"])
        expected_result +=  math.atan(expected["x"])
        expected_result +=  math.asin(number_bounds(-1, 1, expected["y"]))
        expected_result +=  math.acos(number_bounds(-1, 1, expected["rot"]))

        check(expected_result, item, "sqrt(x1) + sin(x2) + cos(y1) + tan(y2) + atan(x) + asin(y) + acos(rot)")

        check(i, item, "i")

        i += 1



