import pcbnew

UNIT_MM = 1
UNIT_MIL = 5
UNIT_IN = 0

class Kicad_info:
    def __init__(self):
        pass

    def update(self):
        self.units = pcbnew.GetUserUnits()

        if self.units == UNIT_MM:
            self.unit_string = "mm"
        elif self.units == UNIT_MIL:
            self.unit_string = "mils"
        elif self.units == UNIT_IN:
            self.unit_string = "in"

    def toUnit(self, value):
        if self.units == UNIT_MM:
            return pcbnew.ToMM(value)
        elif self.units == UNIT_MIL:
            return pcbnew.ToMils(value)
        elif self.units == UNIT_IN:
            return pcbnew.ToMils(value) / 1000

    def fromUnit(self, value):
        if self.units == UNIT_MM:
            return pcbnew.FromMM(value)
        elif self.units == UNIT_MIL:
            return pcbnew.FromMils(value)
        elif self.units == UNIT_IN:
            return pcbnew.FromMils(value * 1000)

kicad_info = Kicad_info()

