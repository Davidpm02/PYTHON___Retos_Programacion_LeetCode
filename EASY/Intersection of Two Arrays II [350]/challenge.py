"""
DESCRIPTION:

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

  Input: nums1 = [1,2,2,1], nums2 = [2,2]
  Output: [2,2]

Example 2:

  Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
  Output: [4,9]
  Explanation: [9,4] is also accepted.

 

Constraints:

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

"""

from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
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

        # Defino un contador con las repeticiones de cada entero
        # en ambos parámetros
        counter = Counter(nums1)
        counter.update(nums2)

        # Contadores independientes    
        counter_nums1 = Counter(nums1)
        counter_nums2 = Counter(nums2)

        result = []
        for key, value in counter.items():

            times_in_array1 = counter_nums1[key]
            times_in_array2 = counter_nums2[key]

            if (times_in_array1 == times_in_array2):
                for _ in range(times_in_array1):
                    result.append(key)
            else:
                min_reps_in_nums = min([times_in_array1, times_in_array2])
                for _ in range(min_reps_in_nums):
                    result.append(key)
        return result
