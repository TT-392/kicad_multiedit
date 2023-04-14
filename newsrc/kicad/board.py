from copy import deepcopy

class Footprint:
    def __init__(self, pcbnew_obj):
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
        }

        self.selected = pcbnew_obj.IsSelected()


    def __get_attributes():
        retval = {}

        if self.pcbnew_obj.GetAttributes() & 0b10000:
            retval["Not in schematic"] = True
        else:
            retval["Not in schematic"] = False

        return retval


    def __set_attributes(attrib):
        attributes = self.pcbnew_obj.GetAttributes()

        if attrib["Not in schematic"] == True:
            attributes |= 0b10000
        elif attrib["Not in schematic"] == False:
            attributes &= ~0b10000

        self.pcbnew_obj.SetAttributes(attributes)


    def __update_stored_values(self):
        pos = self.pcbnew_obj.GetPosition()
        attributes = self.__get_attributes()

        self.__values["Position"]["X"] = pos.x

        self.__values["Position"]["Y"] = pos.y

        self.__values["Orientation"]["Angle"] = \
                self.pcbnew_obj.GetOrientationDegrees()

        self.__values["Text Items"]["Ref"] = \
                self.pcbnew_obj.GetReference()

        self.__values["Fabrication Attributes"]["Not in schematic"] = \
                attributes["not in schematic"]


    def set_units(self, units):
        self.units = units


    def set_origin(self, origin):
        self.origin = origin


    def get_values(self):
        self.__update_stored_values()
        return deepcopy(self.__values)


    def put_values(self, values):
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

