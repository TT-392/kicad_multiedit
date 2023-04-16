from .kicad import *
from ..utils import *
from copy import deepcopy
import pprint

class Board_item:
    origin = (0, 0), 0


    def __str__(self):
        retval = {"Type": type(self),
                  "Values": self.get_values(),
                  "obj": self.pcbnew_obj,
                  "selected": self.is_selected(),
                  "origin": self.origin,
                  "units": self.units
                 }

        return pprint.pformat(retval, indent=4)


    def set_units(self, units):
        self.units = units


    def set_origin(self, origin):
        self.origin = self.__origin_from_user_unit(origin)


    def __transform_rotation_and_position(self, rot, pos):
        pos = (kicad_utils.to_unit(self.units, pos.x),
               kicad_utils.to_unit(self.units, pos.y))

        rot = rot - self.origin[1]

        if rot > 180:
            rot -= 360
        elif rot <= -180:
            rot += 360

        pos = utils.translate(pos, self._Board_item__origin_to_user_unit(self.origin))

        return rot, pos

        
    def __origin_to_user_unit(self, origin):
        return ((
            kicad_utils.to_unit(self.units, origin[0][0]),
            kicad_utils.to_unit(self.units, origin[0][1])),
            origin[1]
        )


    def __origin_from_user_unit(self, origin):
        return ((
            kicad_utils.from_unit(self.units, origin[0][0]),
            kicad_utils.from_unit(self.units, origin[0][1])),
            origin[1]
        )


    def get_values(self):
        self.update_stored_values()
        return deepcopy(self.values)
