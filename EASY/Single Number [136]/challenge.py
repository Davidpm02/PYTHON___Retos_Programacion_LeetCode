"""
DESCRIPTION:

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

  Input: nums = [2,2,1]
  Output: 1

Example 2:

  Input: nums = [4,1,2,1,2]
  Output: 4

Example 3:

  Input: nums = [1]
  Output: 1

 

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

"""

from collections import Counter
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        """
            Summary:
                Método de la clase Solution encargado de obtener el 
                elemento único de un array dado.
                La función procesa un array de enteros duplicados y 
                retorna aquel con una única aparición.
            Args:
                nums (list) -- Array de enteros.
            Returns:
                int (int) -- Entero con una única aparición dentro
                             de 'nums'.
        """

        # Instancio un contador con las apariciones de cada elemento
        # en 'nums'.
        nums_count_counter = Counter(nums)
        return nums_count_counter.most_common()[-1][0]