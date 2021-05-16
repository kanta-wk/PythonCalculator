import os
import sys
import unittest
sys.path.append(os.path.abspath(".."))

from src.Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    LEFT_VALUE = 4564
    RIGHT_VALUE = 349

    def setUp(self) -> None:
        self.create_calculator(self.LEFT_VALUE)
        self.calculator.right_value = self.RIGHT_VALUE


    def tearDown(self) -> None:
        pass

    def create_calculator(self, left_value):
        self.calculator = Calculator(left_value)

    @unittest.skip("write the code")
    def test_add(self):
        self.calculator.operator#TODO 加算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE + self.RIGHT_VALUE)

    @unittest.skip("write the code")
    def test_sub(self):
        self.calculator.operator#TODO 減算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE - self.RIGHT_VALUE)

    @unittest.skip("write the code")
    def test_multi(self):
        self.calculator.operator#TODO かけ算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE * self.RIGHT_VALUE)

    @unittest.skip("write the code")
    def test_divi(self):
        self.calculator.operator#TODO 割り算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE / self.RIGHT_VALUE)

    @unittest.skip("write the code")
    def test_formula_add(self):
        self.test_add()
        self.assertEqual(self.calculator.formula, "{}+{}".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    @unittest.skip("write the code")
    def test_formula_sub(self):
        self.test_sub()
        self.assertEqual(self.calculator.formula, "{}-{}".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    @unittest.skip("write the code")
    def test_formula_multi(self):
        self.test_multi()
        self.assertEqual(self.calculator.formula, "{}×{}".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    @unittest.skip("write the code")
    def test_formula_divi(self):
        self.test_divi()
        self.assertEqual(self.calculator.formula, "{}÷{}".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    @unittest.skip("write the code")
    def test_left_value(self):
        self.assertEqual(self.calculator.left_value, self.LEFT_VALUE)

    @unittest.skip("write the code")
    def test_right_value(self):
        self.calculator.right_value = self.RIGHT_VALUE
        self.assertEqual(self.calculator.right_value, self.RIGHT_VALUE)


if __name__ == '__main__':
    unittest.main()
