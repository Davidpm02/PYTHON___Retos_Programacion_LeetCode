import unittest
from typing import *
from ..scripts.code import *

class TestRemoveElement(unittest.TestCase):
    def test_remove_single_element(self):
        sol = Solution()
        nums = [3, 2, 2, 3]
        val = 3
        expected_output = 2
        self.assertEqual(sol.removeElement(nums, val), expected_output)
        self.assertListEqual(nums[:expected_output], [2, 2])

    def test_remove_all_elements(self):
        sol = Solution()
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_output = 5
        self.assertEqual(sol.removeElement(nums, val), expected_output)
        self.assertListEqual(nums[:expected_output], [0, 1, 4, 0, 3])

    def test_remove_no_elements(self):
        sol = Solution()
        nums = [0, 1, 2, 3, 4]
        val = 5
        expected_output = 5
        self.assertEqual(sol.removeElement(nums, val), expected_output)
        self.assertListEqual(nums, nums[:expected_output])

if __name__ == '__main__':
    unittest.main()