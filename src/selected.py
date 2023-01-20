import pcbnew
from .item import *
from .ui_layout import *
from .kicad.kicad import *
from .kicad.footprint import *
from .kicad.footprint_text import *
from .kicad.line import *
from .kicad.arc import *
from .kicad.rect import *
from .kicad.circle import *
from .kicad.polygon import *
from .kicad.text import *


class Selected:
    def __init__(self):
        self.items = Items([])

    def update(self, test_mode = False):
        LINE = 0
        RECT = 1
        ARC = 2
        CIRCLE = 3
        POLY = 4

        # Reset UI
        for category in ui_layout:
            for name in ui_layout[category]:
                prop = ui_layout[category][name]
                prop.values = {"active": [], "inactive": []}


        pcb = kicad_info.get_board()

        item_list = []

        for footprint in pcb.GetFootprints():
            if footprint.IsSelected() or test_mode:
                item_list.append(Footprint(footprint))

            else:
                for item in footprint.GraphicalItems():
                    if type(item) == pcbnew.FP_TEXT:
                        if item.IsSelected() or test_mode:
                            item_list.append(FootprintText(item))

                reference = footprint.Reference()
                if reference.IsSelected() or test_mode:
                    item_list.append(FootprintText(reference))

                value_text_item = footprint.Value()
                if value_text_item.IsSelected() or test_mode:
                    item_list.append(FootprintText(value_text_item))


        for drawing in pcb.GetDrawings():
            if drawing.IsSelected() or test_mode:
                if type(drawing) == pcbnew.PCB_TEXT:
                    item_list.append(GraphicText(drawing))

                if type(drawing) == pcbnew.PCB_SHAPE:
                    if drawing.GetShape() == LINE:
                        item_list.append(GraphicLine(drawing))

                    elif drawing.GetShape() == ARC:
                        item_list.append(GraphicArc(drawing))

                    elif drawing.GetShape() == RECT:
                        item_list.append(GraphicRect(drawing))

                    elif drawing.GetShape() == CIRCLE:
                        item_list.append(GraphicCircle(drawing))

                    elif drawing.GetShape() == POLY:
                        item_list.append(GraphicPolygon(drawing))


        self.items = Items(item_list)



currently_selected = Selected()
