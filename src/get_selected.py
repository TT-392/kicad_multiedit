import pcbnew
from .item import *
from .kicad.footprint import *


def get_selected():
    pcb = pcbnew.GetBoard()

    item_list = []

    for footprint in pcb.GetFootprints():
        if footprint.IsSelected():
            item_list.append(Footprint(footprint))


    return Items(item_list)

