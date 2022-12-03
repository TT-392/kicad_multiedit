import pcbnew
from ..property import *
from ..item import *
from ..gui.elements import *
from ..ui_layout import *

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
        self.not_in_schematic = self.__not_in_schematic(self)

        ui_layout["Position"]["X"].register(self.x)
        ui_layout["Position"]["Y"].register(self.y)
        ui_layout["Orientation"]["Angle"].register(self.orientation)
        ui_layout["Text Items"]["Ref"].register(self.reference)
        ui_layout["Fabrication Attributes"]["Not in schematic"].register(self.not_in_schematic)

        self.icon = "add_footprint"

    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __reference:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetReference(value)

        def get(self):
            return self.item.obj.GetReference()

    class __x:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetPosition(pcbnew.wxPoint(value, self.item.obj.GetPosition().y))

        def get(self):
            return self.item.obj.GetPosition().x

    class __y:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetPosition(pcbnew.wxPoint(self.item.obj.GetPosition().x, value))

        def get(self):
            return self.item.obj.GetPosition().y

    class __orientation:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetOrientation(value * 10)

        def get(self):
            return self.item.obj.GetOrientation() / 10

    class __not_in_schematic:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            attributes = self.item.obj.GetAttributes()

            if True:
                attributes |= 0b10000
            elif False:
                attributes &= ~0b10000
            else:
                assert 0, "value not True or False"

            self.item.obj.SetAttributes(attributes)


        def get(self):
            if self.item.obj.GetAttributes() & 0b10000:
                return True
            else:
                return False

