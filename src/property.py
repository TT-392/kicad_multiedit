from .kicad.kicad import *
from .utils import *
from .config import *

class Property:
    def __init__(self, widget_type, varname):
        self.widget_type = widget_type
        self.varname = varname
        self.ui_element = None


        self.values = []

        self.ui_element = None

        kicad_info.update()

    def get_ui_value(self):
        # TODO: re enable this check
        #assert len(self.values) != 0, "property without members"

        if len(self.values) == 0:
            return "None"
        if len(self.values) == 1:
            return utils.to_parseable_string(self.values[0].get())
        else:
            firstValue = self.values[0].get()

            for value in self.values[1:]:
                if value.get() != firstValue:
                    return self.varname
            
            return utils.to_parseable_string(firstValue)
    
    def prepare_variables(self, ui_val):
        for value in self.values:
            value.item.python_env.prepare_variables(ui_val)


    def put_ui_value(self, ui_val):
        for value in self.values:
            new_value = value.item.python_eval(ui_val)
            
            if new_value != value.get():
                print("applying", new_value, "to", self.varname, "in", value.item)
                value.put(new_value)


    def register(self, value_obj):
        self.values.append(value_obj)

        return self


    def get_icons(self):
        icons = []

        for item in self.get_items():
            icons.append(item.icon)

        return set(icons)


    def get_items(self):
        items = []

        for value in self.values:
            items.append(value.item)
        
        return items


    def update_ui_value(self):
        self.ui_element.set_value(self.get_ui_value())


    def is_visible(self):
        if len(self.values) == 0:
            return False
        else:
            return True

