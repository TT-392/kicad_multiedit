import math
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

class GraphicCircle(Item):
    def __init__(self, obj):
        self.obj = obj
        self.x = self.translated_x(self, self.__x, self.__y)
        self.y = self.translated_y(self, self.__y, self.__x)
        self.radius = self.to_user_unit(self, self.__radius)
        self.width = self.to_user_unit(self, self.__width)
        self.layer = self.__layer(self)

        self.values = {
            ui_layout["Position"]["X"].register(self.x).varname: self.x,
            ui_layout["Position"]["Y"].register(self.y).varname: self.y,
            ui_layout["Graphic"]["Radius"].register(self.radius).varname: self.radius,
            ui_layout["Graphic"]["Line width"].register(self.width).varname: self.width,
            ui_layout["Miscellaneous"]["Layer"].register(self.layer).varname: self.layer
        }

        #DEPRICATED: also, all of the ones in the other items
        self.icon = "add_circle"


    class __x:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetPosition(pcbnew.wxPoint(value, self.item.obj.GetCenter().y))

        def get(self):
            return self.item.obj.GetPosition().x

    class __y:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetPosition(pcbnew.wxPoint(self.item.obj.GetCenter().x, value))

        def get(self):
            return self.item.obj.GetPosition().y

    class __radius:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            centerX = self.item.obj.GetStartX()
            centerY = self.item.obj.GetStartY()
            self.item.obj.SetEndX(value + centerX)
            self.item.obj.SetEndY(centerY)

        def get(self):
            return self.item.obj.GetRadius()

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
