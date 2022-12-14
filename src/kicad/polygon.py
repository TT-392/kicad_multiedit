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

class GraphicPolygon(Item):
    def __init__(self, obj):
        self.obj = obj
        self.width = self.to_user_unit(self, self.__width)
        self.layer = self.__layer(self)

        self.values = {
            ui_layout["Graphic"]["Line width"].register(self.width).varname: self.width,
            ui_layout["Miscellaneous"]["Layer"].register(self.layer).varname: self.layer
        }

        self.icon = "add_graphical_polygon"

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
