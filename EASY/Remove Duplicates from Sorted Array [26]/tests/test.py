import unittest
from ..scripts.code import *

class TestRemoveDuplicates(unittest.TestCase):
    
    def test_no_duplicates(self):
        sol = Solution()
        nums = [1, 2, 3]
        expected = 3
        self.assertEqual(sol.removeDuplicates(nums), expected)
        
    def test_all_duplicates(self):
        sol = Solution()
        nums = [1, 1, 1]
        expected = 1
        self.assertEqual(sol.removeDuplicates(nums), expected)
        
    def test_empty_list(self):
        sol = Solution()
        nums = []
        expected = 0
        self.assertEqual(sol.removeDuplicates(nums), expected)

if __name__ == '__main__':
    unittest.main()