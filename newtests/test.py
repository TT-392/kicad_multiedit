from termcolor import colored

class Test():
    identifier_string = "Placeholder"

    def __compare(self, value_1, value_2, allowable_error):
        if allowable_error == None:
            return value_1 == value_2
        else:
            return abs(value_1 - value_2) < allowable_error

    def test(self, value, expected_value, identifier_string, allowable_error = None):
        if not self.__compare(value, expected_value, allowable_error):
            print("[" + colored("FAIL", "red") + "]", self.identifier_string + ":", identifier_string)
            print("    expected", expected_value, "but got", value)

            self.result["Fail"] += 1
            return False
        else:
            if self.verbose:
                print("[" + colored("PASS", "green") + "]", self.identifier_string + ":", identifier_string)

            self.result["Pass"] += 1
            return True

