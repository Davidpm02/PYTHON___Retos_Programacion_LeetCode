import unittest
from ..scripts.code import Solution

class TestReverseFunction(unittest.TestCase):
  
    def test_positive_input_within_32_bit_int_range(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)

    def test_negative_input_within_32_bit_int_range(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-123), -321)
    
    def test_zero_input(self):
        solution = Solution()
        self.assertEqual(solution.reverse(0), 0)

    def test_positive_input_outside_32_bit_int_range(self):
        solution = Solution()
        self.assertEqual(solution.reverse(1534236469), 0)

    def test_negative_input_outside_32_bit_int_range(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-1534236469), 0)