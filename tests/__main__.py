from .rotate_around import *
from .gui import *
import sys

if "rotate_around" in sys.argv:
    rotate_around.test()
    print("test rotate_around successful")

if "gui" in sys.argv:
    gui()
