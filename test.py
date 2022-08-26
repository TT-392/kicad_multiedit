from src.properties import *
from src.property import *
from src.eval_value import *


properties = Properties_array([
        Property("X", "Position", "length", 2),
        Property("X", "Position", "length", 2),
        Property("Y", "Position", "length", 3),
        Property("Y", "Position", "length", 4),
        Property("Angle", "Orientation", "angle", 90)
        ])

print(properties)

app = wx.App(False)
frame = GUI(None, 'Properties', properties)
app.MainLoop()

print(properties)
