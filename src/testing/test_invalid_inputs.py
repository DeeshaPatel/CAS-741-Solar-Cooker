import sys
import os
sys.path.insert(0, '../src/')

from builtins import ValueError
import unittest
from src import load_params, verify_params


# Class to test invalid inputs
class TestInvalidInput(unittest.TestCase):

    # Test case for Area Inputs to check zero or negative values

    def test_area_input(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In01.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of lid must be > 0 \n', verify_params.verify_input, params)

    def test_area_ref(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In02.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of reflector must be > 0 \n', verify_params.verify_input, params)

    def test_area_m(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In03.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of mass must be > 0 \n', verify_params.verify_input, params)

    def test_area_glass_1(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In07.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of glass 1 must be > 0 \n', verify_params.verify_input, params)

    def test_area_glass_2(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In08.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of glass 2 must be > 0 \n', verify_params.verify_input, params)

    # Test case for Area Inputs to check large values

    def test_large_area_lid(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In04.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of lid must be between 0 to 20 \n',
                               verify_params.verify_input, params)

    def test_large_area_reflector(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In05.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of reflector must be between 0 to 20 \n',
                               verify_params.verify_input, params)

    def test_large_area_mass(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In06.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of mass must be between 0 to 20 \n',
                               verify_params.verify_input, params)

    def test_large_area_glass_1(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In09.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of glass 1 must be between 0 to 5 \n',
                               verify_params.verify_input, params)

    def test_large_area_glass_2(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In10.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Area of glass 2 must be between 0 to 5 \n',
                               verify_params.verify_input, params)

    # Test case to test input initial temperature against zero and negative values

    def test_temperature_lid(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In11.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Temperature of lid must be > 0 \n',
                               verify_params.verify_input, params)

    def test_temperature_fluid(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In12.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Temperature of fluid must be > 0 \n',
                               verify_params.verify_input, params)

    def test_temperature_reflector(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In13.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Temperature of reflector must be > 0 \n',
                               verify_params.verify_input, params)

    def test_temperaturE_Glass2(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In14.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Temperature of glass 2 must be > 0 \n',
                               verify_params.verify_input, params)

    # Test case to test input initial temperature against excess values

    def test_excess_temperature_lid(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In15.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Excess temperature value of lid \n',
                               verify_params.verify_input, params)

    def test_excess_temperature_fluid(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In16.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Excess temperature value of fluid \n',
                               verify_params.verify_input, params)

    def test_excess_temperature_reflector(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In17.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Excess temperature value of reflector \n',
                               verify_params.verify_input, params)

    def test_excess_temperaturE_Glass2(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In18.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'Excess temperature value of glass 2 \n',
                               verify_params.verify_input, params)

    # Test case to check emissivity values

    def test_emissivity_lid(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In19.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'The given input of emissivity must '
                                           'be between 0 and 1 \n',
                               verify_params.verify_input, params)

    def test_emissivity_reflector(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalidInput', 'In20.txt'))
        params = load_params.load_params(file_path)
        self.assertRaisesRegex(ValueError, 'The given input of emissivity must '
                                           'be between 0 and 1 \n',
                               verify_params.verify_input, params)


class InvalidInputSuite:
    def suite(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInvalidInput)
        return suite
