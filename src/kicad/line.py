from ..property import *
from ..item import *
from ..gui.elements import *

# footprint attributes:
# Footprint type:
#    0b00000: other
#    0b00001: through hole
#    0b00010: smd
# 0b10000: not in schematic
# 0b00100: exclude from position files
# 0b01000: exclude from bom

class GraphicLine(Item):
    def __init__(self, obj):
        self.obj = obj
        self.startX = self.translated_x(self, self.__startX, self.__startY)
        self.startY = self.translated_y(self, self.__startY, self.__startX)
        self.endX = self.translated_x(self, self.__endX, self.__endY)
        self.endY = self.translated_y(self, self.__endY, self.__endX)
        self.width = self.to_user_unit(self, self.__width)

        self.icon = "add_line"

        self.startX_prop = Property("startX", "Points", Type_python(kicad_info.unit_string), self.startX, self, "x1")
        self.startY_prop = Property("startY", "Points", Type_python(kicad_info.unit_string), self.startY, self, "y1")
        self.startX_prop.y_prop = self.startY_prop
        self.startY_prop.x_prop = self.startX_prop

        self.endX_prop = Property("endX", "Points", Type_python(kicad_info.unit_string), self.endX, self, "x2")
        self.endY_prop = Property("endY", "Points", Type_python(kicad_info.unit_string), self.endY, self, "y2")
        self.endX_prop.y_prop = self.endY_prop
        self.endY_prop.x_prop = self.endX_prop

        self.width_prop = Property("width", "Line", Type_python(), self.width, self, "width")

        self.properties = Properties([
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

