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
        self.assertEqual(self.params.a_t, 0.0201, 'a_t')

    def test_parameter_temperature_lid(self):
        self.assertEqual(self.params.t_t, 30, 'T_t')

    def test_parameter_temperature_fluid(self):
        self.assertEqual(self.params.t_f, 30, 'T_f')

    def test_parameter_emissivity_lid(self):
        self.assertEqual(self.params.e_t, 0.85, 'e_t')

    def test_parameter_area_reflector(self):
        self.assertEqual(self.params.a_ref, 0.0804, 'A_ref')

    def test_parameter_temperature_reflector(self):
        self.assertEqual(self.params.t_ref, 30, 't_ref')

    def test_parameter_emissivity_reflector(self):
        self.assertEqual(self.params.e_ref, 0.84, 'e_ref')

    def test_parameter_temperaturE_Glass(self):
        self.assertEqual(self.params.t_g2, 30, 't_g2')

    def test_parameter_area_mass(self):
        self.assertEqual(self.params.a_m, 0.064, 'A_m')

    def test_parameter_area_glass1(self):
        self.assertEqual(self.params.a_g1, 0.4761, 'A_g1')

    def test_parameter_area_glass2(self):
        self.assertEqual(self.params.a_g2, 0.4761, 'A_g2')


class LoadInputSuite:

    def suite(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestLoadParams)
        return suite
