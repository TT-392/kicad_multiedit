from .bitmap_button import *

class Subselector_control:
    def __init__(self, parent_window, parent, item_types, selected_item_types, update_func):
        self.update_func = update_func
        self.buttons = {}

        for Type in item_types:
            self.buttons[Type] = draw_bitmap_button(parent_window, parent, Type, True if Type in selected_item_types else False, self.update_func)
    

    def get_value(self):
        retval = []

        for Type in self.buttons:
            if self.buttons[Type].get_value():
                retval.append(Type)

        return retval



