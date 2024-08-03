"""
DESCRIPTION

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

  Input: nums = [1,3,5,6], target = 5
  Output: 2

Example 2:

  Input: nums = [1,3,5,6], target = 2
  Output: 1

Example 3:

  Input: nums = [1,3,5,6], target = 7
  Output: 4

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104


"""

from collections import OrderedDict
from typing import *

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        """
            Summary:
                Método de la clase Solution encargado de consultar el índice que ocupa un determinado entero
                dentro de la lista recibida como parámetro. En caso de que el entero no se encuentre dentro 
                de la lista, la función retorna el índice que este debería ocupar en caso de ser insertado.
            
            Args:
                nums -- Array con una serie de enteros registrados.
                target -- Entero cuyo índice deseamos obtener.
            
            Returns:
                index -- índice que ocupa el entero 'target' dentro del array de enteros 'nums'.
        """

        try:
            # Me aseguro de que target se encuentre dentro de nums
            index = nums.index(target)
            return index
        except ValueError:
            # Defino un diccionario que mapee cada uno de los valores en nums
            nums_dict = dict()
            for index, num in enumerate(nums):
                nums_dict[num] = index

            # Defino una lista con todas las claves del diccionario, más el 'target'
            nums_ = nums[:]
            nums_.append(target)
            nums_ = sorted(nums_)

            for index, num in enumerate(nums_):
                if num not in nums_dict:
                    nums_dict[num] = index

            # Ordeno las claves del diccionario
            od = OrderedDict(sorted(nums_dict.items()))
            return od[target]

if __name__ == "__main__":
    
    # Ejemplo de interacción con el método '.searchInsert()'
    nums = [1,3,5,6]
    target = 5
    
    sol = Solution()
    index = sol.searchInsert(nums, target)
    
