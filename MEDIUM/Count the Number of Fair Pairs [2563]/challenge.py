"""
DESCRIPTION:

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 10^5
nums.length == n
-109 <= nums[i] <= 10^9
-109 <= lower <= upper <= 10^9

"""

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Esta función devuelve el número de pares válidos (i, j)
        tales que 0 <= i < j < n y lower <= nums[i] + nums[j] <= upper.
        
        params:
            nums (List[int])
            lower (int)
            upper (int)
        
        returns:
            int
        """
        # Ordeno los números para poder usar búsqueda binaria
        nums.sort()
        n = len(nums)
        count = 0

        # Itero cada índice i y busco los j > i válidos usando bisect
        for i in range(n):
            # Calculo los límites de búsqueda para nums[j]
            left = lower - nums[i]
            right = upper - nums[i]

            # Encuentro los índices de los posibles j usando bisect
            left_idx = bisect_left(nums, left, i + 1)
            right_idx = bisect_right(nums, right, i + 1)

            # Acumulo la cantidad de pares válidos con nums[i]
            count += right_idx - left_idx

        return count