"""
DESCRIPTION:

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

  Input: nums = [0,1,0,3,12]
  Output: [1,3,12,0,0]

Example 2:

  Input: nums = [0]
  Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Summary:
            Método de la clase Solution que se encarga de actualizar
            un array de enteros recibido como parámetro.

            El método detecta los enteros 0 dentro del array, y
            los 'mueve' al final del mismo, manteniendo el orden
            relativo del resto de enteros en nums.
        Args:
            nums (List[int]) -- Array procesado por el método.
        Returns:
            None
        """
        
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)