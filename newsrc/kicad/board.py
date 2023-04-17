import pcbnew
import os
from .footprint import *
from .graphic_circle import *
import pprint
import time

class Board:
    def __init__(self):
        self.pcb = pcbnew.LoadBoard(os.path.join(os.path.dirname(__file__), "..", "..", "newtests", "pcbnew_test_files", "test1.kicad_pcb"))

        self.__board_items = {}

        self.update()


    def __str__(self):
        return pprint.pformat(self.__board_items, indent=4)
    

    def __create_item(self, pcbnew_object):
        LINE = 0
        RECT = 1
        ARC = 2
        CIRCLE = 3
        POLY = 4

        if type(pcbnew_object) == pcbnew.FOOTPRINT:
            return Footprint(pcbnew_object)
        elif type(pcbnew_object) == pcbnew.PCB_SHAPE:
            shape = pcbnew_object.GetShape()

            if pcbnew_object.GetShape() == CIRCLE:
                return Graphic_circle(pcbnew_object)
            else:
                print("Warning: Shape:", shape, "not yet implemented")
                return None
        elif type(pcbnew_object) == pcbnew.PCB_TEXT:
            print("Warning: PCB_TEXT not yet implemented")
            return None
        else:
            print("Warning:", type(pcbnew_object), "not yet implemented")
            return None


    def update(self):
        print("UPDATING BOARD")
        new_pcbnew_objects = set([])
        
        new_pcbnew_objects = set(
            self.pcb.GetFootprints() + \
            self.pcb.GetDrawings()
        #    [item.GraphicalItems() for item in self.pcb.GetFootprints()]
        )

        new_pcbnew_objects = {obj.m_Uuid.Hash() : obj for obj in new_pcbnew_objects}


        for item_hash in self.__board_items:
            if not item_hash in new_pcbnew_objects:
                self.__board_items.pop(item_hash)

        for item_hash in new_pcbnew_objects:
            if not item_hash in self.__board_items:
                item = self.__create_item(new_pcbnew_objects[item_hash])

                if not item == None:
                    self.__board_items[item_hash] = item
            else:
                self.__board_items[item_hash].update_object(new_pcbnew_objects[item_hash])

        return


    def get_selected(self):
        self.update()
        selected = set([])

        for item_hash in self.__board_items:
            item = self.__board_items[item_hash]

            if item.is_selected():
                selected.add(item)

        return selected

