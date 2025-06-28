"""
DESCRIPTION:

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 10^5
1 <= k <= nums.length

"""

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Paso 1: Asocio cada número con su índice original
        indexed_nums = list(enumerate(nums))
        
        # Paso 2: Selecciono los k elementos con mayor valor
        # Lo hago ordenando por valor, de mayor a menor, y tomando los primeros k
        k_largest = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        
        # Paso 3: Reordeno los elementos seleccionados según su índice original
        k_largest.sort(key=lambda x: x[0])
        
        # Paso 4: Extraigo los valores, en el orden original
        return [num for idx, num in k_largest]
        