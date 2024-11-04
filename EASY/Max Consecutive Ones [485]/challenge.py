"""
DESCRIPTION:

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

  Input: nums = [1,1,0,1,1,1]
  Output: 3
  Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

  Input: nums = [1,0,1,1,0,1]
  Output: 2

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.

"""

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de hallar la 
            cantidad máximas de unos en un array dado.
        Args:
            nums (List[int])
        Returns:
            int -- Cantidad máxima de unos consecutivos dentro
            del array 'nums'.
        """

        # Defino una lista que funcione como contador de los elementos consecutivos
        rep_consecutive_elements_array = []

        if 1 not in nums:
            return 0
        
        consecutives_ones = 0
        for num in nums:
            if num == 0:
                if consecutives_ones > 0:
                    rep_consecutive_elements_array.append(consecutives_ones)
                    consecutives_ones = 0
                continue
            else:
                consecutives_ones += 1
                continue
        if consecutives_ones > 0:
            rep_consecutive_elements_array.append(consecutives_ones)
            consecutives_ones = 0
        
        return max(rep_consecutive_elements_array)