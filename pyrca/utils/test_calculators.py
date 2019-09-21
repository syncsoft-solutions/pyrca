import unittest
from ..properties.node import Node
from .calculators import calculate_area, calculate_centroid_y


class TestCalculators(unittest.TestCase):
    def test_area(self):
        data = [Node(0, 0), Node(0, 400), Node(200, 400), Node(200, 0)]
        result = calculate_area(data)
        self.assertEqual(result, 80000, msg='Error in calculation of area!')

    def test_centroid_y(self):
        data = [Node(0, 0), Node(0, 400), Node(200, 400), Node(200, 0)]
        result = calculate_centroid_y(data)
        self.assertEqual(result, 200, msg='Error in calculation of centroid y.')


if __name__ == '__main__':
    unittest.main()