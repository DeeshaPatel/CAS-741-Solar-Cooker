import sys
import os
sys.path.insert(0, '../src/')
import src.load_params as load_params
import src.constant as constant
import unittest


class TestConstParams(unittest.TestCase):

    def setUp(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.in'))
        self.params = load_params.load_params(file_path)

    def test_STEFAN_CONST(self):
        self.assertEqual(constant.STEFAN_CONST, 5.670374419e-08, 'STEFAN_CONST')

    def test_H_G1_INT1(self):
        self.assertEqual(constant.H_G1_INT1, 3.8, 'H_G1_INT1')

    def test_H_G1_AMB(self):
        self.assertEqual(constant.H_G1_AMB, 13.3, 'H_G1_AMB')

    def test_H_T_INT2(self):
        self.assertEqual(constant.H_T_INT2, 4.4, 'H_T_INT2')

    def test_H_G2_INT1(self):
        self.assertEqual(constant.H_G2_INT1, 4.4, 'H_G2_INT1')

    def test_H_T_INT3(self):
        self.assertEqual(constant.H_T_INT3, 4.0, 'H_T_INT3')

    def test_H_REF_INT2(self):
        self.assertEqual(constant.H_REF_INT2, 4.4, 'H_REF_INT2')

    def test_H_REF_F(self):
        self.assertEqual(constant.H_REF_F, 4.0, 'H_REF_F')

    def test_E_G(self):
        self.assertEqual(constant.E_G, 0.35, 'E_G')

    def test_T_AMB(self):
        self.assertEqual(constant.T_AMB, 34.5, 'T_AMB')

    def test_ALPHA_G1(self):
        self.assertEqual(constant.ALPHA_G1, 0.17, 'ALPHA_G1')

    def test_ALPHA_T(self):
        self.assertEqual(constant.ALPHA_T, 0.9, 'ALPHA_T')

    def test_C_R(self):
        self.assertEqual(constant.C_R, 900, 'C_R')

    def test_C_F(self):
        self.assertEqual(constant.C_F, 4190, 'C_F')

    def test_M_F(self):
        self.assertEqual(constant.M_F, 0.2, 'M_F')

    def test_M_R(self):
        self.assertEqual(constant.M_R, 0.2, 'M_R')

    def test_G(self):
        self.assertEqual(constant.G, 476, 'G')

    def test_P(self):
        self.assertEqual(constant.P, 0.89, 'P')

    def test_T_G(self):
        self.assertEqual(constant.T_G, 0.48, 'T_G')

    def test_THETA_REF(self):
        self.assertEqual(constant.THETA_REF, 90, 'THETA_REF')

class ConstantSuite:
    def suite(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestConstParams)
        return suite
