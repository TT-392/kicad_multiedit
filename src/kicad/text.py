from ..property import *
from ..item import *
from ..gui.elements import *
from ..ui_layout import *

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

        self.values = {
            ui_layout["Text"]["Text"].register(self.text).varname: self.text,
            ui_layout["Position"]["X"].register(self.x).varname: self.x,
            ui_layout["Position"]["Y"].register(self.y).varname: self.y,
            ui_layout["Text"]["Width"].register(self.textWidth).varname: self.textWidth,
            ui_layout["Text"]["Height"].register(self.textHeight).varname: self.textHeight,
            ui_layout["Graphic"]["Line width"].register(self.width).varname: self.width,
            ui_layout["Orientation"]["Angle"].register(self.orientation).varname: self.orientation,
            ui_layout["Miscellaneous"]["Layer"].register(self.layer).varname: self.layer
        }

        self.icon = "text"


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
            self.item.obj.SetTextAngleDegrees(value)

        def get(self):
            return self.item.obj.GetTextAngleDegrees()

    class __layer:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetLayer(kicad_info.get_layer_id(value))

        def get(self):
            return pcbnew.LayerName(self.item.obj.GetLayer())
