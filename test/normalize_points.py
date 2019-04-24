import unittest
from util import normalize_points


class TestNormalizePoints(unittest.TestCase):
    def test_quadrant_one(self):
        # Test where second point is in Quadrant 1 relative to first point
        origin = [10, 10]
        corner = [15, 5]

        result = normalize_points(origin, corner)
        # X of first point in result is origin x
        self.assertEqual(result[0][0], origin[0])
        # Y of first point is corner Y
        self.assertEqual(result[0][1], corner[1])

        # X of second point is corner X
        self.assertEqual(result[1][0], corner[0])
        # Y of second point is origin Y
        self.assertEqual(result[1][1], origin[1])

    def test_quadrant_two(self):
        pass

    def test_quadrant_three(self):
        pass

    def test_quadrant_four(self):
        pass
