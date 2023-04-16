import pcbnew
import os
from .footprint import *
import pprint

class Board:
    def __init__(self):
        self.pcb = pcbnew.LoadBoard(os.path.join(os.path.dirname(__file__), "..", "..", "newtests", "pcbnew_test_files", "test1.kicad_pcb"))

        self.items = set([])
        self.__pcbnew_objects = set([])

        self.update()


    def __str__(self):
        return pprint.pformat(self.items, indent=4)
    

    def __create_item(self, pcbnew_object):
        if type(pcbnew_object) == pcbnew.FOOTPRINT:
            return Footprint(pcbnew_object)


    def update(self):
        new_pcbnew_objects = set([])
        
        for pcbnew_fp in self.pcb.GetFootprints():
            new_pcbnew_objects.add(pcbnew_fp)

        new = new_pcbnew_objects - self.__pcbnew_objects
        marked_for_deletion = self.__pcbnew_objects - new_pcbnew_objects

        for pcbnew_object in new:
            self.__pcbnew_objects.add(pcbnew_object)
            self.items.add(self.__create_item(pcbnew_object))

        for pcbnew_object in marked_for_deletion:
            self.__pcbnew_objects.remove(pcbnew_object)

            for item in self.items:
                if item.pcbnew_obj == pcbnew_object:
                    self.items.remove(item)
                    break


    def get_selected(self):
        self.update()
        selected = set([])

        for item in self.items:
            if item.is_selected():
                selected.add(item)

        return selected

