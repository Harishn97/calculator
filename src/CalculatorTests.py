import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    # def test_add_method_calculator(self):
    #     self.assertEqual(self.calculator.add(2, 2), 4)
    #     self.assertEqual(self.calculator.result, 4)

    def test_add(self):
        test_data = CsvReader('/src/csv/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('/src/csv/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    # def test_subtract_method_calculator(self):
    #     self.assertEqual(self.calculator.subtract(2, 2), 0)
    #     self.assertEqual(self.calculator.result, 0)

    # def test_multiply_method_calculator(self):
    #     self.assertEqual(self.calculator.multiply(2, 2), 4)
    #     self.assertEqual(self.calculator.result, 4)
    #
    # def test_divide_method_calculator(self):
    #     self.assertEqual(self.calculator.divide(2, 2), 1)
    #     self.assertEqual(self.calculator.result, 1)
    #
    # def test_square_method_calculator(self):
    #     self.assertEqual(self.calculator.square(3), 9)
    #     self.assertEqual(self.calculator.result, 9)
    #
    # def test_squareroot_method_calculator(self):
    #     self.assertEqual(self.calculator.squareroot(9), 3)
    #     self.assertEqual(self.calculator.result, 3)


if __name__ == '__main__':
    unittest.main()
