import unittest
from ..properties.node import Node
from .calculators import calculate_area


class TestCalculators(unittest.TestCase):
    def test_area(self):
        data = [Node(0, 0), Node(0, 400), Node(200, 400), Node(200, 0)]
        result = calculate_area(data)
        self.assertEqual(result, 80000, msg='Error in calculation of area!')


if __name__ == '__main__':
    unittest.main()