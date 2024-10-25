"""
DESCRIPTION:

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

  Input: nums = [4,3,2,7,8,2,3,1]
  Output: [5,6]

Example 2:

  Input: nums = [1,1]
  Output: [2]

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

"""

from typing import List
from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        """
        Summary:
            Método de la clase Solution encargado de hallar todos los
            números faltantes en 'nums', cuyo valor se encuentra dentro
            del rango [1, n].
        Args:
            nums (List[int]) -- Array de enteros a evaluar.
        Returns:
            List[int] -- Array de todos los números ausentes en 'nums'.
        """
        
        nums_counter = Counter(nums)
        return [num for num in range(1, len(nums) + 1) if num not in nums_counter.keys()]
