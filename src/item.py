from .property import *
from .unit import *
import wx
import pcbnew

class Item:
    def __init__(self, pcbnew_obj):
        self.obj = pcbnew_obj

        prop_list = []
        if type(pcbnew_obj) == pcbnew.FOOTPRINT:
            prop_list.append(Property("X", "Position", "length", toUnit(pcbnew_obj.GetPosition().x)))
            prop_list.append(Property("Y", "Position", "length", toUnit(pcbnew_obj.GetPosition().y)))
            prop_list.append(Property("Angle", "Orientation", "angle", pcbnew_obj.GetOrientation() / 10))
            prop_list.append(Property("Ref", "Fields", "string", pcbnew_obj.GetReference()))

        self.properties = Properties_array(prop_list)

    def write_properties(self):
        if type(self.obj) == pcbnew.FOOTPRINT:
            x = self.properties.get_with_name("X").list[0]
            y = self.properties.get_with_name("Y").list[0]
            angle = self.properties.get_with_name("Angle").list[0]
            ref = self.properties.get_with_name("Ref").list[0]

            pos = [fromUnit(x.value),fromUnit(y.value)]
            posChanged = False

            if x.eval():
                pos[0] = fromUnit(x.value)
                posChanged = True

            if y.eval():
                pos[1] = fromUnit(y.value)
                posChanged = True

            if posChanged:
                self.obj.SetPosition(pcbnew.wxPoint(pos[0], pos[1]))


            if angle.eval():
                self.obj.SetOrientation(angle.value * 10)

            if ref.eval():
                self.obj.SetReference(ref.value)



class Items:
    def __init__(self, items):
        self.list = items

    def get_properties(self):
        properties = Properties_array([])
        
        for item in self.list:
            properties += item.properties


        return properties
