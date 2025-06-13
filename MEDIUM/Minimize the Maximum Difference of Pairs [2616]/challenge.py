"""
DESCRIPTION:

You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 109
0 <= p <= (nums.length)/2

"""

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        # Primero ordeno el array para facilitar emparejar valores cercanos
        nums.sort()

        # Esta función auxiliar me dice si puedo formar al menos 'p' pares
        # con diferencia máxima menor o igual a 'max_diff'
        def can_form_pairs(max_diff: int) -> bool:
            count = 0
            i = 1
            while i < len(nums):
                # Si la diferencia del par actual es válida, lo tomo y salto 2
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2
                else:
                    # Si no, solo avanzo uno
                    i += 1
                if count >= p:
                    return True
            return count >= p

        # Búsqueda binaria sobre la diferencia máxima
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid  # Intento minimizar más
            else:
                left = mid + 1  # Necesito permitir mayor diferencia

        return left
