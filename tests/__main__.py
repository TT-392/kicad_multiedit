import sys
from src.config import *


config.extended_checks = True
config.test_mode = True

if "rotate_around" in sys.argv:
    from .rotate_around import *
    rotate_around.test()
    print("test rotate_around successful")

if "to_parseable_string" in sys.argv:
    from .to_parseable_string import *
    to_parseable_string.test()
    print("test to_parseable_string successful")

if "gui" in sys.argv:
    from .gui import *
    gui()

if "python_field_eval" in sys.argv:
    from .python_field_eval import *
    python_field_eval()
    print("test python_field_eval successful")

