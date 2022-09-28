from .rotate_around import *
from .gui import *
from .python_field_variables import *
import sys

if "rotate_around" in sys.argv:
    rotate_around.test()
    print("test rotate_around successful")

if "gui" in sys.argv:
    gui()

if "python_field_variables" in sys.argv:
    python_field_variables()
