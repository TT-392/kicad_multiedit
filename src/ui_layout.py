from .kicad.kicad import *
from .ui_element import *
from .property import *
from .gui.elements import *

ui_layout = {
    "Position": {
        "X": Property(Type_python("unit user length"), "x"),
        "Y": Property(Type_python("unit user length"), "y")
    }, 
    "Orientation": {
        "Angle": Property(Type_python(), "rot")
    },
    "Graphic": {
        "Start X": Property(Type_python("unit user length"), "x1"),
        "Start Y": Property(Type_python("unit user length"), "y1"),
        "End X": Property(Type_python("unit user length"), "x2"),
        "End Y": Property(Type_python("unit user length"), "y2"),
        "Arc angle": Property(Type_python(), "arcAngle"),
        "Line width": Property(Type_python("unit user length"), "width"),
        "Radius": Property(Type_python("unit user length"), "radius")
    },
    "Text": {
        "Text": Property(Type_string(), "text"),
        "Width": Property(Type_python("unit user length"), "width"),
        "Height": Property(Type_python("unit user length"), "height")
    },
    "Text Items": {
        "Ref": Property(Type_string(), "ref")
    },
    "Fabrication Attributes": {
        "Not in schematic": Property(Type_checkbox(), "not_in_schematic")
    },
    "Miscellaneous": {
        "Layer": Property(Type_dropdown("all layers"), "layer"),
        "Visible": Property(Type_checkbox(), "visible")
    }
}

