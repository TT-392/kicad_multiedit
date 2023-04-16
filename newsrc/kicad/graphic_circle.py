from .kicad import *
from .board_item import *

class Graphic_circle(Board_item):
    def __init__(self, pcbnew_obj, units = UNIT_MM):
        self.pcbnew_obj = pcbnew_obj
        self.units = units

        self.values = {
            "Position": {
                "X": None,
                "Y": None 
            }, 
            "Graphic": {
                "Radius": None,
                "Line width": None
            },
            "Miscellaneous": {
                "Layer": None
            },
            "Custom Attributes": {}
        }


    def is_selected(self):
        return self.pcbnew_obj.IsSelected()


    def update_stored_values(self):
        pos = self.pcbnew_obj.GetPosition()
        dummy, pos = self._Board_item__transform_rotation_and_position(0, pos)
        radius = kicad_utils.to_unit(self.units, self.pcbnew_obj.GetRadius())


        self.values["Position"]["X"] = pos[0]
        self.values["Position"]["Y"] = pos[1]

        self.values["Graphic"]["Radius"] = radius


    def put_values(self, values):
        pass

