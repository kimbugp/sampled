import unittest

from line_intersection import intersection


class TestLineIntersection(unittest.TestCase):
    def test_no_intersect_with_values_unsorted(self):
        res = intersection(10, 5, 4, 2)
        self.assertEqual(res, False)

    def test_no_intersect_with_values_sorted(self):
        res = intersection(1, 2, 3, 4)
        self.assertEqual(res, False)

    def test_no_intersect_with_values_with_same_values(self):
        res = intersection(2, 2, 3, 4)
        self.assertEqual(res, False)

    def test_intersect_with_values_unsorted(self):
        res = intersection(8, 5, 9, 6)
        self.assertEqual(res, True)

    def test_intersect_with_values_sorted(self):
        res = intersection(2, 5, 4, 8)
        self.assertEqual(res, True)

    def test_intersect_with_values_with_same_values(self):
        res = intersection(2, 3, 2, 6)
        self.assertEqual(res, True)

    def test_no_intersect_with_negative_values(self):
        res = intersection(-10, -5, -3, -1)
        self.assertEqual(res, False)

    def test_intersect_with_negative_values(self):
        res = intersection(-10, -5, -6, -1)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()
