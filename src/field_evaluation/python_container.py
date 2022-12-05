import math
import pcbnew
from ..kicad.kicad import *
from ..item import *

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def atan(x):
    return math.atan(x)

def asin(x):
    if x > 1:
        x = 1 
    elif x < -1:
        x = -1

    return math.asin(x)

def acos(x):
    if x > 1:
        x = 1 
    elif x < -1:
        x = -1

    return math.acos(x)

def snap(x, amount):
    x = x / amount
    x = round(x, 0)
    return x * amount

def prefix(designator):
    retval = ""

    for c in designator:
        if c in "0123456789":
            break
        retval += c

    return retval

def postfix(designator):
    retval = ""

    for c in designator[::-1]:
        if not c in "0123456789":
            break
        retval = c + retval

    return int(retval)



# TODO: Eventually I want the normal function to accept self or just have a normal variable for any item with an x1, y1, x2 and y2
def normal(x1, y1, x2, y2):
    x_distance = x2 - x1
    y_distance = y2 - y1
    angle = math.degrees(math.atan2(x_distance, y_distance))
    normal = angle - 90

    if normal < 0:
        normal += 360

    return normal


class fp:
    def __init__(self, prefix, postfix):
        found = False
        pcb = kicad_info.get_board()
        for footprint in pcb.GetFootprints():
            if footprint.GetReference() == prefix + str(postfix):
                self.footprint = footprint
                found = True
                break
        
        if not found:
            print("footprint not found")
            return

        position = self.footprint.GetPosition()
        self.x = kicad_info.toUnit(position.x)
        self.y = kicad_info.toUnit(position.y)
        self.rot = self.footprint.GetOrientation() / 10
        self.origin = (self.x, self.y), self.rot



def eval_in_container(defines_string, string):
    exec(defines_string)

    return eval(string)

