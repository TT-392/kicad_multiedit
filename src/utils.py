import math
import numpy as np

class utils:
    def rotate_around(coord, pivot, angle):
        r = math.hypot(coord[0] - pivot[0], coord[1] - pivot[1])
        angle = np.angle(coord[0] - pivot[0] + (coord[1] - pivot[1])*1j) + np.deg2rad(angle)
        x = math.cos(angle) * r + pivot[0]
        y = math.sin(angle) * r + pivot[1]
        
        return [utils.round(x), utils.round(y)]

    def round(val):
        if abs(val) <= 1E-14:
            val = 0
        return round(val, 14)
