"""
DESCRIPTION:

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

  Input: nums = [2,2,3,2]
  Output: 3

Example 2:

  Input: nums = [0,1,0,1,0,1,99]
  Output: 99

 

Constraints:

    1 <= nums.length <= 3 * 104
    -231 <= nums[i] <= 231 - 1
    Each element in nums appears exactly three times except for one element which appears once.

"""

from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        """
            Summary:
                Método de la clase Solution encargado de obtener el 
                elemento único de un array dado.
                La función procesa un array de enteros triplicados y 
                retorna aquel con una única aparición.
            Args:
                nums (list) -- Array de enteros.
            Returns:
                int (int) -- Entero con una única aparición dentro
                             de 'nums'.
        """

        nums_count_counter = Counter(nums)
        return nums_count_counter.most_common()[-1][0]