import unittest
from ..scripts.code import *

class TestLongestCommonPrefix(unittest.TestCase):
    def test_empty_list(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix([]), "")
        
    def test_no_common_prefix(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["dog", "racecar", "car"]), "")
        
    def test_common_prefix(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        
    def test_longest_common_prefix(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["ab", "a"]), "a")
        
    def test_no_strings(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix([]), "")
        
if __name__ == "__main__":
    unittest.main()