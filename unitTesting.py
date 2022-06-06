import unittest

class Calculator:

    def add(self, first_operator, second_operator):
        return (first_operator + second_operator)


class TestCalculator(unittest.TestCase):
    calculator = Calculator()

    def test_two_numbers_are_added(self):
        self.assertEqual(self.calculator.add(1,2), 3)


if __name__== '__main__':
    unittest.main()