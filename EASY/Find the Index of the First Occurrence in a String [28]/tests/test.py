import unittest
from ..scripts.code import *

class TestStrStr(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_needle_at_beginning(self):
        haystack = "abcdefgh"
        needle = "abc"
        self.assertEqual(self.solution.strStr(haystack, needle), 0)

    def test_needle_at_end(self):
        haystack = "abcdefgh"
        needle = "fgh"
        self.assertEqual(self.solution.strStr(haystack, needle), 5)

    def test_needle_in_middle(self):
        haystack = "abcdefgh"
        needle = "def"
        self.assertEqual(self.solution.strStr(haystack, needle), 3)

    def test_needle_not_present(self):
        haystack = "abcdefgh"
        needle = "xyz"
        self.assertEqual(self.solution.strStr(haystack, needle), -1)

if __name__ == '__main__':
    unittest.main()