"""
DESCRIPTION:

You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.

 

Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.

 

Constraints:

    1 <= nums1.length, nums2.length <= 105
    0 <= nums1[i], nums2[j] <= 109

"""

from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        Se encarga de obtener el resultado de aplicar XOR a los resultados 
        de aplicar XOR en todas las parejas de enteros entre nums1 y nums2.

        params:
            nums1 (List[int])
            nums2 (List[int])
        
        returns:
            int
        """

        # Número máximo de bits en un entero
        max_bits = 32
        result = 0
        
        # Para cada bit
        for bit in range(max_bits):
            # Números en nums1 y nums2 que tienen bits fijados
            count1 = sum((num >> bit) & 1 for num in nums1)
            count2 = sum((num >> bit) & 1 for num in nums2)
            
            # Si hay un número de nums1 con este bit en 1 y un número de nums2 con este bit en 0,
            # o viceversa, el bit en el resultado debe ser 1.
            if (count1 * len(nums2) + count2 * len(nums1)) % 2 != 0:
                result |= (1 << bit)
        
        return result