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

        # Diccionario para elementos repetidos.
        reps_dict = dict()
        for num in nums:
            if num in reps_dict:
                reps_dict[num] += 1
            else:
                reps_dict[num] = 1
        
        for num, reps in reps_dict.items():
            if reps > 1:
                # Lista de índices donde aparece cada elemento repetido.
                indexes_in_nums = []
                for index, n in enumerate(nums):
                    if n == num:
                        indexes_in_nums.append(index)
                
                # Pruebo a combinar los diferentes índices de apariciones.
                for _ in range(0, len(indexes_in_nums)):
                    if indexes_in_nums[_] == indexes_in_nums[-1]:
                        continue
                    if abs(indexes_in_nums[_] - indexes_in_nums[_ + 1]) == k:
                        return True
                    else:
                        continue
            else:
                continue
        return False    


        