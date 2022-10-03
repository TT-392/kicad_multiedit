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
    return math.asin(x)

def acos(x):
    return math.acos(x)

def snap(x, amount):
    x = x / amount
    x = round(x, 0)
    return x * amount

class fp:
    def __init__(self, prefix, postfix):
        found = False
        pcb = pcbnew.GetBoard()
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

