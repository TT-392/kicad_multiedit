import re
from ..item import *
from ..property import *
from .python_container import *

class Python_env:
    def __init__(self, items, item, i):
        props = items.get_properties()
        self.item = item

        self.varnames = props.get_varnames()

        self.defines_string = ""

        for varname in self.varnames:
            self.defines_string += varname + "=0\n"

        self.defines_string += "i=" + str(i) + "\n"

        self.update()

    def update(self):
        props = self.item.properties
        varnames = props.get_varnames()
        self.populated_defines_string = self.defines_string

        for prop in props.get_list():
            if prop.varname != None:
                if prop.varname == "ref":
                    number = re.findall("[\d]*$", prop.get_ui_value())[0]
                    self.populated_defines_string += prop.varname + "=" + number + "\n"
                else:
                    self.populated_defines_string += prop.varname + "=" + str(prop.get_ui_value()) + "\n"

    def eval(self, string):
        return eval_in_container(self.populated_defines_string, string)
        


