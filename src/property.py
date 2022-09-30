from .kicad.kicad import *
from .utils import *

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
            self.value.put(float(ui_val))




class Properties_array:
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
        return Properties_array(self.__list + other.__list)

    def is_empty(self):
        if len(self.__list) == 0:
            return True
        else:
            return False

    def contains_category(self, category):
        for prop in self.__list:
            if prop.category == category:
                return True
        return False

    def contains_name(self, name):
        for prop in self.__list:
            if prop.name == name:
                return True
        return False

    def get_in_category(self, category):
        properties = []

        for prop in self.__list:
            if prop.category == category:
                properties.append(prop)

        return Properties_array(properties)

    def get_with_name(self, name):
        properties = []

        for prop in self.__list:
            if prop.name == name:
                properties.append(prop)

        return Properties_array(properties)

    def get_in_category_and_with_name(self, category, name):
        properties = []

        for prop in self.__list:
            if prop.category == category and prop.name == name:
                properties.append(prop)

        return Properties_array(properties)

    def append(self, prop):
        self.__list.append(prop)

    def get_categories(self):
        categories = [] # should be ordered

        for prop in self.__list:
            if not prop.category in categories:
                categories.append(prop.category)

        return categories


    def get_names(self):
        names = [] # should be ordered

        for prop in self.__list:
            if not prop.name in names:
                names.append(prop.name)

        return names

    def get_varnames(self):
        varnames = [] # should be ordered

        for prop in self.__list:
            if not prop.varname in varnames:
                if not prop.varname == None:
                    varnames.append(prop.varname)

        return varnames

    def all_same_value(self):
        value = self.__list[0].value.get()

        for prop in self.__list:
            if prop.value.get() != value:
                return False

        return True

    def all_same_category(self):
        category = self.__list[0].category

        for prop in self.__list:
            if prop.category != category:
                return False

        return True

    def all_same_name(self):
        name = self.__list[0].name

        for prop in self.__list:
            if prop.name != name:
                return False

        return True

    def get_items(self):
        items = []
        for prop in self.__list:
            items.append(prop.item)
        return items

    #NOTE: These could be run at creation of object, assuming an empty array is never created
    def get_variable_name(self):
        assert len(self.__list) != 0, "Properties array empty"

        retval = self.__list[0].varname
        
        for prop in self.__list[1:]:
            assert prop.varname == retval, "Mismatched varnames in properties array"

        return retval

    def get_data_type(self):
        assert len(self.__list) != 0, "Properties array empty"

        retval = self.__list[0].data_type
        
        for prop in self.__list[1:]:
            assert prop.data_type == retval, "Mismatched data types in properties array"

        return retval
    
    def get_ui_value(self):
        assert len(self.__list) != 0, "Properties array empty"
        assert self.all_same_value(), "Mismatched ui values in properties array"

        return self.__list[0].get_ui_value()

    def put_ui_value(self, value):
        assert len(self.__list) != 0, "Properties array empty"

        for prop in self.__list:
            prop.put_ui_value(value)

    def get_list(self):
        return self.__list



            


from .update_value import *
