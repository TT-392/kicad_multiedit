from .kicad.kicad import *
from .ui_element import *
from .property import *
from .gui.elements import *

ui_layout = {
    "Position": {
        "X": Property(None, None, Type_python("mm"), None, None, "x"),
        "Y": Property(None, None, Type_python("mm"), None, None, "y")
    }, 
    "Orientation": {
        "Angle": Property(None, None, Type_python(), None, None, "rot")
    },
    "Text Items": {
        "Ref": Property(None, None, Type_string(), None, None, "ref")
    },
    "Fabrication Attributes": {
        "Not in schematic": Property(None, None, Type_checkbox(), None, None, "not_in_schematic")
    },
    "Line": {
        "Width": Property(None, None, Type_python("mm"), None, None, "width")
    }
}

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

