from .kicad.kicad import *
from .utils import *
from .config import *

class Property:
    def __init__(self, widget_type, varname):
        self.widget_type = widget_type
        self.varname = varname
        self.ui_element = None


        self.values = {"active": [], "inactive": []}

        self.ui_element = None

        kicad_info.update()

    def get_ui_value(self):
        # TODO: re enable this check
        #assert len(self.values) != 0, "property without members"

        if len(self.values["active"]) == 0:
            return "None"
        if len(self.values["active"]) == 1:
            return utils.to_parseable_string(self.values["active"][0].get())
        else:
            firstValue = self.values["active"][0].get()

            for value in self.values["active"][1:]:
                if value.get() != firstValue:
                    return self.varname
            
            return utils.to_parseable_string(firstValue)
    
    def prepare_variables(self, ui_val):
        for value in self.values["active"]:
            value.item.python_env.prepare_variables(ui_val)


    def put_ui_value(self, ui_val):
        for value in self.values["active"]:
            new_value = value.item.python_eval(ui_val)
            
            if new_value != value.get():
                print("applying", new_value, "to", self.varname, "in", value.item)
                value.put(new_value)


    def register(self, value_obj):
        self.values["active"].append(value_obj)

        return self


    def get_item_types(self):
        item_types = []

        for item in self.get_items():
            item_types.append(type(item))

        return set(item_types)


    def get_items(self):
        items = []

        for value in self.values["active"]:
            items.append(value.item)
        
        return items


    def update_ui_value(self):
        self.ui_element.set_value(self.get_ui_value())

    def set_selected_types(self, item_types):
        active_values = []
        inactive_values = []

        for value in self.values["active"] + self.values["inactive"]:
            if type(value.item) in item_types:
                active_values.append(value)
            else:
                inactive_values.append(value)

        self.values["active"] = active_values
        self.values["inactive"] = inactive_values

    def is_active(self):
        if len(self.values["active"]) == 0:
            return False
        else:
            return True

