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

class FootprintText(Item):
    def __init__(self, obj):
        self.obj = obj
        self.text = self.__text(self)
        self.x = self.translated_x(self, self.__x, self.__y)
        self.y = self.translated_y(self, self.__y, self.__x)
        self.textWidth = self.to_user_unit(self, self.__textWidth)
        self.textHeight = self.to_user_unit(self, self.__textHeight)
        self.width = self.to_user_unit(self, self.__width)
        self.orientation = self.translated_orientation(self, self.__orientation)
        self.visible = self.__visible(self)
        self.layer = self.__layer(self)

        ui_layout["Text"]["Text"].register(self.text)
        ui_layout["Position"]["X"].register(self.x)
        ui_layout["Position"]["Y"].register(self.y)
        ui_layout["Text"]["Width"].register(self.textWidth)
        ui_layout["Text"]["Height"].register(self.textHeight)
        ui_layout["Graphic"]["Line width"].register(self.width)
        ui_layout["Orientation"]["Angle"].register(self.orientation)
        ui_layout["Miscellaneous"]["Visible"].register(self.orientation)
        ui_layout["Miscellaneous"]["Layer"].register(self.layer)

        self.icon = "footprint_text"

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

    class __visible:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetVisible(value)

        def get(self):
            return self.item.obj.IsVisible()

    class __layer:
        def __init__(self, item):
            self.item = item
            
        def put(self, value):
            self.item.obj.SetLayer(kicad_info.get_layer_id(value))

        def get(self):
            return pcbnew.LayerName(self.item.obj.GetLayer())
