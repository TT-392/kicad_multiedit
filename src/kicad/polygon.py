import pcbnew
import math
from ..property import *

# footprint attributes:
# Footprint type:
#    0b00000: other
#    0b00001: through hole
#    0b00010: smd
# 0b10000: not in schematic
# 0b00100: exclude from position files
# 0b01000: exclude from bom

class GraphicPolygon:
    def __init__(self, obj):
        self.obj = obj
        self.width = self.__width(self)

        self.width_prop = Property("width", "Line", "length_unsigned", self.width, self)

        self.properties = Properties_array([
            self.width_prop
            ])


    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __width:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetWidth(value)

        def get(self):
            return self.s.obj.GetWidth()

