import unittest
from ..scripts.code import *

class TestConvert(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(Solution().convert("", 0), "")
        self.assertEqual(Solution().convert("", 1), "")
        self.assertEqual(Solution().convert("", 2), "")

    def test_single_row(self):
        self.assertEqual(Solution().convert("A", 1), "A")
        self.assertEqual(Solution().convert("AB", 1), "AB")
        self.assertEqual(Solution().convert("ABC", 1), "ABC")

    def test_two_rows(self):
        self.assertEqual(Solution().convert("A", 2), "A")
        self.assertEqual(Solution().convert("AB", 2), "AB")
        self.assertEqual(Solution().convert("ABC", 2), "ACB")
        self.assertEqual(Solution().convert("ABCD", 2), "ADCB")

    def test_three_rows(self):
        self.assertEqual(Solution().convert("A", 3), "A")
        self.assertEqual(Solution().convert("AB", 3), "AB")
        self.assertEqual(Solution().convert("ABC", 3), "ACB")
        self.assertEqual(Solution().convert("ABCD", 3), "ADCB")
        self.assertEqual(Solution().convert("ABCDEF", 3), "ADGFBCE")

    def test_longer_strings(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(Solution().convert("A", 1000), "A")

if __name__ == '__main__':
    unittest.main()