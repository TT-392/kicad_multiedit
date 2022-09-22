from .property import *
from .unit import *

class Items:
    def __init__(self, items):
        self.__list = items

    def get_properties(self):
        properties = Properties_array([])
        
        for item in self.__list:
            properties += item.properties


        return properties
    
    def get_icons(self):
        retval = []
        for item in self.__list:
            if not item.icon in retval:
                retval.append(item.icon)
        
        return retval

