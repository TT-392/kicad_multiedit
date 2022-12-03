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


    def put_ui_value(self, ui_val):
        for value in self.values:
            new_value = value.item.python_eval(ui_val)
            
            if new_value != value.get():
                value.put(new_value)
                print("putting 1 value")


    def register(self, value_obj):
        self.values.append(value_obj)


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
            if name == "widget_type": #TODO When new property type system is written, they should actually be the same object, and this exception shouldn't be needed anymore
                val0 = type(utils.get_member(self.__list[0], name))
            else:
                val0 = utils.get_member(self.__list[0], name)

            for i in self.__list: 
                if name == "widget_type": #TODO When new property type system is written, they should actually be the same object, and this exception shouldn't be needed anymore
                    val = type(eval("i." + name))
                else:
                    val = eval("i." + name)

                if val != val0:
                    print(str(val0) + " != " + str(eval("i." + name)))
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

