import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        CsvReader.data = []

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

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

    def test_multiplication(self):
        test_data = CsvReader('/src/csv/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('/src/csv/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square(self):
        test_data = CsvReader('/src/csv/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squareroot(self):
        test_data = CsvReader('/src/csv/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squareroot(row['Value 1']), round(float(row['Result']),8))
            self.assertEqual(self.calculator.result, round(float(row['Result']),8))

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

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
