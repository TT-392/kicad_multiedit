from ..property import *
from ..item import *
from ..gui.elements import *

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
        self.layer = self.__layer(self)

        self.icon = "text"

        self.text_prop = Property("Text", "Strings", Type_string(), self.text, self, "text")
        self.x_prop = Property("X", "Position", Type_python(kicad_info.unit_string), self.x, self, "x")
        self.y_prop = Property("Y", "Position", Type_python(kicad_info.unit_string), self.y, self, "y")
        self.x_prop.y_prop = self.y_prop
        self.y_prop.x_prop = self.x_prop

        self.textWidth_prop = Property("Width", "Text", Type_python(), self.textWidth, self, "textWidth")
        self.textHeight_prop = Property("Height", "Text", Type_python(), self.textHeight, self, "textHeight")
        self.width_prop = Property("width", "Line", Type_python(), self.width, self, "width")
        self.orientation_prop = Property("Angle", "Orientation", Type_python(), self.orientation, self, "rot")

        self.layer_prop = Property("Layer", "Miscellaneous", Type_dropdown(kicad_info.get_layers()), self.layer, self, "Layer")

        self.properties = Properties([
            self.text_prop,
            self.x_prop,
            self.y_prop,
            self.textWidth_prop,
            self.textHeight_prop,
            self.width_prop,
            self.orientation_prop,
            self.layer_prop
            ])


    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __text:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetText(value)

        def get(self):
            return self.item.obj.GetText()

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

    class __textWidth:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetTextWidth(value)

        def get(self):
            return self.item.obj.GetTextWidth()

    class __textHeight:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetTextHeight(value)

        def get(self):
            return self.item.obj.GetTextHeight()

    class __width:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetTextThickness(value)

        def get(self):
            return self.item.obj.GetTextThickness()

    class __orientation:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetTextAngle(value * 10)

        def get(self):
            return self.item.obj.GetTextAngle() / 10

    class __layer:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetLayer(kicad_info.get_layer_id(value))

        def get(self):
            return pcbnew.LayerName(self.item.obj.GetLayer())
