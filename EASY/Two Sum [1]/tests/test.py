import unittest
from ..scripts.code import *

class TestTwoSum(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(sol.twoSum(nums, target), [0, 1])

    def test_case_2(self):
        sol = Solution()
        nums = [3, 3, 4, 5]
        target = 6
        self.assertEqual(sol.twoSum(nums, target), [0, 1])

    def test_case_3(self):
        sol = Solution()
        nums = [1, 2, 3, 4]
        target = 10
        self.assertEqual(sol.twoSum(nums, target), [-1, -1])

if __name__ == '__main__':
    unittest.main()