import pcbnew
from .item import *


def get_selected():
    pcb = pcbnew.GetBoard()

    item_list = []

    for footprint in pcb.GetFootprints():
        if footprint.IsSelected():
            item_list.append(Item(footprint))
            print()
            print("attributes", footprint.GetAttributes())
            print("flag", footprint.GetFlag())
            print("likelyattr", footprint.GetLikelyAttribute())
            for p in footprint.GetPropertiesNative():
                print("propertiesnative", p)
            print("class", footprint.GetClass())
            print(SELECTED)


    return Items(item_list)

