import math
from ..property import *
from ..item import *

# footprint attributes:
# Footprint type:
#    0b00000: other
#    0b00001: through hole
#    0b00010: smd
# 0b10000: not in schematic
# 0b00100: exclude from position files
# 0b01000: exclude from bom

class GraphicPolygon(Item):
    def __init__(self, obj):
        self.obj = obj
        self.width = self.to_user_unit(self, self.__width)

        self.icon = "add_graphical_polygon"

        self.width_prop = Property("width", "Line", "length_unsigned", self.width, self, "width")

        self.properties = Properties([
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

