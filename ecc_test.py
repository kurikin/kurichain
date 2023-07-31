from ecc import FE, Point
import unittest

class ECCTest(unittest.TestCase):

    def test_on_curve(self):
        prime = 223
        a = FE(0, prime)
        b = FE(7, prime)
        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))
        for x_raw, y_raw in valid_points:
            x = FE(x_raw, prime)
            y = FE(y_raw, prime)
            Point(x, y, a, b)

        for x_raw, y_raw in invalid_points:
            x = FE(x_raw, prime)
            y = FE(y_raw, prime)
            with self.assertRaises(ValueError):
                Point(x, y, a, b)
