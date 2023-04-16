import sys
from ..test import *
sys.path.append("../..")
from newsrc.kicad.footprint import *
from newsrc.kicad.kicad import *

import os
import pcbnew
import pprint

class Footprint_test(Test):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.identifier_string = "Footprint"

        self.pcb = pcbnew.LoadBoard(os.path.join(os.path.dirname(__file__), "..", "pcbnew_test_files", "test1.kicad_pcb"))

        self.footprints = {}

        for pcbnew_fp in self.pcb.GetFootprints():
            footprint = Footprint(pcbnew_fp)

            self.footprints[footprint.get_values()["Text Items"]["Ref"]] = footprint



    def test_all(self):
        self.result = {"Pass": 0, "Fail": 0}

        self.footprints["U1"].set_units(UNIT_MM)
        U1 = self.footprints["U1"].get_values()
        self.test(U1["Position"]["X"], 92, "U1 X")
        self.test(U1["Position"]["Y"], 62, "U1 Y")
        self.test(U1["Orientation"]["Angle"], 32, "U1 Angle")
        self.test(U1["Text Items"]["Ref"], "U1", "U1 Ref")
        self.test(U1["Fabrication Attributes"]["Not in schematic"], False, "U1 not in schematic")

        self.footprints["U1"].set_units(UNIT_MM)
        self.footprints["U1"].set_origin(((10, 10), 0))
        U1 = self.footprints["U1"].get_values()
        self.test(U1["Position"]["X"], 82, "U1 X, adjusted origin")
        self.test(U1["Position"]["Y"], 52, "U1 Y, adjusted origin")
        self.test(U1["Orientation"]["Angle"], 32, "U1 Angle, adjusted origin")

        self.footprints["U2"].set_units(UNIT_MM)
        U2 = self.footprints["U2"].get_values()
        self.test(U2["Position"]["X"], 74, "U2 X")
        self.test(U2["Position"]["Y"], 82, "U2 Y")
        self.test(U2["Orientation"]["Angle"], 90, "U2 Angle")
        self.test(U2["Text Items"]["Ref"], "U2", "U2 Ref")
        self.test(U2["Fabrication Attributes"]["Not in schematic"], False, "U2 not in schematic")

        self.footprints["U3"].set_units(UNIT_MM)
        U3 = self.footprints["U3"].get_values()
        self.test(U3["Position"]["X"], 112, "U3 X")
        self.test(U3["Position"]["Y"], 89, "U3 Y")
        self.test(U3["Orientation"]["Angle"], 0, "U3 Angle")
        self.test(U3["Text Items"]["Ref"], "U3", "U3 Ref")
        self.test(U3["Fabrication Attributes"]["Not in schematic"], True, "U3 not in schematic")

        self.footprints["U4"].set_units(UNIT_MM)
        U4 = self.footprints["U4"].get_values()
        self.test(U4["Position"]["X"], 130, "U4 X")
        self.test(U4["Position"]["Y"], 69, "U4 Y")
        self.test(U4["Orientation"]["Angle"], -12, "U4 Angle")
        self.test(U4["Text Items"]["Ref"], "U4", "U4 Ref")
        self.test(U4["Fabrication Attributes"]["Not in schematic"], False, "U4 not in schematic")

        self.footprints["U5"].set_units(UNIT_MIL)
        U5 = self.footprints["U5"].get_values()
        self.test(U5["Position"]["X"], 7000, "U5 X")
        self.test(U5["Position"]["Y"], 2000, "U5 Y")
        self.test(U5["Orientation"]["Angle"], 32, "U5 Angle")
        self.test(U5["Text Items"]["Ref"], "U5", "U5 Ref")
        self.test(U5["Fabrication Attributes"]["Not in schematic"], False, "U5 not in schematic")

        self.footprints["U5"].set_units(UNIT_IN)
        U5 = self.footprints["U5"].get_values()
        self.test(U5["Position"]["X"], 7, "U5 X, inch")
        self.test(U5["Position"]["Y"], 2, "U5 Y, inch")

        self.footprints["U6"].set_units(UNIT_MIL)
        U6 = self.footprints["U6"].get_values()
        self.test(U6["Position"]["X"], 8294, "U6 X")
        self.test(U6["Position"]["Y"], 2923, "U6 Y")
        self.test(U6["Orientation"]["Angle"], -12, "U6 Angle")
        self.test(U6["Text Items"]["Ref"], "U6", "U6 Ref")
        self.test(U6["Fabrication Attributes"]["Not in schematic"], True, "U6 not in schematic")

        self.footprints["U6"].set_units(UNIT_IN)
        U6 = self.footprints["U6"].get_values()
        self.test(U6["Position"]["X"], 8.294, "U6 X, inch")
        self.test(U6["Position"]["Y"], 2.923, "U6 Y, inch")

        self.footprints["U7"].set_units(UNIT_MIL)
        U7 = self.footprints["U7"].get_values()
        self.test(U7["Position"]["X"], 9000, "U7 X")
        self.test(U7["Position"]["Y"], 5000, "U7 Y")
        self.test(U7["Orientation"]["Angle"], 90, "U7 Angle")
        self.test(U7["Text Items"]["Ref"], "U7", "U7 Ref")
        self.test(U7["Fabrication Attributes"]["Not in schematic"], False, "U7 not in schematic")

        self.footprints["U7"].set_units(UNIT_IN)
        U7 = self.footprints["U7"].get_values()
        self.test(U7["Position"]["X"], 9, "U7 X, inch")
        self.test(U7["Position"]["Y"], 5, "U7 Y, inch")

        self.footprints["U8"].set_units(UNIT_MIL)
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], 7000, "U8 X")
        self.test(U8["Position"]["Y"], 5000, "U8 Y")
        self.test(U8["Orientation"]["Angle"], 0, "U8 Angle")
        self.test(U8["Text Items"]["Ref"], "U8", "U8 Ref")
        self.test(U8["Fabrication Attributes"]["Not in schematic"], False, "U8 not in schematic")

        self.footprints["U8"].set_units(UNIT_IN)
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], 7, "U8 X, inch")
        self.test(U8["Position"]["Y"], 5, "U8 Y, inch")


        self.footprints["U8"].set_units(UNIT_MIL)
        self.footprints["U8"].set_origin(((5000, 5000), 0))
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], 2000, "U8 X, adjusted origin")
        self.test(U8["Position"]["Y"], 0, "U8 Y, adjusted origin")
        self.test(U8["Orientation"]["Angle"], 0, "U8 Angle, adjusted origin")

        self.footprints["U8"].set_units(UNIT_IN)
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], 2, "U8 X, inch, adjusted origin")
        self.test(U8["Position"]["Y"], 0, "U8 Y, inch, adjusted origin")


        self.footprints["U8"].set_units(UNIT_IN)
        self.footprints["U8"].set_origin(((5, 5), 0))
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], 2, "U8 X, adjusted origin, 0°")
        self.test(U8["Position"]["Y"], 0, "U8 Y, adjusted origin, 0°")
        self.test(U8["Orientation"]["Angle"], 0, "U8 Angle, adjusted origin, 0°")

        self.footprints["U8"].set_units(UNIT_IN)
        self.footprints["U8"].set_origin(((5, 5), 90))
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], 0, "U8 X, adjusted origin, 90°")
        self.test(U8["Position"]["Y"], 2, "U8 Y, adjusted origin, 90°")
        self.test(U8["Orientation"]["Angle"], -90, "U8 Angle, adjusted origin, 90°")

        self.footprints["U8"].set_units(UNIT_IN)
        self.footprints["U8"].set_origin(((5, 5), 180))
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], -2, "U8 X, adjusted origin, 180°")
        self.test(U8["Position"]["Y"], 0, "U8 Y, adjusted origin, 180°")
        self.test(U8["Orientation"]["Angle"], 180, "U8 Angle, adjusted origin, 180°")

        self.footprints["U8"].set_units(UNIT_IN)
        self.footprints["U8"].set_origin(((5, 5), -90))
        U8 = self.footprints["U8"].get_values()
        self.test(U8["Position"]["X"], 0, "U8 X, adjusted origin, -90°")
        self.test(U8["Position"]["Y"], -2, "U8 Y, adjusted origin, -90°")
        self.test(U8["Orientation"]["Angle"], 90, "U8 Angle, adjusted origin, -90°")
        # TODO tests for non multiples of 90°
        # TODO: put_values tests

        return self.result


print("Footprint test:", Footprint_test(False).test_all())

