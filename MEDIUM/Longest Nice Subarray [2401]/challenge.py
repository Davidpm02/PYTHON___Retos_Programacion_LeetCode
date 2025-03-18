"""
DESCRIPTION:

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

 

Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109

"""

from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        """
        Se encarga de hallar el subarray de mayor longitud dentro del
        array 'nums', cumpliendo las condiciones del enunciado.

        params:
            nums (List[int])
        
        returns:
            int
        """

        bit_mask = 0  # Máscara de bits para verificar el AND bit a bit
        left = 0  # Puntero izquierdo de la ventana
        max_length = 0  # Longitud máxima del subarray nice
        
        for right in range(len(nums)):
            # Mientras el número actual no cumpla la condición AND == 0
            while (bit_mask & nums[right]) != 0:
                bit_mask ^= nums[left]  # Eliminar el efecto de nums[left] de la máscara
                left += 1  # Mover el puntero izquierdo para reducir la ventana
            
            # Incluir nums[right] en la ventana actual
            bit_mask |= nums[right]
            
            # Calcular la longitud de la ventana actual
            max_length = max(max_length, right - left + 1)
        
        return max_length