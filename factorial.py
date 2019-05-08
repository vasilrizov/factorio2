import unittest

FACTORIAL_NOT_DEFINED = "Factorial is not defined for that number"


def factorial(number):
    if number<0:
        raise Exception(FACTORIAL_NOT_DEFINED)
    elif number==0:
        return 1
    else:
        return factorial(number-1)*number


class FactorialTest(unittest.TestCase):

    def test_factorial_is_not_defined_on_negative_integers(self):
        try:
            factorial(-1)
            self.fail()
        except Exception as not_defined:
            self.assertEquals(FACTORIAL_NOT_DEFINED,str(not_defined))

    def test_factorial_of_base_number_is_one(self):
        self.assertEquals(1,factorial(0))

    def test_number_times_factorial_of_previous_is_factorial_for_other_numbers(self):
        self.assertEquals(6,factorial(3))

        print("this was for the test")