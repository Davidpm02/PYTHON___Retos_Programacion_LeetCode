import unittest
from ..scripts.code import *

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(1), "I")

    def test_10(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(10), "X")

    def test_58(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(58), "LVIII")

    def test_1994(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(1994), "MCMXCIV")

    def test_3999(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()