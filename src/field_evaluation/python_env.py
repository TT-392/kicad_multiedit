import re
from ..item import *
from ..property import *
from .python_container import *
from ..ui_layout import *
from ..utils import *

class Python_env:
    varnames = set([])
    for category in ui_layout:
        for prop in ui_layout[category]:
            varnames.add(ui_layout[category][prop].varname)
    
    def __init__(self, items, item, i):
        self.item = item
        self.i = i

        self.reset()



    def reset(self):
        self.defines_string = "i = " + str(self.i) + "\n"

    def prepare_variables(self, string):
        present_varnames = set([])

        for varname in self.varnames:
            if len(re.findall(r"\b" + varname + r"\b", string)) != 0:
                present_varnames.add(varname)
        

        for varname in present_varnames:
            if varname in self.item.values:
                value_string = utils.to_parseable_string(self.item.values[varname].get())
            else:
                #TODO: default value should be datatype specific
                value_string = "0"

            self.defines_string += varname + "=" + value_string + "\n"




    def eval(self, string):
        return eval_in_container(self.defines_string, string)
        


