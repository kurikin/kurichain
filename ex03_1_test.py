import unittest
from ecc import FE

prime = 223

def on_curve(x, y) -> bool:
    a = FE(0, prime)
    b = FE(7, prime)
    return y**2 == x**3 + a*x + b

class TestOnCurve(unittest.TestCase):

    def test_all_points(self):
        x1, y1 = FE(192, prime), FE(105, prime)
        x2, y2 = FE(17, prime), FE(56, prime)
        x3, y3 = FE(200, prime), FE(119, prime)
        x4, y4 = FE(1, prime), FE(193, prime)
        x5, y5 = FE(42, prime), FE(99, prime)

        self.assertEqual(on_curve(x1, y1), True)
        self.assertEqual(on_curve(x2, y2), True)
        self.assertEqual(on_curve(x3, y3), False)
        self.assertEqual(on_curve(x4, y4), True)
        self.assertEqual(on_curve(x5, y5), False)

if __name__ == '__main__':
    unittest.main()
