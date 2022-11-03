from ..property import *
from ..item import *
from ..gui.elements import *

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

        self.icon = "add_graphical_polygon"

        self.width_prop = Property("width", "Line", Type_python(), self.width, self, "width")
        self.layer_prop = Property("Layer", "Miscellaneous", Type_dropdown(kicad_info.get_layers()), self.layer, self, "Layer")

        self.properties = Properties([
            self.width_prop,
            self.layer_prop
            ])

    def __str__(self):
        return "Footprint: " + self.reference.get()

    class __width:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetWidth(value)

        def get(self):
            return self.s.obj.GetWidth()

    class __layer:
        def __init__(self, Self):
            self.s = Self
            
        def put(self, value):
            self.s.obj.SetLayer(kicad_info.get_layer_id(value))

        def get(self):
            return pcbnew.LayerName(self.s.obj.GetLayer())
