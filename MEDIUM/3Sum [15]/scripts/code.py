"""
DESCRIPTION:

## TODO ==> Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]
  Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.


Example 2:

  Input: nums = [0,1,1]
  Output: []
  Explanation: The only possible triplet does not sum up to 0.


Example 3:

  Input: nums = [0,0,0]
  Output: [[0,0,0]]
  Explanation: The only possible triplet sums up to 0.
 

## Constraints:

  3 <= nums.length <= 3000
  -105 <= nums[i] <= 105

"""
from collections import Counter
from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Método de la clase Solution encargado de recibir una lista de enteros, y retornar una lista con aquellos enteros
           que cumplen la condición del problema (los enteros son diferentes entre sí, y la suma de todos es igual a 0).
           
           Args:
               nums -- Array de números enteros a procesar por la función.
           
           Returns:
               list -- Lista de enteros que cumplen la condición del enunciado.
        """
        
        if len(nums) < 3:
          return []
        
        # Comienzo ordenando el array recibido
        nums.sort()
        
        
        # Mapeo cada elemento con el conteo de apariciones; si aparece más de 3 veces, me quedo solo con 3 repeticiones.
        num_count_dict = Counter(nums)
        nums_ = []
        for key, value in num_count_dict.items():
          if value > 3:
            for _ in range(3):
              nums_.append(key)
          else:
            for _ in range(value):
              nums_.append(key)

        # Inicializo una referencia al conjunto de tripletes
        triplet_set = set()
                
        # Itero sobre la lista de numeros recibida
        for index, num in enumerate(nums_):
          
          index_left_pointer = index+1
          index_right_pointer = len(nums_)-1
          
          
          # A continuación, aplico una estrategia basada en dos punteros
          for _ in nums_[index+1:]:
            
            if index_left_pointer >= index_right_pointer:
              break
            
            left_pointer = nums_[index_left_pointer]
            right_pointer = nums_[index_right_pointer]
            
            
            nums_sum = (num + left_pointer + right_pointer)
            if nums_sum == 0:
              # Hemos encontrado un triplete válido
              triplet = sorted([num, left_pointer, right_pointer])
              triplet_set.add(tuple(triplet))
            
              
              # Ajusto ambos punteros
              index_left_pointer +=1
              index_right_pointer -=1
              continue
              
            elif nums_sum < 0:
              index_left_pointer +=1
              continue
            elif nums_sum > 0:
              index_right_pointer -=1
              continue
        
        threeSum_array = [list(triplet) for triplet in triplet_set]
        return threeSum_array
            
            
        
        

if __name__ == "__main__":
  
  nums = [-1,0,1,2,-1,-4]
  solution = Solution()
  sol = solution.threeSum(nums=nums)
  print(sol)

        