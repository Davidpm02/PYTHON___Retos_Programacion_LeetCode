"""
DESCRIPTION:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        """
           Summary:
               Método de la clase Solution encargado de procesar dos arrays de entrada, y retornar la mediana de los 
               valores registrados en estos.
           
           Args:
              - nums1 -- Primer array 
              - nums2 -- Segundo array
        
           Returns:
              float -- Mediana de los valores registrados dentro de cada array.
        """
        
        # Defino una lista con los numeros de ambos arrays
        merged_array = nums1.copy()
        
        # Añado los números del segundo array
        merged_array += nums2

        # Ordeno la lista
        merged_array.sort()
        
        # En caso de que la lista tenga un número de elementos par, tomo la media de los dos valores
        # centrales. En caso de tener una longitud impar, 
        if len(merged_array)%2 == 0:  # La lista tiene un número de elementos par
            length_merged_array = len(merged_array)
            half_length_merged_array = length_merged_array // 2
             
            min__middle_values = merged_array[half_length_merged_array - 1]
            max__middle_values = merged_array[half_length_merged_array]
            
            result = (min__middle_values + max__middle_values) / 2 
            return float(result)
        
        else:   # La lista tiene un número de elementos impar
            length_merged_array = len(merged_array)
            length_merged_array__minus_1 = length_merged_array - 1
            n_values_edges = length_merged_array__minus_1 // 2
            
            result = merged_array[n_values_edges]
            return float(result)



if __name__ == '__main__':
    
    array1 = [1,2, 5]
    array2 = [3,4]
    solution = Solution()
    sol = solution.findMedianSortedArrays(nums1 = array1,
                                          nums2 = array2)
    print(sol)
    