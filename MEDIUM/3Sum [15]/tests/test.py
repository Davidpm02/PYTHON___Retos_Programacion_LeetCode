import unittest
from collections import Counter
from typing import *
from ..scripts.code import *

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.threeSum([]), [])

    def test_single_element_list(self):
        self.assertEqual(self.solution.threeSum([0]), [])

    def test_two_element_list(self):
        self.assertEqual(self.solution.threeSum([0, 0]), [])

    def test_list_with_positive_numbers(self):
        self.assertEqual(self.solution.threeSum([1, 2, 3]), [])

    def test_list_with_negative_numbers(self):
        self.assertEqual(self.solution.threeSum([-1, -2, -3]), [])

    def test_list_with_zero_sum_triplets(self):
        self.assertEqual(self.solution.threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_list_with_multiple_zero_sum_triplets(self):
        self.assertEqual(self.solution.threeSum([0, 0, 0, 0, 0]), [[0, 0, 0], [0, 0, 0]])

    def test_list_with_positive_and_negative_numbers(self):
        self.assertEqual(self.solution.threeSum([-1, 0, 1, 2, -1]), [[-1, -1, 2], [-1, 0, 1]])

    def test_list_with_duplicate_numbers(self):
        self.assertEqual(self.solution.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 5]), [[-4, -2, 2], [-4, 0, 4], [-2, -2, 2], [-2, 0, 2]])

if __name__ == '__main__':
    unittest.main()