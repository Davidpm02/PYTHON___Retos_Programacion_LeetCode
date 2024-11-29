"""
DESCRIPTION:

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

  Input: nums = [1,12,-5,-6,50,3], k = 4
  Output: 12.75000
  Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

  Input: nums = [5], k = 1
  Output: 5.00000

 

Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104

"""

from functools import reduce
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        """
        Halla el conjunto de números del parámetro 'nums' con longitud
        'k' cuya media es la máxima de todos los posibles conjuntos de
        'k' elementos de 'nums'.

        params:
            nums (List[int])
            k (int)
        
        returns:
            float
        """

        # Defino una lista que contendrá todas las medias calculadas
        averages_array = []

        # Recorro la lista 'nums' y tomo los primeros 'k' elementos consecuentes
        for idx, num in enumerate(nums):
            try:
                idx_num = nums.index(num)
                subsequence_nums = nums[idx_num: idx_num + k]
                assert (len(subsequence_nums) == k)
                averages_array.append(float((reduce((lambda x, y: x + y), subsequence_nums) / k)))
            except AssertionError:
                break
        return max(averages_array)