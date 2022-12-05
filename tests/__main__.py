import sys
from src.config import *


config.extended_checks = True
config.test_mode = True

if "rotate_around" in sys.argv:
    from .rotate_around import *
    rotate_around.test()
    print("test rotate_around successful")

if "gui" in sys.argv:
    from .gui import *
    gui()

if "python_field_variables" in sys.argv:
    python_field_variables()
