import unittest

class TestCalculator(unittest.TestCase):

    def test_two_numbers_are_added(self):
        self.assertEqual(self.calculator.add(1,2), 3)


if __name__== '__main__':
    unittest.main()