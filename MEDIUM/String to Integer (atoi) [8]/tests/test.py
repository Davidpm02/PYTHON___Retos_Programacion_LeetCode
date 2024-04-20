import unittest
from ..scripts.code import *

class TestMyAtoi(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_positive_number_with_whitespace(self):
        self.assertEqual(self.solution.myAtoi("   42"), 42)
        
    def test_negative_number_with_whitespace(self):
        self.assertEqual(self.solution.myAtoi("   -42"), -42)
        
    def test_number_with_plus_sign(self):
        self.assertEqual(self.solution.myAtoi("+42"), 42)
        
    def test_number_with_minus_sign(self):
        self.assertEqual(self.solution.myAtoi("-42"), -42)
        
    def test_number_with_leading_zeros(self):
        self.assertEqual(self.solution.myAtoi("00042"), 42)
        
    def test_number_exceeding_upper_limit(self):
        self.assertEqual(self.solution.myAtoi("2147483648"), 2147483647)
        
    def test_number_below_lower_limit(self):
        self.assertEqual(self.solution.myAtoi("-2147483649"), -2147483648)
        
    def test_empty_string(self):
        self.assertEqual(self.solution.myAtoi(""), 0)
        
    def test_string_with_no_numerical_characters(self):
        self.assertEqual(self.solution.myAtoi("abc"), 0)

if __name__ == '__main__':
    unittest.main()