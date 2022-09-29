import math
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
        return utils.rotate_around(val, (0, 0), origin[1])

    def reverse_translate(val, origin):
        val = utils.rotate_around(val, (0, 0), -origin[1])
        val[0] += origin[0][0]
        val[1] += origin[0][1]
        return val


    def round(val):
        if abs(val) <= 1E-14:
            val = 0
        return round(val, 14)

