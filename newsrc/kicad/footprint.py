from .kicad import *
from .board_item import *

class Footprint(Board_item):
    def __init__(self, pcbnew_obj, units = UNIT_MM):
        self.pcbnew_obj = pcbnew_obj
        self.units = units

        self.values = {
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


    def update_stored_values(self):
        pos = self.pcbnew_obj.GetPosition()
        rot = self.pcbnew_obj.GetOrientationDegrees()
        rot, pos = self._Board_item__transform_rotation_and_position(rot, pos)
        attributes = self.__get_attributes()

        self.values["Position"]["X"] = pos[0]

        self.values["Position"]["Y"] = pos[1]

        self.values["Orientation"]["Angle"] = rot

        self.values["Text Items"]["Ref"] = \
                self.pcbnew_obj.GetReference()

        self.values["Fabrication Attributes"]["Not in schematic"] = \
                attributes["Not in schematic"]



    def put_values(self, values):
        # TODO: value translation and unit convertion when putting values
        category = values["Position"], local_category = values["Position"]
        if category["X"] != local_category["X"] or category["Y"] != local_category["Y"]: 
            self.pcbnew_obj.SetPosition(pcbnew.wxPoint(category["X"], category["Y"]))


        category = values["Orientation"], local_category = values["Orientation"]
        if category["Angle"] != local_category["Angle"]:
            self.pcbnew_obj.SetOrientationDegrees(category["Rotation"])


        category = values["Text Items"], local_category = values["Text Items"]
        if category["Ref"] != local_category["Ref"]:
            self.pcbnew_obj.SetReference(category["Ref"])


        category = values["Fabrication Attributes"]
        local_category = values["Fabrication Attributes"]
        if category["Not in schematic"] != local_category["Not in schematic"]:
            attributes["Not in schematic"] = category["Not in schematic"]


        self.__set_attributes(attributes)

