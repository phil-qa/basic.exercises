import unittest

from prime_numbers import is_prime_number

class PrimeUnitTest(unittest.TestCase):
    """Tests for prime.py"""

    def test_return_type(self):
        self.assertIsInstance(is_prime_number(10),bool)

    def test_is_eleven_prime(self):
        self.assertTrue(is_prime_number(11))

    def test_special_one_is_prime(self):
        self.assertFalse(is_prime_number(1))

if __name__=='__main__':
    unittest.main(verbosity=2)