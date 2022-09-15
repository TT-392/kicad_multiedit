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

class GraphicCircle:
    def __init__(self, obj):
        self.obj = obj
        self.x = self.__x(self)
        self.y = self.__y(self)
        self.radius = self.__radius(self)
        self.width = self.__width(self)

        self.icon = "add_circle"

        self.x_prop = Property("X", "Position", "length", self.x, self)
        self.y_prop = Property("Y", "Position", "length", self.y, self)
        self.radius_prop = Property("Radius", "Shape", "length_unsigned", self.radius, self)
        self.width_prop = Property("width", "Line", "length_unsigned", self.width, self)

        self.properties = Properties_array([
            self.x_prop,
            self.y_prop,
            self.radius_prop,
            self.width_prop
            ])


    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __x:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetCenter(pcbnew.wxPoint(value, self.s.y.get()))

        def get(self):
            return self.s.obj.GetCenter().x

    class __y:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetCenter(pcbnew.wxPoint(self.s.x.get(), value))

        def get(self):
            return self.s.obj.GetCenter().y

    class __radius:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            centerX = self.s.obj.GetStartX()
            centerY = self.s.obj.GetStartY()
            self.s.obj.SetEndX(value + centerX)
            self.s.obj.SetEndY(centerY)

        def get(self):
            return self.s.obj.GetRadius()

    class __width:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetWidth(value)

        def get(self):
            return self.s.obj.GetWidth()

