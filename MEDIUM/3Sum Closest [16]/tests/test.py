import unittest
from typing import *
from ..scripts.code import *

class TestThreeSumClosest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 2, 1, -4]
        target = 1
        expected_result = 2
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_example_2(self):
        nums = [0, 0, 0]
        target = 1
        expected_result = 0
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_empty_list(self):
        nums = []
        target = 1
        expected_result = 0
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_list_with_one_element(self):
        nums = [1]
        target = 1
        expected_result = 1
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_list_with_two_elements(self):
        nums = [1, 2]
        target = 1
        expected_result = 3
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_list_with_negative_numbers(self):
        nums = [-1, -2, -3]
        target = -5
        expected_result = -6
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_list_with_large_numbers(self):
        nums = [1000, 2000, 3000]
        target = 5000
        expected_result = 3000
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_list_with_duplicate_numbers(self):
        nums = [1, 1, 1, 1, 1]
        target = 5
        expected_result = 3
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

    def test_list_with_negative_and_positive_numbers(self):
        nums = [-1, 2, -3, 4]
        target = 5
        expected_result = 2
        self.assertEqual(self.solution.threeSumClosest(nums, target), expected_result)

if __name__ == '__main__':
    unittest.main()