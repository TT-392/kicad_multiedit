import pcbnew
from kicad import *
from ..property import *
from ..item import *
from ..gui.elements import *
from ..ui_layout import *

class GraphicLine(Item):
    def __init__(self, obj):
        self.obj = obj
        self.startX = self.translated_x(self, self.__startX, self.__startY)
        self.startY = self.translated_y(self, self.__startY, self.__startX)
        self.endX = self.translated_x(self, self.__endX, self.__endY)
        self.endY = self.translated_y(self, self.__endY, self.__endX)
        self.width = self.to_user_unit(self, self.__width)
        self.layer = self.__layer(self)

        self.values = {
            ui_layout["Graphic"]["Start X"].register(self.startX).varname: self.startX,
            ui_layout["Graphic"]["Start Y"].register(self.startY).varname: self.startY,
            ui_layout["Graphic"]["End X"].register(self.endX).varname: self.endX,
            ui_layout["Graphic"]["End Y"].register(self.endY).varname: self.endY,
            ui_layout["Graphic"]["Line width"].register(self.width).varname: self.width,
            ui_layout["Miscellaneous"]["Layer"].register(self.layer).varname: self.layer
        }

        self.icon = "add_line"



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
