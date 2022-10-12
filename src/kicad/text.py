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

class GraphicText(Item):
    def __init__(self, obj):
        self.obj = obj
        self.text = self.__text(self)
        self.x = self.translated_x(self, self.__x, self.__y)
        self.y = self.translated_y(self, self.__y, self.__x)
        self.textWidth = self.to_user_unit(self, self.__textWidth)
        self.textHeight = self.to_user_unit(self, self.__textHeight)
        self.width = self.to_user_unit(self, self.__width)
        self.orientation = self.translated_orientation(self, self.__orientation)

        self.icon = "text"

        self.text_prop = Property("Text", "Strings", "string", self.text, self)
        self.x_prop = Property("X", "Position", "length", self.x, self, "x", "x")
        self.y_prop = Property("Y", "Position", "length", self.y, self, "y", "y")
        self.x_prop.y_prop = self.y_prop
        self.y_prop.x_prop = self.x_prop

        self.textWidth_prop = Property("Width", "Text", "length_unsigned", self.textWidth, self, "textWidth")
        self.textHeight_prop = Property("Height", "Text", "length_unsigned", self.textHeight, self, "textHeight")
        self.width_prop = Property("Width", "Line", "length_unsigned", self.width, self, "width")
        self.orientation_prop = Property("Angle", "Orientation", "angle", self.orientation, self, "rot", "rot")

        self.properties = Properties([
            self.text_prop,
            self.x_prop,
            self.y_prop,
            self.textWidth_prop,
            self.textHeight_prop,
            self.width_prop,
            self.orientation_prop
            ])


    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __text:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetText(value)

        def get(self):
            return self.s.obj.GetText()

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

    class __textWidth:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetTextWidth(value)

        def get(self):
            return self.s.obj.GetTextWidth()

    class __textHeight:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetTextHeight(value)

        def get(self):
            return self.s.obj.GetTextHeight()

    class __width:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetTextThickness(value)

        def get(self):
            return self.s.obj.GetTextThickness()

    class __orientation:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetTextAngle(value * 10)

        def get(self):
            return self.s.obj.GetTextAngle() / 10

