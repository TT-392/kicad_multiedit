from .item import *
from .kicad.kicad import *


class Ui_property:
    def __init__(self, name, category, widget_type, ui_value, properties, items, unit=None):
        self.name = name
        self.category = category
        self.widget_type = widget_type
        self.ui_value = ui_value
        self.properties = properties
        self.unit = unit
        self.items = items

    def __str__(self):
        retval = self.name + ": " + str(self.ui_value)
        retval += " " + self.widget_type

        if self.unit != None:
            retval += " " + self.unit

        #for item in self.items.list:
        #    retval += str(type(item))
        #    retval += " "

        return retval



class Ui_elements:
    def __init__(self, properties):
        #TODO: I don't think it'd hurt combining these 2 for cleaner code
        names = properties.get_names()
        categories = properties.get_categories()

        self.list = []
        for category in categories:
            self.list.append(category)

            for name in names:
                props = properties.get_in_category_and_with_name(category, name)

                if len(props.list) != 0:
                    widget_type = self.__widget_type_from_data_type(props.list[0].data_type)
                    if props.all_same_value():
                        ui_value = str(props.list[0].get_ui_value())
                    else:
                        ui_value = "x"

                    items = Items(props.get_items())
                    unit = self.__unit_from_data_type(props.list[0].data_type)
                    self.list.append(Ui_property(name, category, widget_type, ui_value, props, items, unit))

    def __widget_type_from_data_type(self, data_type):
        if data_type == "string" or data_type == "length" or data_type == "length_unsigned" or data_type == "angle":
            return "textbox"

        elif data_type == "bool":
            return "checkbox"

        else:
            print("error, datatype not implemented yet")

    def __unit_from_data_type(self, data_type):
        if data_type == "length" or data_type == "length_unsigned":
            kicad_info.update()
            return kicad_info.unit_string
        elif data_type == "angle":
            return "deg"
        else:
            return None


    def __str__(self):
        retval = "Ui_properties {"

        for ui_prop in self.list:
            retval += "\n"
            retval += str(ui_prop)
            retval += ","

        retval = retval[:-1]

        retval += "}"

        return retval

