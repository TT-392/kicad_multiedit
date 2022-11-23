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

