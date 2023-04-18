import sys
import os
sys.path.insert(0, '../src/')
import src.load_params as load_params
import unittest


class TestLoadParams(unittest.TestCase):

    def setUp(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.in'))
        self.params = load_params.load_params(file_path)

    def test_parameter_area_lid(self):
        self.assertEqual(self.params.A_t, 0.0201, 'A_t')

    def test_parameter_temperature_lid(self):
        self.assertEqual(self.params.T_t, 30, 'T_t')

    def test_parameter_temperature_fluid(self):
        self.assertEqual(self.params.T_f, 30, 'T_f')

    def test_parameter_emissivity_lid(self):
        self.assertEqual(self.params.e_t, 0.85, 'e_t')

    def test_parameter_area_reflector(self):
        self.assertEqual(self.params.A_ref, 0.0804, 'A_ref')

    def test_parameter_temperature_reflector(self):
        self.assertEqual(self.params.T_ref, 30, 'T_ref')

    def test_parameter_emissivity_reflector(self):
        self.assertEqual(self.params.e_ref, 0.84, 'e_ref')

    def test_parameter_temperature_glass(self):
        self.assertEqual(self.params.T_g2, 30, 'T_g2')

    def test_parameter_area_mass(self):
        self.assertEqual(self.params.A_m, 0.064, 'A_m')

    def test_parameter_area_glass1(self):
        self.assertEqual(self.params.A_g1, 0.4761, 'A_g1')

    def test_parameter_area_glass2(self):
        self.assertEqual(self.params.A_g2, 0.4761, 'A_g2')


class LoadInputSuite:

    def suite(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestLoadParams)
        return suite
