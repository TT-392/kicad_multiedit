import math

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def atan(x):
    return math.atan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def snap(x, amount):
    x = x / amount
    x = round(x, 0)
    return x * amount


def evaluate(string, prop):
    x = prop.get_ui_value()
    return eval(string)
