"""
DESCRIPTION:

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

  Input: nums = [3,0,1]
  Output: 2
  Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

  Input: nums = [0,1]
  Output: 2
  Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

  Input: nums = [9,6,4,2,3,5,7,0,1]
  Output: 8
  Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

 

Constraints:

    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.

"""
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de comprobar el
            entero ausente dentro de una lista recibida como 
            parámetro.
            El método toma en consideración el número de enteros
            presente dentro de 'nums' para definir un rango [0, n],
            y retornar el único entero de 'nums' ausente en este
            rango.
        Args:
            nums (List[int]) -- Lista a evaluar por el método.
        Returns:
            int -- Entero ausente (dentro del rango [n, len(nums)])
        """

        n = len(nums)
        for _ in range(n + 1):
            if _ not in nums:
                return _