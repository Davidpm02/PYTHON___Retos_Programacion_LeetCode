"""
DESCRIPTION:

Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

 

Example 1:

Input: nums = [1,2,4]

Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:

Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

 

Constraints:

2 <= nums.length <= 100
-100 <= nums[i] <= 100

"""

from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        """
        Se encarga de hallar la máxima diferencia absoluta entre los
        elementos adyacentes de un array circular.

        params:
            nums (List[int])
        
        returns:
            int
        """

        # Defino una lista con los resultados
        result_array = []

        # Evaluo primero los extremos
        result_array.append(abs(nums[0] - nums[-1]))

        # Recorro 'nums' y evaluo los elementos adyacentes
        n = len(nums) - 1
        for i in range(0, n):
            result_array.append(abs(nums[i] - nums[i + 1]))
        
        return max(result_array)