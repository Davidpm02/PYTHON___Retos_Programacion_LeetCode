"""
DESCRIPTION:

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i], k <= 10^9

"""

from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        """
        Se encarga de contar el número de subarrays dentro de 'nums'
        que tienen, al menos, 'k' pares de índices (i, j) tales que
        i < j y arr[i] == arr[j].

        params:
            nums (List[int])
            k (int)

        returns:
            int
        """

        freq = defaultdict(int)
        n = len(nums)
        left = 0  # Límite izquierdo de la ventana
        total_pairs = 0  # Cantidad de pares dentro de la ventana
        result = 0  # Acumulador de subarrays buenos

        # Recorro el array con el extremo derecho de la ventana
        for right in range(n):
            num = nums[right]
            # Cada vez que agrego un número, contribuye con freq[num] pares adicionales
            total_pairs += freq[num]
            freq[num] += 1

            # Mientras la ventana sea válida (pares >= k), intento acortarla por la izquierda
            while total_pairs >= k:
                # Como tengo al menos k pares, todos los subarrays desde left hasta el final son válidos
                result += n - right

                # Quito nums[left] de la ventana, ajustando los pares
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]
                left += 1

        return result