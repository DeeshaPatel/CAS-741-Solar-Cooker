import sys
import os

import pytest

sys.path.insert(0, '../src/')

import unittest
from src import calculation, load_params


class TestTemperature(unittest.TestCase):

    # Test case with normal inputs
    def test_temperature_01(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'validInputForTestTemp', 'In01.in'))
        params = load_params.load_params(file_path)
        init_temp1 = [params.T_ref, params.T_f, params.T_g2, params.T_t, params.T_g2]
        t1 = [0, 10, 20, 30, 40]
        output = [0.17439055871999998, 0.0, 18.49248576, 1.983937536, 4912898.001264997]
        temp1 = calculation.calculate_temp(init_temp1, t1, params)
        self.assertAlmostEqual(temp1[0], output[0], places=None, msg='Temperature of Reflector')
        self.assertAlmostEqual(temp1[1], output[1], places=None, msg='Temperature of Fluid')
        self.assertAlmostEqual(temp1[2], output[2], places=None, msg='Temperature of Glass 2')
        self.assertAlmostEqual(temp1[3], output[3], places=None, msg='Temperature of Lid')
        self.assertAlmostEqual(temp1[4], output[4], places=None, msg='Temperature of Glass 1')

    # Test case with high inputs
    def test_temperature_02(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'validInputForTestTemp', 'In02.in'))
        params = load_params.load_params(file_path)
        init_temp = [params.T_ref, params.T_f, params.T_g2, params.T_t, params.T_g2]
        t = [0, 10, 20, 30, 40]
        output = [0.20800055105566442, 0.004468510260142362, 2012.6495254309657, 9.128765290349056, 4912898.001264997]
        temp = calculation.calculate_temp(init_temp, t, params)
        self.assertAlmostEqual(temp[0], output[0], places=None, msg='Temperature of Reflector')
        self.assertAlmostEqual(temp[1], output[1], places=None, msg='Temperature of Fluid')
        self.assertAlmostEqual(temp[2], output[2], places=None, msg='Temperature of Glass 2')
        self.assertAlmostEqual(temp[3], output[3], places=None, msg='Temperature of Lid')
        self.assertAlmostEqual(temp[4], output[4], places=None, msg='Temperature of Glass 1')

    # Test case with low inputs
    def test_temperature_03(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'validInputForTestTemp', 'In03.in'))
        params = load_params.load_params(file_path)
        init_temp = [params.T_ref, params.T_f, params.T_g2, params.T_t, params.T_g2]
        t = [0, 10, 20, 30, 40]
        output = [0.26028441599999996, 0.0, 18.49248576, 8.78459904, 26747829.04330682]
        temp = calculation.calculate_temp(init_temp, t, params)
        self.assertAlmostEqual(temp[0], output[0], places=None, msg='Temperature of Reflector')
        self.assertAlmostEqual(temp[1], output[1], places=None, msg='Temperature of Fluid')
        self.assertAlmostEqual(temp[2], output[2], places=None, msg='Temperature of Glass 2')
        self.assertAlmostEqual(temp[3], output[3], places=None, msg='Temperature of Lid')
        self.assertAlmostEqual(temp[4], output[4], places=None, msg='Temperature of Glass 1')

    def test_negative_temperature_04(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'validInputForTestTemp', 'In04.in'))
        params = load_params.load_params(file_path)
        init_temp = [params.T_ref, params.T_f, params.T_g2, params.T_t, params.T_g2]
        t = [10, 10, 10, 10, 10]
        temp = calculation.calculate_temp(init_temp, t, params)
        if temp[4] < 0:
            pytest.fail("Temperature of glass 1 should be > 0 \n")
        elif temp[2] < 0:
            pytest.fail("Temperature of glass 2 should be > 0 \n")
        elif temp[0] < 0:
            pytest.fail("Temperature of reflector should be > 0 \n")
        elif temp[1] < 0:
            pytest.fail("Temperature of fluid should be > 0 \n")
        elif temp[3] < 0:
            pytest.fail("Temperature of lid should be > 0 \n")

class TempSuite:
    def suite(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestTemperature)
        return suite
