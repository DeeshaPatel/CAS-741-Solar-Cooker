import os.path
import sys
sys.path.insert(0, '../src/')

import src.load_params as load_params
import src.energy_calculation as energy_calculation

import unittest
import pytest


class TestEnergy(unittest.TestCase):

    def setUp(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.in'))
        self.params = load_params.load_params(file_path)

    # Test case with high temperature
    def test_energy_01(self):
        temp = [40, 41, 42, 43]
        output = [8380.0, 9218.0, 10056.0, 10894.0]
        energy = energy_calculation.energywat(temp, self.params.T_f)
        self.assertAlmostEqual(energy[0], output[0], places=None, msg='Energy 01')
        self.assertAlmostEqual(energy[1], output[1], places=None, msg='Energy 02')
        self.assertAlmostEqual(energy[2], output[2], places=None, msg='Energy 03')
        self.assertAlmostEqual(energy[3], output[3], places=None, msg='Energy 04')

    # Test case with low temperature
    def test_energy_02(self):
        temp = [30, 31, 32, 33]
        output = [0.0, 838.0, 1676.0, 2514.0]
        energy = energy_calculation.energywat(temp, self.params.T_f)
        self.assertAlmostEqual(energy[0], output[0], places=None, msg='Energy 01')
        self.assertAlmostEqual(energy[1], output[1], places=None, msg='Energy 02')
        self.assertAlmostEqual(energy[2], output[2], places=None, msg='Energy 03')
        self.assertAlmostEqual(energy[3], output[3], places=None, msg='Energy 04')

    # Test case with low temperature
    def test_energy_03(self):
        temp = [10, 11, 12, 13]
        energy = energy_calculation.energywat(temp, self.params.T_f)
        for e1 in energy:
            if e1 < 0:
                pytest.fail("Energy value is negative")

    # Test case with low temperature
    def test_energy_04(self):
        temp = [60, 62, 62, 64]
        energy = energy_calculation.energywat(temp, self.params.T_f)
        for e1 in energy:
            if e1 < 0:
                pytest.fail("Energy value is negative")


class EnergySuite:
    def suite(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestEnergy)
        return suite
