import unittest
from ..scripts.code import *

class TestLongestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome("racecar"), "racecar")

    def test_substring_palindrome(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome("babad"), "bab")

    def test_no_palindrome(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome("abcd"), "")

    def test_empty_string(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome(""), "")

    def test_single_char(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome("a"), "a")

if __name__ == "__main__":
    unittest.main()