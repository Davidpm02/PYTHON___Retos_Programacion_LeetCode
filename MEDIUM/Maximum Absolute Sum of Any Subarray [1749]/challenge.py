"""
DESCRIPTION:

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.

 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

"""

from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        """
        Se encarga de hallar la máxima suma (en valor absoluto) 
        de cualquier subarray que pueda obtenerse a partir del
        array 'nums' recibido como parámetro.

        params:
            nums (List[int])
        
        returns:
            int
        """

        # Variables de referencia inicializadas a 0
        max_sum = 0
        min_sum = 0
        actual_max_sum = 0
        actual_min_sum = 0

        # Itero sobre la lista de números actualizando las referencias
        for num in nums:
            actual_max_sum = max(num, actual_max_sum + num)
            max_sum = max(max_sum, actual_max_sum)

            actual_min_sum = min(num, actual_min_sum + num)
            min_sum = min(min_sum, actual_min_sum)

        return max(max_sum, abs(min_sum))