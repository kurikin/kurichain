from ecc import FE, Point
import unittest

class ECCTest(unittest.TestCase):

    def test_ex01(self):
        prime = 223

        def on_curve(x, y) -> bool:
            a = FE(0, prime)
            b = FE(7, prime)
            return y**2 == x**3 + a*x + b

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

    def test_ex03(self):
        prime = 223
        a = FE(0, prime)
        b = FE(7, prime)
        additions = (
                (192, 105, 17, 56, 170, 142),
                (47, 71, 117, 141, 60, 139),
                (143, 98, 76, 66, 47, 71)
        )
        for x1_raw, y1_raw, x2_raw, y2_raw, x3_raw, y3_raw in additions:
            x1 = FE(x1_raw, prime)
            y1 = FE(y1_raw, prime)
            p1 = Point(x1, y1, a, b)
            x2 = FE(x2_raw, prime)
            y2 = FE(y2_raw, prime)
            p2 = Point(x2, y2, a, b)
            x3 = FE(x3_raw, prime)
            y3 = FE(y3_raw, prime)
            p3 = Point(x3, y3, a, b)
            self.assertEqual(p1 + p2, p3)

    def test_ex04(self):
        prime = 223

        a = FE(0, prime)
        b = FE(7, prime)

        additions = (
                (192, 105, 49, 71, 2),
                (143, 98, 64, 168, 2),
                (47, 71, 36, 111, 2),
                (47, 71, 194, 51, 4),
                (47, 71, 116, 55, 8),
        )
        for x1_raw, y1_raw, x2_raw, y2_raw, count in additions:
            x1 = FE(x1_raw, prime)
            y1 = FE(y1_raw, prime)
            p = Point(x1, y1, a, b)

            expression = ' + '.join(['p'] * count)
            print(expression)
            result = eval(expression)

            x2 = FE(x2_raw, prime)
            y2 = FE(y2_raw, prime)
            q  = Point(x2, y2, a, b)
            self.assertEqual(result, q)

if __name__ == '__main__':
    unittest.main()
