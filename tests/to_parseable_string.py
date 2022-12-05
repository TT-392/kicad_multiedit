from src.utils import *
from tests.resources import *
import math

def check(result, expected):
    assert expected == result, "expected: " + str(expected) + " but got: " + str(result)

class to_parseable_string:
    def test():
        check(eval(utils.to_parseable_string(True)), True)
        check(eval(utils.to_parseable_string(False)), False)
        check(eval(utils.to_parseable_string("interesting string")), "interesting string")
        check(eval(utils.to_parseable_string("text \n, text\\text\'\"")), "text \n, text\\text\'\"")
        check(eval(utils.to_parseable_string(32)), 32)
        check(eval(utils.to_parseable_string(32.43)), 32.43)
        check(eval(utils.to_parseable_string(-32)), -32)
        check(eval(utils.to_parseable_string(-32.43)), -32.43)





