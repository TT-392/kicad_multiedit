import math
import os
import wx
import numpy as np

class utils:
    def rotate_around(coord, pivot, angle):
        r = math.hypot(coord[0] - pivot[0], coord[1] - pivot[1])
        angle = np.angle(coord[0] - pivot[0] + (coord[1] - pivot[1])*1j) + np.deg2rad(angle)
        x = math.cos(angle) * r + pivot[0]
        y = math.sin(angle) * r + pivot[1]
        
        return [utils.round(x), utils.round(y)]


    def translate(val, origin):
        val = list(val)
        val[0] -= origin[0][0]
        val[1] -= origin[0][1]

        if origin[1] == 0:
            pass
        elif origin[1] == 90:
            val = [-val[1], val[0]]
        elif origin[1] == 180:
            val = [-val[0], -val[1]]
        elif origin[1] == -90:
            val = [val[1], -val[0]]
        else:
            val = utils.rotate_around(val, (0, 0), origin[1])

        if val[0] == -0.0:
            val[0] = 0.0
        if val[1] == -0.0:
            val[1] = 0.0

        return val


    def reverse_translate(val, origin):
        val = utils.rotate_around(val, (0, 0), -origin[1])
        val[0] += origin[0][0]
        val[1] += origin[0][1]
        return val


    def round(val):
        if abs(val) <= 1E-14:
            val = 0

        return round(val, 14)


    def get_theme():
        sys_appearance = wx.SystemSettings.GetAppearance()
        return "dark" if sys_appearance.IsDark() else "light"


    def get_item_icon_path(item_type):
        from .icons import icons
        path = os.path.join(os.path.dirname(__file__), "../resources/output/" + utils.get_theme() + "/" + icons[item_type] + ".png")
        return path


    def to_parseable_string(data):
        special_chars = {"\"": "\\\"", "\\": "\\\\", "\'": "\\\'", "\n": "\\n"}

        if type(data) == str:
            retval = ""
            for c in data:
                if c in special_chars:
                    retval += special_chars[c]

                else:
                    retval += c

            return "\"" + retval + "\""

        else:
            return str(data)

