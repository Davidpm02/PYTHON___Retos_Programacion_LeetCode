"""
DESCRIPTION:

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

  Input: nums = [1,3,5,4,7]
  Output: 3
  Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
   Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
   4.

Example 2:

  Input: nums = [2,2,2,2,2]
  Output: 1
  Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
   increasing.

 

Constraints:

    1 <= nums.length <= 104
    -109 <= nums[i] <= 109

"""

from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        """
        Halla la longitud del subconjunto mayor de enteros ascendentes
        contecutivos dentro de la lista 'nums'.
        
        params:
            nums (List[int])
        
        returns:
            int -- Longitud del subconjunto mayor de enteros ascendentes
            en 'nums'.
        """

        longest_ascendent_subsequences = []
        while True:
            length_subsequence = 0
            for idx, num in enumerate(nums):
                print('Número actual en iteración -->', num)
                if (idx == 0):
                    length_subsequence += 1
                    continue
                
                if (num > nums[idx - 1]):
                    length_subsequence += 1
                else:
                    longest_ascendent_subsequences.append(length_subsequence)
                    length_subsequence = 1  # Reinicio de la longitud
            
            longest_ascendent_subsequences.append(length_subsequence)
            break
        return max(longest_ascendent_subsequences)