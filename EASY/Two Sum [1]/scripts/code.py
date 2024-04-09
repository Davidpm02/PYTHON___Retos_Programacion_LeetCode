"""
DESCRIPTION:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].



Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]



Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        Summary:
            Función parametrizada encargada de efectuar un procedimiento Two-Sum, para retornar una lista de índices, en 
            función de los valores de los parámetros recibidos.
        
        Args:
            nums -- array de números que la función debe tener en cuenta para generar el array de índices final.
            target -- valor númerico que se espera obtener tras sumar dos números dentro de el parámetro 'nums'.
        
        Returns:
            index-array -> List[int] -- Lista de enteros que representan los índices de los elementos del array 'nums', cuya suma
                                        es igual a 'target'.
                                        
        """
        
        ## LÓGICA 
        first_index_target = 0
        second_index_target = 0
        
        for index_1, num_1 in enumerate(nums):
            
            if second_index_target != 0:
                break
            first_index_target = index_1
            for index_2, num_2 in enumerate(nums):

                if index_1 == index_2:
                    continue
                if num_1 + num_2 == target:

                    second_index_target = index_2
                else:
                    continue
                
        return [first_index_target, second_index_target]
    
    
if __name__ == "__main__":
    
    # Instancio un objeto "Solution"
    solution = Solution()
    
    # Parámetros con los que probar el método ".twoSum()"
    nums = [3,3]
    target = 6
    
    sol = solution.twoSum(nums, target)
    print(sol)
    
    