
import unittest
from prime_checker import is_prime


class TestPrimeChecker(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(7))

    def test_not_prime(self):
        self.assertFalse(is_prime(10))


if __name__ == "__main__":
    unittest.main()
