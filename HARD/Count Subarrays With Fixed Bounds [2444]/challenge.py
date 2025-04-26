"""
DESCRIPTION:

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6

"""

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        """
        Cuenta el número de subarreglos con límites fijos en el arreglo
        nums.
        
        Un subarreglo con límites fijos es aquel donde el valor mínimo
        es exactamente minK y el valor máximo es exactamente maxK.
        
        params:
            nums (List[int])
            minK (int)
            maxK (int)
            
        returns:
            int
        """
        
        # Si minK es mayor que maxK, no hay solución posible
        if minK > maxK:
            return 0
            
        n = len(nums)
        result = 0
        
        # Inicializamos los índices
        left_bound = -1  # Índice del último elemento fuera de rango
        last_min = -1    # Última posición donde encontramos minK
        last_max = -1    # Última posición donde encontramos maxK
        
        for i in range(n):
            # Si el número actual está fuera del rango [minK, maxK]
            if nums[i] < minK or nums[i] > maxK:
                left_bound = i
            
            # Actualizamos los índices de las últimas ocurrencias de minK y maxK
            if nums[i] == minK:
                last_min = i
            if nums[i] == maxK:
                last_max = i
            
            # Calculamos el número de subarreglos válidos que terminan en la posición i
            # El subarreglo debe contener tanto minK como maxK
            valid_subarrays = min(last_min, last_max) - left_bound
            
            # Agregamos al resultado solo si hay subarreglos válidos
            result += max(0, valid_subarrays)
        
        return result