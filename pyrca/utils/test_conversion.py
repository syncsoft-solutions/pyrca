import unittest
from pyrca.utils.conversion import *


class TestConversion(unittest.TestCase):
    def test_mpa_to_psi(self):
        mpa = 10
        result = mpa_to_psi(mpa)
        self.assertAlmostEqual(result, 1450.38, 2, msg='Wrong conversion!')

    def test_psi_to_mpa(self):
        psi = 10
        result = psi_to_mpa(psi)
        self.assertAlmostEqual(result, 0.0689476, 5, msg='Wrong conversion!')

    def test_mm_to_inch(self):
        mm = 10
        result = mm_to_in(mm)
        self.assertAlmostEqual(result, 0.393701, 4, msg='Wrong conversion!')

    def test_inch_to_mm(self):
        inch = 10
        result = in_to_mm(inch)
        self.assertEqual(result, 254, msg='Wrong conversion!')


if __name__ == '__main__':
    unittest.main()
