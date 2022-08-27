from .property import Property
from .regex import regex
import math
import re

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


class Property(Property):
    def eval(self):
        if self.data_type == 'string':
            if self.ui_element.GetValue()[:2] == "*s":
                value = regex(self.value + self.ui_element.GetValue()[1:])

            elif re.search("^\*\s*$", self.ui_element.GetValue()) == None:
                value = self.ui_element.GetValue()

            else:
                value = self.value


        if self.data_type == 'length' or self.data_type == 'length_unsigned' or self.data_type == 'angle': #TODO: angles shouldn't go above 360 degrees
            if re.search("^\d*\s*$", self.ui_element.GetValue()) != None:
                value = int(self.ui_element.GetValue())

            else:
                x = self.value
                try:
                    value = eval(self.ui_element.GetValue())

                except (Exception, ArithmeticError) as e:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(e).__name__, e.args)

                    wx.MessageBox(message, 'Error', wx.OK | wx.ICON_INFORMATION)


        if value != self.value:
            self.value = value
            return True
        else:
            return False

