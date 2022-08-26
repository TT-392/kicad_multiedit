# types: 'bool', 'string', 'length', 'lenght_unsigned', 'angle'
# Anything expressed in meters, inches, feet, lightyears is considered to be
# expressed in a unit of length, even if a coordinate or thickness isn't
# neccesarely considered "length'

class Property:
    def __init__(self, name, cathegory, data_type, value):
        self.name = name
        self.cathegory = cathegory
        self.data_type = data_type
        self.value = value
        self.ui_element = None

    def __str__(self):
        return "Property{" + self.name + ", " + self.cathegory + ", " + self.data_type + ", " + str(self.value) + "}"

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



    def contains_cathegory(self, cathegory):
        for prop in self.list:
            if prop.cathegory == cathegory:
                return True
        return False

    def contains_name(self, name):
        for prop in self.list:
            if prop.name == name:
                return True
        return False

    def get_in_cathegory(self, cathegory):
        properties = []

        for prop in self.list:
            if prop.cathegory == cathegory:
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
            if not prop.cathegory in cathegories:
                cathegories.append(prop.cathegory)

        return cathegories


    def get_names(self):
        names = [] # should be ordered

        for prop in self.list:
            if not prop.name in names:
                names.append(prop.name)

        return names

    def all_same_value(self):
        value = self.list[0].value

        for prop in self.list:
            if prop.value != value:
                return False

        return True

    def all_same_cathegory(self):
        cathegory = self.list[0].cathegory

        for prop in self.list:
            if prop.cathegory != cathegory:
                return False

        return True

    def all_same_name(self):
        name = self.list[0].name

        for prop in self.list:
            if prop.name != name:
                return False

        return True


