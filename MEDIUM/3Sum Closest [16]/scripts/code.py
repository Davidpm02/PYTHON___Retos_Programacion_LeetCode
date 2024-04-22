"""
DESCRIPTION:

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

  Input: nums = [-1,2,1,-4], target = 1
  Output: 2
  Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Example 2:

  Input: nums = [0,0,0], target = 1
  Output: 0
  Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

## Constraints:

  3 <= nums.length <= 500
  -1000 <= nums[i] <= 1000
  -104 <= target <= 104

"""

from typing  import *
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Método de la clase Solution que se encarga de retornar el entero resultado de la suma de tres dígitos del parámetro
           nums, cuyo resultado es igual o más cercano al valor contenido en el parámetro 'target'.
           
           Args:
               nums -- Lista de enteros que la función debe procesar.
               target -- Entero que la función utiliza como referencia para al momento de procesar el parámetro 'nums'
                         y retornar un resultado.
           Returns:
               int -- Entero cuyo valor es igual o más cercano al valor del párametro 'target'.
        """
        
        def closest_num(values, target):
          """Función auxiliar del método 'threeSumClosest' que se encarga de encontrar el valor más cerca al parámetro 'target' que se 
             encuentre dentro del parámetro 'values'.
             
             Args:
                 values -- Lista que contiene las sumas de todos los tripletes posibles, y sobre la que se tiene que obtener un resultado.
                 target -- Entero que la función utiliza como referencia al escoger un número del array 'values'.
             
             Returns:
                 int -- Entero cuyo valor es el más cercano al valor contenido en el parámetro 'target'.
          """

          # Inicializo un diccionario con valores 0
          values_distance_dict = {value:0 for value in values}
          
          # Itero sobre el parámetro 'values'
          for value in values:
            distance = abs(value - target)
            values_distance_dict[value] = distance  # Asigno la distancia a la clave del valor en el diccionario
          
          ordered_distance_dict = {distance:value for value, distance in values_distance_dict.items()}
          distances_array = list(ordered_distance_dict.keys())
          
          # Ordeno las distancias contenidas en el array
          distances_array.sort()
          
          # Busco el valor cuya distancia es menor
          closest_target_num = ordered_distance_dict[distances_array[0]]
          return closest_target_num
        
        
        
        # Comienzo reordenando los valores del parámetro 'nums'
        nums.sort()
        
        # Defino un conjunto que contenga todos los valores obtenidos de la suma de tripletes
        sum_triplets_set = set()
        
        
        for index, num in enumerate(nums):
          
          # Hallo los tripletes mediante una lógica basada en punteros
          index_left_pointer = index + 1
          index_right_pointer = len(nums) - 1
        
          for _ in nums[index+1:]:
            
            if index_left_pointer == index_right_pointer:
              break
            
            # Defino los punteros
            left_pointer = nums[index_left_pointer]
            right_pointer = nums[index_right_pointer]
            
            # Sumo el triplete, y almaceno el resultado en el conjunto inicial
            triplet_sum = num + left_pointer + right_pointer
            sum_triplets_set.add(triplet_sum)
            
            if triplet_sum > target:
              
              # Reasigno el índice del puntero derecho
              index_right_pointer -= 1
              continue
              
            elif triplet_sum < target:
              
              # Reasigno el índice del puntero izquierdo
              index_left_pointer += 1
              continue
            
            continue
        
        # Ahora, busco el valor más cercano a 'target' dentro del conjunto 'sum_triplets_set'
        values = [num for num in sum_triplets_set] 
        
        # Ordeno la lista con los resultados
        values.sort()
        
        # Obtengo el valor más cercano al parámetro "target"
        closest_target_num = closest_num(values= values, 
                                         target= target)
        
        return closest_target_num
      
      
if __name__ == "__main__":
  
  nums = [0,0,0]
  target = 1
  solution = Solution()
  sol = solution.threeSumClosest(nums= nums, target= target)
  print(sol)
        
        