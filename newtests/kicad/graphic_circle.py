import sys
from ..test import *
sys.path.append("../..")
from newsrc.kicad.graphic_circle import *
import os
import pcbnew

class Graphic_circle_test(Test):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.identifier_string = "Graphic circle"

        self.pcb = pcbnew.LoadBoard(os.path.join(os.path.dirname(__file__), "..", "pcbnew_test_files", "test1.kicad_pcb"))

        self.circles = {}

        CIRCLE = 3

        for drawing in self.pcb.GetDrawings():
            if drawing.GetShape() == CIRCLE:
                circle = Graphic_circle(drawing)

                # Can't think of a better identifier for a circle object
                self.circles[circle.get_values()["Graphic"]["Radius"]] = circle


    def test_all(self):
        self.result = {"Pass": 0, "Fail": 0}

        self.circles[1].set_units(UNIT_MM)
        circle = self.circles[1].get_values()
        self.test(circle["Position"]["X"], 30, "Circle 1 X")
        self.test(circle["Position"]["Y"], 40, "Circle 1 Y")
        self.test(circle["Graphic"]["Radius"], 1, "Circle 1 Radius")
        self.test(circle["Graphic"]["Line width"], 0.2, "Circle 1 Line width")
        self.test(circle["Miscellaneous"]["Layer"], "F.Cu", "Circle 1 Layer")

        self.circles[2].set_units(UNIT_MM)
        circle = self.circles[2].get_values()
        self.test(circle["Position"]["X"], 54, "Circle 2 X")
        self.test(circle["Position"]["Y"], 55, "Circle 2 Y")
        self.test(circle["Graphic"]["Radius"], 2, "Circle 2 Radius")
        self.test(circle["Graphic"]["Line width"], 1, "Circle 2 Line width")
        self.test(circle["Miscellaneous"]["Layer"], "User.Drawings", "Circle 2 Layer")

        self.circles[3].set_units(UNIT_MIL)
        circle = self.circles[3].get_values()
        self.test(circle["Position"]["X"], 2536, "Circle 3 X")
        self.test(circle["Position"]["Y"], 1109, "Circle 3 Y")
        self.test(circle["Graphic"]["Radius"], 118.1102362, "Circle 3 Radius", 0.0000001)
        self.test(circle["Graphic"]["Line width"], 118.2, "Circle 3 Line width")
        self.test(circle["Miscellaneous"]["Layer"], "B.Adhesive", "Circle 3 Layer")

        # TODO tests for different origins
        # TODO: put_values tests

        return self.result


print("Graphic Circle test:", Graphic_circle_test(False).test_all())

