from .property import Property
from .field_evaluation.math import *
from .field_evaluation.regex import *
import math
import re
import wx

class Property(Property):
    def update_value(self):
        if self.data_type == 'string':
            if self.ui_element.GetValue()[:2] == "*s":
                self.put_ui_value(regex(self.get_ui_value() + self.ui_element.GetValue()[1:]))

            elif re.search("^\*\s*$", self.ui_element.GetValue()) == None:
                self.put_ui_value(self.ui_element.GetValue())



        elif self.data_type == 'length' or self.data_type == 'length_unsigned' or self.data_type == 'angle': #TODO: angles shouldn't go above 360 degrees
            try:
                self.put_ui_value(evaluate(self.ui_element.GetValue(), self))

            except (Exception, ArithmeticError) as e:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)

                wx.MessageBox(message, 'Error', wx.OK | wx.ICON_INFORMATION)
                return
