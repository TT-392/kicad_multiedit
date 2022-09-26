from ..property import *

# footprint attributes:
# Footprint type:
#    0b00000: other
#    0b00001: through hole
#    0b00010: smd
# 0b10000: not in schematic
# 0b00100: exclude from position files
# 0b01000: exclude from bom

class GraphicText:
    def __init__(self, obj):
        self.obj = obj
        self.text = self.__text(self)
        self.x = self.__x(self)
        self.y = self.__y(self)
        self.textWidth = self.__textWidth(self)
        self.textHeight = self.__textHeight(self)
        self.width = self.__width(self)
        self.orientation = self.__orientation(self)

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

        self.properties = Properties_array([
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
            self.s.obj.SetTextAngle(value)

        def get(self):
            return self.s.obj.GetTextAngle()

