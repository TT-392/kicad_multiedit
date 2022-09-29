from src.utils import *
from tests.resources import *
import math

def check(array1, array2, allowable_error):
    for i in range(0, len(array1)):
        if math.fabs(array1[i] - array2[i]) > allowable_error:
            return False
    return True


class rotate_around:
    def test():
        assert(check(utils.rotate_around((10, 0), (0, 0), 90), [0, 10.0], 0))
        assert(check(utils.rotate_around((10, 0), (0, 0), 45), [7.0710678118654755, 7.071067811865475], 0.001))
        assert(check(utils.rotate_around((10, 0), (0, 0), 170),[-9.84807753012208, 1.7364817766693028], 0.001))
        assert(check(utils.rotate_around((1, 9), (5, 9), 90),  [5, 5], 0))
        assert(check(utils.rotate_around((1, 9), (5, 9), 45),  [2.1715728752538093, 6.17157287525381], 0.001))
        assert(check(utils.rotate_around((1, 9), (5, 9), 170), [8.939231012048833, 8.305407289332278], 0.001))
        assert(check(utils.rotate_around((1, 9), (5, 9), 333), [1.4359739032465275, 10.815961998958185], 0.001))

        
        assert(check(utils.translate((0, 0), ((10, 5), 0)), (-10, -5), 0))
        assert(check(utils.translate((34.2, 20.2), ((30, 20), 0)), (4.2, .2), 0))
        assert(check(utils.translate((38, 20), ((30, 20), 45)), (math.sqrt(math.pow(8, 2)/2), math.sqrt(math.pow(8, 2)/2)), 0.001))
        assert(check(utils.translate((-10, 10 + math.sqrt(2*math.pow(8, 2))), ((-10, 10), -45)), (8, 8), 0))


        assert(check(utils.reverse_translate((-10, -5), ((10, 5), 0)), (0, 0), 0))
        assert(check(utils.reverse_translate((4.2, .2), ((30, 20), 0)), (34.2, 20.2), 0))
        assert(check(utils.reverse_translate((math.sqrt(math.pow(8, 2)/2), math.sqrt(math.pow(8, 2)/2)), ((30, 20), 45)), (38, 20), 0.001))
        assert(check(utils.reverse_translate((0, math.sqrt(2*math.pow(8, 2))), ((-20, 10), -45)), (-28, 18), 0))




