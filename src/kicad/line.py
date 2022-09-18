import pcbnew
from ..property import *

# footprint attributes:
# Footprint type:
#    0b00000: other
#    0b00001: through hole
#    0b00010: smd
# 0b10000: not in schematic
# 0b00100: exclude from position files
# 0b01000: exclude from bom

class GraphicLine:
    def __init__(self, obj):
        self.obj = obj
        self.startX = self.__startX(self)
        self.startY = self.__startY(self)
        self.endX = self.__endX(self)
        self.endY = self.__endY(self)
        self.width = self.__width(self)

        self.icon = "add_line"

        self.startX_prop = Property("startX", "Points", "length", self.startX, self, "x1")
        self.startY_prop = Property("startY", "Points", "length", self.startY, self, "y1")
        self.endX_prop = Property("endX", "Points", "length", self.endX, self, "x2")
        self.endY_prop = Property("endY", "Points", "length", self.endY, self, "y2")
        self.width_prop = Property("width", "Line", "length_unsigned", self.width, self)

        self.properties = Properties_array([
            self.startX_prop,
            self.startY_prop,
            self.endX_prop,
            self.endY_prop,
            self.width_prop
            ])


    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __startX:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetStartX(value)

        def get(self):
            return self.s.obj.GetStartX()

    class __startY:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetStartY(value)

        def get(self):
            return self.s.obj.GetStartY()

    class __endX:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetEndX(value)

        def get(self):
            return self.s.obj.GetEndX()

    class __endY:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetEndY(value)

        def get(self):
            return self.s.obj.GetEndY()


    class __width:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetWidth(value)

        def get(self):
            return self.s.obj.GetWidth()

