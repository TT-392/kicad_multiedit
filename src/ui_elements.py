from .item import *
from .kicad.kicad import *


class Ui_element:
    def __init__(self, name, category, widget_type, field_value, properties, items):
        self.name = name
        self.category = category
        self.widget_type = widget_type
        self.field_value = field_value
        self.properties = properties
        self.items = items

    def __str__(self):
        retval = self.name + ": " + str(self.field_value)
        retval += " " + str(self.widget_type)

        #for item in self.items.list:
        #    retval += str(type(item))
        #    retval += " "

        return retval

    def update(self):
        if self.properties.all_same_value():
            self.field_value = str(self.properties.get_ui_value())
            self.wx_field.SetValue(self.field_value)

    def put(self, value):
        print(self, "updated")
        self.properties.put_ui_value(value)




class Ui_elements:
    def __init__(self, properties):
        names = properties.get_all("name")
        categories = properties.get_all("category")

        self.list = []
        for category in categories:
            self.list.append(category)

            for name in names:
                props = properties.get_in_category_and_with_name(category, name)

                if len(props) != 0:
                    if props.all_same_value():
                        field_value = props.get_ui_value()
                    else:
                        varname = props.get("varname")
                        field_value = varname

                    items = Items(props.get_items())
                    widget_type = props.get("widget_type")
                    self.list.append(Ui_element(name, category, widget_type, field_value, props, items))



    def __str__(self):
        retval = "Ui_elements {"

        for ui_prop in self.list:
            retval += "\n"
            retval += str(ui_prop)
            retval += ","

        retval = retval[:-1]

        retval += "}"

        return retval

