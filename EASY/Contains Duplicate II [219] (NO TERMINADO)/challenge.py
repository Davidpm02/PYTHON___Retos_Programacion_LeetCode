"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

  Input: nums = [1,2,3,1], k = 3
  Output: true

Example 2:

  Input: nums = [1,0,1,1], k = 1
  Output: true

Example 3:

  Input: nums = [1,2,3,1,2,3], k = 2
  Output: false

 

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105

"""

from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        """
        Summary:
            Método de la clase Solution encargado de averiguar si existen
            duplicados dentro de 'num' cuya distancia entre sí sea igual o
            menor que 'k'.
        Args:
            nums (List[int]) -- Lista de enteros a procesar.
            k (int) -- Distancia máxima permitida.
        Returns:
            bool
        """

        # Array para elementos repetidos
        reps_array = []

        # Inicializo una clase contador
        counter = Counter(nums)
        for count in counter.most_common():
            if count[-1] > 1:
                reps_array.append(count[0])
        
        # Recorro reps_array en busca de alguna coincidencia
        # que cumpla la condición del enunciado
        for num in reps_array:
            indexes_num_reps = []
            for index, value in nums:
                if num == value:
                    indexes_num_reps.append(index)
            for idx in indexes_num_reps:  # DEMASIADOS BUCLES FOR
                pass
        