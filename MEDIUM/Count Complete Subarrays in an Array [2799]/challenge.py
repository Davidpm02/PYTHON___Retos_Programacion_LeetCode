"""
DESCRIPTION:

You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

 

Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2000

"""

from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        """
        Se encarga de hallar el número de subarrays completos que podemos
        obtener a partir de un array 'nums' predefinido.

        Se considera un subarray completo aquel cuyo número de elementos 
        diferentes es igual al número de elementos diferentes de todo
        el array de partida.

        params:
            nums (List[int])

        returns:
            int
        """
        
        # Número de elementos distintos en el array completo
        total_distinct = len(set(nums))
        n = len(nums)
        result = 0
        
        # Para cada posible inicio de subarray
        for start in range(n):
            # Conjunto para rastrear elementos distintos en el subarray actual
            distinct_elements = set()
            
            # Expandimos el subarray
            for end in range(start, n):
                distinct_elements.add(nums[end])
                
                # Si el subarray actual tiene todos los elementos distintos
                if len(distinct_elements) == total_distinct:
                    # Todos los subarray que comienzan en 'start' y terminan en o después de 'end'
                    # son completos
                    result += n - end
                    break
        
        return result