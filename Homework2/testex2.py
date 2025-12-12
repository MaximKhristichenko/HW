import unittest
from ex2 import mnk

class Testmnk(unittest.TestCase):

    def test_1(self):
        a, b = mnk([1.0, 2.0, 3.0, 4.0], [4.0, 6.0, 7.0, 9.0])
        self.assertAlmostEqual(a, 1.6)
        self.assertAlmostEqual(b, 2.5)
    def test_2(self):
        a, b = mnk([3.0, 4.0], [1.0, 2.0])
        self.assertAlmostEqual(a, 1.0)
        self.assertAlmostEqual(b, -2.0)
    def test_3(self):
        a, b = mnk([1.0, 100.0], [99.0, 0.0])
        self.assertAlmostEqual(a, -1.0)
        self.assertAlmostEqual(b, 100.0)
    
if __name__ == "__main__":
    unittest.main()