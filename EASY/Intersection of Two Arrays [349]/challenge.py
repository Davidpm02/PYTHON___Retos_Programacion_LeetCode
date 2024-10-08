"""
DESCRIPTION:

Given two integer arrays nums1 and nums2, return an array of their
intersection.
Each element in the result must be unique and you may return the result in any order.

 

Example 1:

  Input: nums1 = [1,2,2,1], nums2 = [2,2]
  Output: [2]

Example 2:

  Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
  Output: [9,4]
  Explanation: [4,9] is also accepted.

 

Constraints:

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

"""
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        """
        Summary:
            Método de la clase Solution encargado de hallar la
            intersección de dos arrays.
            Una vez se haya esta intersección, el método la 
            retorna en forma de lista.
        Args:
            nums1 (List[int]) -- Primer array.
            nums2 (List[int]) -- Segundo array.
        Returns:
            List[int]
        """

        return set(num for num in nums1 if num in nums2)