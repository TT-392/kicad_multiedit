import pcbnew
from .item import *
from .kicad.footprint import *
from .kicad.line import *
from .kicad.arc import *
from .kicad.rect import *
from .kicad.circle import *
from .kicad.polygon import *
from .kicad.text import *

def get_selected():
    LINE = 0
    RECT = 1
    ARC = 2
    CIRCLE = 3
    POLY = 4



    pcb = pcbnew.GetBoard()

    item_list = []

    for footprint in pcb.GetFootprints():
        if footprint.IsSelected():
            item_list.append(Footprint(footprint))

    for drawing in pcb.GetDrawings():
        if drawing.IsSelected():
            if type(drawing) == pcbnew.PCB_TEXT:
                item_list.append(GraphicText(drawing))

            elif drawing.GetShape() == LINE:
                item_list.append(GraphicLine(drawing))

            elif drawing.GetShape() == ARC:
                item_list.append(GraphicArc(drawing))

            elif drawing.GetShape() == RECT:
                item_list.append(GraphicRect(drawing))

            elif drawing.GetShape() == CIRCLE:
                item_list.append(GraphicCircle(drawing))

            elif drawing.GetShape() == POLY:
                item_list.append(GraphicPolygon(drawing))


    return Items(item_list)

