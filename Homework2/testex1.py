import unittest
from ex1 import prime

class TestPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(prime(2), [2])
    def test_2(self):
        self.assertEqual(prime(6), [2, 3])
        self.assertEqual(prime(12), [2, 2, 3])
    def test_3(self):
        self.assertEqual(prime(97), [97])
    def test_4(self):
        self.assertEqual(prime(100000000), [2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5])

if __name__ == "__main__":
    unittest.main()