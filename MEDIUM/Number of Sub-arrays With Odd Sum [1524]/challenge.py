"""
DESCRIPTION:

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16

 

Constraints:

    1 <= arr.length <= 105
    1 <= arr[i] <= 100

"""

from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        """
        Se encarga de obtener el total de subarrays contiguas
        entre sí con una suma de elementos impar, a partir del array
        'arr'.

        params:
            arr (List[int])
        
        returns:
            int
        """

        MOD = 10**9 + 7
        
        odd_count = 0  # Cantidad de sumas acumuladas impares encontradas
        even_count = 1  # Inicializamos en 1 porque una suma de 0 es considerada par
        prefix_sum = 0  # Suma acumulativa
        result = 0  # Contador de subarrays con suma impar

        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:  # Si la suma acumulada es par
                result += odd_count  # Solo los prefijos impares previos generan suma impar
                even_count += 1  # Incremento el número de prefijos pares
            else:  # Si la suma acumulada es impar
                result += even_count  # Solo los prefijos pares previos generan suma impar
                odd_count += 1  # Incremento el número de prefijos impares
            
            result %= MOD  # Aplicamos módulo según el problema
        
        return result