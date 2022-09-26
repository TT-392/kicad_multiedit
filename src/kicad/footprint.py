from ..property import *

# footprint attributes:
# Footprint type:
#    0b00000: other
#    0b00001: through hole
#    0b00010: smd
# 0b10000: not in schematic
# 0b00100: exclude from position files
# 0b01000: exclude from bom

class Footprint:
    def __init__(self, obj):
        self.obj = obj
        self.reference = self.__reference(self)
        self.x = self.__x(self)
        self.y = self.__y(self)
        self.orientation = self.__orientation(self)

        self.icon = "add_footprint"

        self.x_prop = Property("X", "Position", "length", self.x, self, "x", "x")
        self.y_prop = Property("Y", "Position", "length", self.y, self, "y", "y")
        self.x_prop.y_prop = self.y_prop
        self.y_prop.x_prop = self.x_prop

        self.ref_prop = Property("Ref", "Strings", "string", self.reference, self)
        self.orientation_prop = Property("Angle", "Orientation", "angle", self.orientation, self, "Rot", "rot")

        self.properties = Properties_array([
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
            self.s.obj.SetPosition(pcbnew.wxPoint(value, self.s.y.get()))

        def get(self):
            return self.s.obj.GetPosition().x

    class __y:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetPosition(pcbnew.wxPoint(self.s.x.get(), value))

        def get(self):
            return self.s.obj.GetPosition().y

    class __orientation:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetOrientation(value)

        def get(self):
            return self.s.obj.GetOrientation()

