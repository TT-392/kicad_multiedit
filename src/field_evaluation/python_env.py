import re
from ..item import *
from ..property import *
from .python_container import *

class Python_env:
    def __init__(self, items, item, i):
        pass
        #props = items.get_properties()
        #self.item = item

        #self.varnames = props.get_all("varname")

        #self.defines_string = ""

        #for varname in self.varnames:
        #    if varname != None:
        #        self.defines_string += varname + "=0\n"

        #self.defines_string += "i=" + str(i) + "\n"

        #self.update()

    def update(self):
        pass
        #props = self.item.properties
        #varnames = props.get_all("varname")
        #
        #self.populated_defines_string = self.defines_string

        #for prop in props:
        #    if prop.varname != None:
        #        self.populated_defines_string += prop.varname + "=" + str(prop.get_ui_value()) + "\n"

    def eval(self, string):
        pass
        #return eval_in_container(self.populated_defines_string, string)
        


