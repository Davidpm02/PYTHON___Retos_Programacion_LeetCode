"""
DESCRIPTION:

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

  Input: nums = [1,2,2,3,1]
  Output: 2
  Explanation: 
  The input array has a degree of 2 because both elements 1 and 2 appear twice.
  Of the subarrays that have the same degree:
  [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
  The shortest length is 2. So return 2.

Example 2:

  Input: nums = [1,2,2,3,1,4,2]
  Output: 6
  Explanation: 
  The degree is 3 because the element 2 is repeated 3 times.
  So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

 

Constraints:

    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.

"""

from collections import Counter
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        """
        Halla la longitud de la mínima sublista de mayor grado dentro
        de una lista dada.

        params:
            nums(List[int])
        
        returns:
            int
        """

        reps_counter = Counter(nums)
        ordered_reps_counter = reps_counter.most_common()

        max_degree_in_array = ordered_reps_counter[0][-1]

        # Elementos de mayor grado en 'nums'
        higher_degree_integers = { item[0]:[] for item in ordered_reps_counter if (item[-1] == max_degree_in_array)}
        
        # Recorro el diccionario para rellenar la lista de índices
        for key in higher_degree_integers.keys():
            higher_degree_integers[key] = [i for i in range(len(nums)) if nums[i] == key]
        
        # Defino una lista con las diferencias de índices para cada
        # clave del diccionario
        difference_among_indexes = [(value[-1] - value[0]) for key, value in higher_degree_integers.items()]
        return min(difference_among_indexes) + 1