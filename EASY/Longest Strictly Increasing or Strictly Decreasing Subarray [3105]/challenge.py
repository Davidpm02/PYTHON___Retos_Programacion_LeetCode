"""
DESCRIPTION:

You are given an array of integers nums. Return the length of the longest
subarray
of nums which is either
strictly increasing
or
strictly decreasing
.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

 

Constraints:

    1 <= nums.length <= 50
    1 <= nums[i] <= 50

"""

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        """
        Se encarga de verificar la longitud máxima de cualquier
        subcadena de 'nums' cuyos elementos estén en orden 
        ascendente o descendente.
        
        params:
            nums (List[int])
        
        returns:
            int
        """

        # Lógica para búsqueda de subarrays crecientes.
        increasing_subarrays = []
        last_subarray = []
        for idx, num in enumerate(nums):
            if (idx == 0):
                last_subarray.append(num)
            else:
                if (num > nums[idx - 1]):
                    last_subarray.append(num)
                else:
                    increasing_subarrays.append(last_subarray)
                    last_subarray = [num]
        increasing_subarrays.append(last_subarray)


        # Lógica para búsqueda de subarrays decrecientes.
        decreasing_subarrays = []
        last_subarray = []
        for idx, num in enumerate(nums):
            if (idx == 0):
                last_subarray.append(num)
            else:
                if (num < nums[idx - 1]):
                    last_subarray.append(num)
                else:
                    decreasing_subarrays.append(last_subarray)
                    last_subarray = [num]
        decreasing_subarrays.append(last_subarray)

        # Listas con las longitudes de cada subcadena.
        lengths_increasing_subarrays = [len(subarray) for subarray in increasing_subarrays]
        lengths_decreasing_subarrays = [len(subarray) for subarray in decreasing_subarrays]

        # Retorno la máxima longitud de entre ambos tipos de subcadenas.
        return max([max(lengths_increasing_subarrays), max(lengths_decreasing_subarrays)])