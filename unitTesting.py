import sys
import unittest
from io import StringIO


class Calculator:

    def add(self, first_operator, second_operator):
        try:
            return first_operator + second_operator
        except TypeError:
            print("Use only numeric values")


class TestCalculator(unittest.TestCase):
    calculator = Calculator()

    def test_two_numbers_are_added(self):
        self.assertEqual(self.calculator.add(1, 2), 3)

    def test_at_least_one_input_is_non_numeric(self):
        capture_output = StringIO()
        sys.stdout = capture_output
        self.calculator.add(1, "r")
        sys.stdout = sys.__stdout__
        response_value = capture_output.getvalue()
        print(f"captured {response_value}")
        self.assertEqual("Use only numeric values", response_value)


if __name__ == '__main__':
    unittest.main()
