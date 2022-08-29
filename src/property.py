from .kicad.kicad import *

# types: 'bool', 'string', 'length', 'lenght_unsigned', 'angle'
# Anything expressed in meters, inches, feet, lightyears is considered to be
# expressed in a unit of length, even if a coordinate or thickness isn't
# neccesarely considered "length'

class Property:
    def __init__(self, name, category, data_type, value, item):
        self.name = name
        self.category = category
        self.data_type = data_type

        self.value = value

        self.ui_element = None

        kicad_info.update()

    def __str__(self):
        return "Property{" + self.name + ", " + self.category + ", " + self.data_type + ", " + str(self.get_ui_value()) + "}"

    def get_ui_value(self):
        if self.data_type == "length" or self.data_type == "length_unsigned":
            ui_val = kicad_info.toUnit(self.value.get())
        elif self.data_type == "angle":
            ui_val = self.value.get() / 10
        else:
            ui_val = self.value.get()
        
        self.__ui_val = ui_val
        return ui_val

    def put_ui_value(self, ui_val):
        if self.get_ui_value() == ui_val:
            return

        print("updating value", self.name)

        if self.data_type == "length" or self.data_type == "length_unsigned":
            self.value.put(kicad_info.fromUnit(ui_val))
        elif self.data_type == "angle":
            self.value.put(ui_val * 10)
        else:
            self.value.put(ui_val)
        


class Properties_array:
    def __init__(self, properties):
        self.list = properties

    def __str__(self):
        retval = "Properties {"

        for prop in self.list:
            retval += "\n"
            retval += str(prop)
            retval += ","

        retval = retval[:-1]

        retval += "}"

        return retval
    
    def __add__(self, other):
        return Properties_array(self.list + other.list)

    def contains_category(self, category):
        for prop in self.list:
            if prop.category == category:
                return True
        return False

    def contains_name(self, name):
        for prop in self.list:
            if prop.name == name:
                return True
        return False

    def get_in_category(self, category):
        properties = []

        for prop in self.list:
            if prop.category == category:
                properties.append(prop)

        return Properties_array(properties)

    def get_with_name(self, name):
        properties = []

        for prop in self.list:
            if prop.name == name:
                properties.append(prop)

        return Properties_array(properties)

    def append(self, prop):
        self.list.append(prop)

    def get_cathegories(self):
        cathegories = [] # should be ordered

        for prop in self.list:
            if not prop.category in cathegories:
                cathegories.append(prop.category)

        return cathegories


    def get_names(self):
        names = [] # should be ordered

        for prop in self.list:
            if not prop.name in names:
                names.append(prop.name)

        return names

    def all_same_value(self):
        value = self.list[0].value.get()

        for prop in self.list:
            if prop.value.get() != value:
                return False

        return True

    def all_same_category(self):
        category = self.list[0].category

        for prop in self.list:
            if prop.category != category:
                return False

        return True

    def all_same_name(self):
        name = self.list[0].name

        for prop in self.list:
            if prop.name != name:
                return False

        return True


from .update_value import *
