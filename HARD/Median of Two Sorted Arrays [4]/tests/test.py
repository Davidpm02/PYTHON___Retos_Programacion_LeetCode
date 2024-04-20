import unittest
from ..scripts.code import *

class TestFindMedianSortedArrays(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
        
    def test_empty_arrays(self):
        nums1 = []
        nums2 = []
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 0.0)
        
    def test_one_empty_array(self):
        nums1 = [1, 2, 3]
        nums2 = []
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.0)
        
    def test_one_element_arrays(self):
        nums1 = [5]
        nums2 = [3]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 4.0)
        
    def test_multiple_elements_arrays(self):
        nums1 = [1, 3, 5]
        nums2 = [2, 4, 6]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 3.5)

if __name__ == '__main__':
    unittest.main()