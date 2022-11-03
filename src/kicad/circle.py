import math
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

class GraphicCircle(Item):
    def __init__(self, obj):
        self.obj = obj
        self.x = self.translated_x(self, self.__x, self.__y)
        self.y = self.translated_y(self, self.__y, self.__x)
        self.radius = self.to_user_unit(self, self.__radius)
        self.width = self.to_user_unit(self, self.__width)
        self.layer = self.__layer(self)

        self.icon = "add_circle"

        self.x_prop = Property("X", "Position", Type_python(kicad_info.unit_string), self.x, self, "x")
        self.y_prop = Property("Y", "Position", Type_python(kicad_info.unit_string), self.y, self, "y")
        self.x_prop.y_prop = self.y_prop
        self.y_prop.x_prop = self.x_prop

        self.radius_prop = Property("Radius", "Shape", Type_python(), self.radius, self, "r")
        self.width_prop = Property("width", "Line", Type_python(), self.width, self, "width")
        self.layer_prop = Property("Layer", "Miscellaneous", Type_dropdown(kicad_info.get_layers()), self.layer, self, "Layer")

        self.properties = Properties([
            self.x_prop,
            self.y_prop,
            self.radius_prop,
            self.width_prop,
            self.layer_prop
            ])


    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __x:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetPosition(pcbnew.wxPoint(value, self.s.obj.GetCenter().y))

        def get(self):
            return self.s.obj.GetPosition().x

    class __y:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetPosition(pcbnew.wxPoint(self.s.obj.GetCenter().x, value))

        def get(self):
            return self.s.obj.GetPosition().y

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

    class __layer:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetLayer(kicad_info.get_layer_id(value))

        def get(self):
            return pcbnew.LayerName(self.s.obj.GetLayer())
