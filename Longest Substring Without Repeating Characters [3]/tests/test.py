import unittest
from ..scripts.code import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Solution.lengthOfLongestSubstring("", 0))

    def test_all_unique_characters(self):
        self.assertEqual(Solution.lengthOfLongestSubstring("abcde", 5))
    
    def test_all_repeating_characters(self):
        self.assertEqual(Solution.lengthOfLongestSubstring("aaaaa", 1))

    def test_mix_unique_and_repeating_characters(self):
        self.assertEqual(Solution.lengthOfLongestSubstring("abcabcbb", 3))

if __name__ == '__main__':
    
    
    unittest.main()