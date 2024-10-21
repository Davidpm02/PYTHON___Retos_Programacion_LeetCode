"""
DESCRIPTION:

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

  Input: nums = [3,2,1]
  Output: 1
  Explanation:
   The first distinct maximum is 3.
   The second distinct maximum is 2.
   The third distinct maximum is 1.

Example 2:

  Input: nums = [1,2]
  Output: 2
  Explanation:
   The first distinct maximum is 2.
   The second distinct maximum is 1.
   The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

  Input: nums = [2,2,3,1]
  Output: 1
  Explanation:
   The first distinct maximum is 3.
   The second distinct maximum is 2 (both 2's are counted together since they have the same value).
   The third distinct maximum is 1.

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

"""

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de hallar el tercer
            valor máximo de un array recibido como parámetro.

            En caso de que no exista un tercer valor máximo, el método
            retornará simplemente el máximo valor del array.
        Args:
            nums (List[int]) -- Array de enteros a evaluar.
        Returns:
            int -- Máximo encontrado por el método.
        """

        try:
            nums = set(nums)
            assert len(nums) >= 3

            # Buscamos el tercer máximo de la lista
            max_numbers_on_nums = []
            while len(max_numbers_on_nums) < 3:
                max_on_nums = max(nums)
                max_numbers_on_nums.append(max_on_nums)
                nums.remove(max_on_nums)
            
            # Retornamos el tercer máximo de la lista
            return max_numbers_on_nums[-1]

        except AssertionError:
            return max(nums)