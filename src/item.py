from .property import *
from .utils import *
from .kicad.kicad import *
from .field_evaluation.python_env import *

class Item:
    origin=((0,0), 0)

    def set_origin(self, origin):
        self.origin = origin

    def init_python_env(self, items, i):
        self.python_env = Python_env(items, self, i)

    def python_eval(self, string):
        return self.python_env.eval(string)

    # OPTIMIZATION: x_class and y_class can be combined into one class for items
    class translated_x:
        def __init__(self, item, x_class, y_class):
            self.x_obj = item.to_user_unit(item, x_class)
            self.y_obj = item.to_user_unit(item, y_class)
            self.item = item

        def put(self, value):
            coords = utils.translate((self.x_obj.get(), self.y_obj.get()), self.item.origin)
            coords[0] = value
            coords = utils.reverse_translate(coords, self.item.origin)
            self.x_obj.put(coords[0])
            self.y_obj.put(coords[1])

        def get(self):
            return utils.translate((self.x_obj.get(), self.y_obj.get()), self.item.origin)[0]

    class translated_y:
        def __init__(self, item, y_class, x_class):
            self.x_obj = item.to_user_unit(item, x_class)
            self.y_obj = item.to_user_unit(item, y_class)
            self.item = item

        def put(self, value):
            coords = utils.translate((self.x_obj.get(), self.y_obj.get()), self.item.origin)
            coords[1] = value
            coords = utils.reverse_translate(coords, self.item.origin)
            self.x_obj.put(coords[0])
            self.y_obj.put(coords[1])

        def get(self):
            return utils.translate((self.x_obj.get(), self.y_obj.get()), self.item.origin)[1]
        
    class translated_orientation:
        def __init__(self, item, rot_class):
            self.rot_obj = rot_class(item)
            self.item = item

        def put(self, value):
            self.rot_obj.put(value + self.item.origin[1])

        def get(self):
            return self.rot_obj.get() - self.item.origin[1]


    class to_user_unit:
        def __init__(self, item, value_class):
            self.item = item
            self.value_class = value_class(item)

        def put(self, value):
            self.value_class.put(kicad_info.fromUnit(value))

        def get(self):
            return kicad_info.toUnit(self.value_class.get())


class Items:
    def __init__(self, items):
        self.list = items

    def get_properties(self):
        properties = Properties([])
        
        for item in self.list:
            properties += item.properties


        return properties
    
    def get_icons(self):
        retval = []
        for item in self.list:
            if not item.icon in retval:
                retval.append(item.icon)
        
        return retval

    def get_types(self):
        retval = set([])
        for item in self.list:
            retval.add(type(item))
        
        return retval

