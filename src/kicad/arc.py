import pcbnew
from kicad import *
from ..property import *
from ..item import *
from ..gui.elements import *

class GraphicArc(Item):
    def __init__(self, obj):
        self.obj = obj
        self.startX = self.translated_x(self, self.__startX, self.__startY)
        self.startY = self.translated_y(self, self.__startY, self.__startX)
        self.endX = self.translated_x(self, self.__endX, self.__endY)
        self.endY = self.translated_y(self, self.__endY, self.__endX)
        self.arcAngle = self.__arcAngle(self)
        self.width = self.to_user_unit(self, self.__width)
        self.layer = self.__layer(self)

        self.icon = "add_arc"

        self.startX_prop = Property("startX", "Points", Type_python(kicad_info.unit_string), self.startX, self, "x1")
        self.startY_prop = Property("startY", "Points", Type_python(kicad_info.unit_string), self.startY, self, "y1")
        self.startX_prop.y_prop = self.startY_prop
        self.startY_prop.x_prop = self.startX_prop

        self.endX_prop = Property("endX", "Points", Type_python(kicad_info.unit_string), self.endX, self, "x2")
        self.endY_prop = Property("endY", "Points", Type_python(kicad_info.unit_string), self.endY, self, "y2")
        self.endX_prop.y_prop = self.endY_prop
        self.endY_prop.x_prop = self.endX_prop

        self.arcAngle_prop = Property("arcangle", "Line", Type_python(), self.arcAngle, self, "arcAngle")
        self.width_prop = Property("width", "Line", Type_python(), self.width, self, "width")
        self.layer_prop = Property("Layer", "Miscellaneous", Type_dropdown(kicad_info.get_layers()), self.layer, self, "Layer")

        self.properties = Properties([
            self.startX_prop,
            self.startY_prop,
            self.endX_prop,
            self.endY_prop,
            self.arcAngle_prop,
            self.width_prop,
            self.layer_prop
            ])


    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __startX:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetStartX(value)

        def get(self):
            return self.item.obj.GetStartX()

    class __startY:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetStartY(value)

        def get(self):
            return self.item.obj.GetStartY()

    class __endX:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetEndX(value)

        def get(self):
            return self.item.obj.GetEndX()

    class __endY:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetEndY(value)

        def get(self):
            return self.item.obj.GetEndY()

    class __arcAngle:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetArcAngleAndEnd(value * 10)

        def get(self):
            return self.item.obj.GetArcAngle() / 10

    class __width:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetWidth(value)

        def get(self):
            return self.item.obj.GetWidth()

    class __layer:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetLayer(kicad_info.get_layer_id(value))

        def get(self):
            return pcbnew.LayerName(self.item.obj.GetLayer())
