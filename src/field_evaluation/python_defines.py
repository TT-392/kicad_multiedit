from src.item import *
from src.property import *

class Python_env:
    def __init__(self, items):
        props = items.get_properties()
        self.varnames = props.get_varnames()

        self.defines_string = ""

        for varname in self.varnames:
            self.defines_string += varname + "=0\n"

    def eval(self, item, string):
        props = item.properties
        varnames = props.get_varnames()
        defines_string = self.defines_string

        for prop in props.get_list():
            if prop.varname != None:
                defines_string += prop.varname + "=" + str(prop.get_ui_value()) + "\n"

        return eval_in_clean_environment(defines_string, string)
        

def eval_in_clean_environment(defines_string, string):
    exec(defines_string)

    return eval(string)

