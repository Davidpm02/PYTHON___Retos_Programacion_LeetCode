import unittest
from ..scripts.code import *

class TestRomanToInt(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
        
    def test_single_numeral_character(self):
        self.assertEqual(self.solution.romanToInt("I"), 1)
        
    def test_combination_numerals(self):
        self.assertEqual(self.solution.romanToInt("XXIV"), 24)
        
    def test_maximum_valid_numeral(self):
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)
        
    def test_empty_string_input(self):
        self.assertEqual(self.solution.romanToInt(""), 0)
        
    def test_invalid_numerals(self):
        # Testing with an invalid character 'Z'
        self.assertEqual(self.solution.romanToInt("IZ"), 1)  # It should ignore 'Z' and consider only 'I'
        
if __name__ == '__main__':
    unittest.main()