from .kicad.kicad import *
from .utils import *
from .config import *

# data_types: 'bool', 'string', 'length', 'lenght_unsigned', 'angle'
# Anything expressed in meters, inches, feet, lightyears is considered to be
# expressed in a unit of length, even if a coordinate or thickness isn't
# neccesarely considered "length'
# translatable_types: 'None', 'x', 'y', 'rot'

class Property:
    def __init__(self, name, category, data_type, value, item, varname=None, translatable_type=None):
        self.name = name
        self.category = category
        self.data_type = data_type
        self.item = item
        self.varname = varname
        self.translatable_type = translatable_type

        self.value = value

        self.ui_element = None

        kicad_info.update()

    def __str__(self):
        return "Property{" + self.name + ", " + self.category + ", " + self.data_type + ", " + str(self.get_ui_value()) + "}"

    def get_ui_value(self):
        if self.data_type == "string":
            return self.value.get()
        else:
            return str(self.value.get())

    def put_ui_value(self, ui_val):
        if self.get_ui_value() == ui_val:
            return

        if self.data_type == "string":
            self.value.put(ui_val)
        else:
            self.value.put(self.item.python_eval(ui_val))




class Properties:
    def __init__(self, properties):
        self.__list = properties

    def __str__(self):
        retval = "Properties {"

        for prop in self.__list:
            retval += "\n"
            retval += str(prop)
            retval += ","

        retval = retval[:-1]

        retval += "}"

        return retval
    
    def __add__(self, other):
        return Properties(self.__list + other.__list)

    def get(self, name):
        if config.extended_checks:
            val0 = utils.get_member(self.__list[0], name)

            for i in self.__list: 
                if eval("i." + name) != val0:
                    assert 0, "ERROR: mismatched " + name + " values"

        return utils.get_member(self.__list[0], name)

    def get_all(self, name):
        retval = []

        for prop in self.__list:
            value = utils.get_member(prop, name)
            if not value in retval:
                retval.append(value)

        return retval


    def get_in_category(self, category):
        properties = []

        for prop in self.__list:
            if prop.category == category:
                properties.append(prop)

        return Properties(properties)

    def get_in_category_and_with_name(self, category, name):
        properties = []

        for prop in self.__list:
            if prop.category == category and prop.name == name:
                properties.append(prop)

        return Properties(properties)

    def append(self, prop):
        self.__list.append(prop)

    def all_same_value(self):
        value = self.__list[0].value.get()

        for prop in self.__list:
            if prop.value.get() != value:
                return False

        return True

    def get_items(self):
        items = []
        for prop in self.__list:
            items.append(prop.item)
        return items

    def get_ui_value(self):
        assert len(self.__list) != 0, "Properties array empty"
        assert self.all_same_value(), "Mismatched ui values in properties array"

        return self.__list[0].get_ui_value()

    def put_ui_value(self, value):
        assert len(self.__list) != 0, "Properties array empty"

        for prop in self.__list:
            prop.put_ui_value(value)

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, i):
        return self.__list[i]

