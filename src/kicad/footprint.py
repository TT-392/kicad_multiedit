import pcbnew
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

class Footprint(Item):
    def __init__(self, obj):
        self.obj = obj
        self.reference = self.__reference(self)
        self.x = self.translated_x(self, self.__x, self.__y)
        self.y = self.translated_y(self, self.__y, self.__x)
        self.orientation = self.translated_orientation(self, self.__orientation)

        self.icon = "add_footprint"

        self.x_prop = Property("X", "Position", "length", self.x, self, "x", "x")
        self.y_prop = Property("Y", "Position", "length", self.y, self, "y", "y")
        self.x_prop.y_prop = self.y_prop
        self.y_prop.x_prop = self.x_prop

        self.ref_prop = Property("Ref", "Strings", "string", self.reference, self, "ref")
        self.orientation_prop = Property("Angle", "Orientation", "angle", self.orientation, self, "rot", "rot")

        self.properties = Properties([
            self.x_prop,
            self.y_prop,
            self.ref_prop,
            self.orientation_prop
            ])

    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __reference:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetReference(value)

        def get(self):
            return self.s.obj.GetReference()

    class __x:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetPosition(pcbnew.wxPoint(value, self.s.obj.GetPosition().y))

        def get(self):
            return self.s.obj.GetPosition().x

    class __y:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetPosition(pcbnew.wxPoint(self.s.obj.GetPosition().x, value))

        def get(self):
            return self.s.obj.GetPosition().y

    class __orientation:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetOrientation(value * 10)

        def get(self):
            return self.s.obj.GetOrientation() / 10

