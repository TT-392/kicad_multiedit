from pcbnew import *

def fromUnit(x):
    return FromMM(x)
#    return FromMils(x)

def toUnit(x):
    return ToMM(x)
#    return toMils(x)
