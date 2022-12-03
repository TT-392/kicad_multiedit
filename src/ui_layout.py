from .kicad.kicad import *
from .ui_element import *
from .property import *
from .gui.elements import *

ui_layout = {
    "Position": {
        "X": Property(None, None, Type_python("unit user length"), None, None, "x"),
        "Y": Property(None, None, Type_python("unit user length"), None, None, "y")
    }, 
    "Orientation": {
        "Angle": Property(None, None, Type_python(), None, None, "rot")
    },
    "Graphic": {
        "Start X": Property(None, None, Type_python("unit user length"), None, None, "x1"),
        "Start Y": Property(None, None, Type_python("unit user length"), None, None, "y1"),
        "End X": Property(None, None, Type_python("unit user length"), None, None, "x2"),
        "End Y": Property(None, None, Type_python("unit user length"), None, None, "y2"),
        "Arc angle": Property(None, None, Type_python(), None, None, "arcAngle"),
        "Line width": Property(None, None, Type_python("unit user length"), None, None, "width"),
        "Radius": Property(None, None, Type_python("unit user length"), None, None, "radius")
    },
    "Text": {
        "Text": Property(None, None, Type_string(), None, None, "text"),
        "Width": Property(None, None, Type_python("unit user length"), None, None, "width"),
        "Height": Property(None, None, Type_python("unit user length"), None, None, "height")
    },
    "Text Items": {
        "Ref": Property(None, None, Type_string(), None, None, "ref")
    },
    "Fabrication Attributes": {
        "Not in schematic": Property(None, None, Type_checkbox(), None, None, "not_in_schematic")
    },
    "Miscellaneous": {
        "Layer": Property(None, None, Type_dropdown("all layers"), None, None, "layer"),
        "Visible": Property(None, None, Type_checkbox(), None, None, "visible")
    }
}

