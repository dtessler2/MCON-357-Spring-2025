import unittest
import sys
from exercises.calculate_factorial import factorial_recursive, process_input

class test_factorial(unittest.TestCase):

    def test_0_factorial(self):
        self.assertEqual(factorial_recursive(0), 1)

    def test_1_factorial(self):
        self.assertEqual(factorial_recursive(1), 1)

    def test_positive(self):
        self.assertEqual(factorial_recursive(5), 120)

    def test_large_num(self):
        self.assertEqual(factorial_recursive(15), 1307674368000)

    def test_negative(self):
        value, error_message = process_input("-7")
        self.assertNone(value)
        self.assertEqual(error_message, "Number cannot be negative")

    def test_fraction(self):
        value, error_message = process_input("3.25")
        self.assertNone(value)
        self.assertEqual(error_message, "Number must be an integer")







    
        

    