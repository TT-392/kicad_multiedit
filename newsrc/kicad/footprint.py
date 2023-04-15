from .kicad import *
from ..utils import *
from copy import deepcopy
import pprint

class Footprint:
    def __init__(self, pcbnew_obj, units = UNIT_MM):
        self.pcbnew_obj = pcbnew_obj

        self.__values = {
            "Position": {
                "X": None,
                "Y": None 
            }, 
            "Orientation": {
                "Angle": None
            },
            "Text Items": {
                "Ref": None
            },
            "Fabrication Attributes": {
                "Not in schematic": None
            },
            "Custom Attributes": {}
        }

        self.origin = (0, 0), 0
        self.units = units


    def __str__(self):
        retval = {"Values": self.get_values(),
                  "obj": self.pcbnew_obj,
                  "selected": self.is_selected(),
                  "origin": self.origin,
                  "units": self.units
                 }

        return pprint.pformat(retval, indent=4)


    def is_selected(self):
        return self.pcbnew_obj.IsSelected()


    def __get_attributes(self):
        retval = {}

        if self.pcbnew_obj.GetAttributes() & 0b10000:
            retval["Not in schematic"] = True
        else:
            retval["Not in schematic"] = False

        return retval


    def __set_attributes(self, attrib):
        attributes = self.pcbnew_obj.GetAttributes()

        if attrib["Not in schematic"] == True:
            attributes |= 0b10000
        elif attrib["Not in schematic"] == False:
            attributes &= ~0b10000

        self.pcbnew_obj.SetAttributes(attributes)


    def __update_stored_values(self):
        pos = self.pcbnew_obj.GetPosition()
        pos = (kicad_utils.to_unit(self.units, pos.x),
               kicad_utils.to_unit(self.units, pos.y))
        pos = utils.translate(pos, self.__origin_to_user_unit(self.origin))
        attributes = self.__get_attributes()
        rot = self.pcbnew_obj.GetOrientationDegrees() - self.origin[1]
        if rot > 180:
            rot -= 360
        elif rot <= -180:
            rot += 360

        self.__values["Position"]["X"] = pos[0]

        self.__values["Position"]["Y"] = pos[1]

        self.__values["Orientation"]["Angle"] = rot

        self.__values["Text Items"]["Ref"] = \
                self.pcbnew_obj.GetReference()

        self.__values["Fabrication Attributes"]["Not in schematic"] = \
                attributes["Not in schematic"]


    def set_units(self, units):
        self.units = units

    
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


    def set_origin(self, origin):
        self.origin = self.__origin_from_user_unit(origin)


    def get_values(self):
        self.__update_stored_values()
        return deepcopy(self.__values)


    def put_values(self, values):
        # TODO: value translation and unit convertion when putting values
        category = values["Position"], local_category = __values["Position"]
        if category["X"] != local_category["X"] or category["Y"] != local_category["Y"]: 
            self.pcbnew_obj.SetPosition(pcbnew.wxPoint(category["X"], category["Y"]))


        category = values["Orientation"], local_category = __values["Orientation"]
        if category["Angle"] != local_category["Angle"]:
            self.pcbnew_obj.SetOrientationDegrees(category["Rotation"])


        category = values["Text Items"], local_category = __values["Text Items"]
        if category["Ref"] != local_category["Ref"]:
            self.pcbnew_obj.SetReference(category["Ref"])


        category = values["Fabrication Attributes"]
        local_category = __values["Fabrication Attributes"]
        if category["Not in schematic"] != local_category["Not in schematic"]:
            attributes["Not in schematic"] = category["Not in schematic"]


        self.__set_attributes(attributes)

