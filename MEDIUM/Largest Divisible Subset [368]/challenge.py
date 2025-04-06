"""
DESCRIPTION:

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.

"""

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        """
        Se encarga de verificar cual es el subconjunto de mayor 
        tamaño que se puede formar con los elementos contenidos
        dentro del array recibido como parámetro.

        params:
            nums (List[int])
        
        returns:
            List[int]
        """

        if not nums:
            return []
        
        # Ordenamos el array para facilitar la verificación de divisibilidad
        nums.sort()
        n = len(nums)
        
        # dp[i] representa el tamaño del mayor subconjunto que termina con nums[i]
        dp = [1] * n
        
        # prev[i] guarda el índice del elemento anterior en el subconjunto
        prev = [-1] * n
        
        # Índice del elemento con el mayor subconjunto
        max_index = 0
        
        # Algoritmo de programación dinámica
        for i in range(n):
            for j in range(i):
                # Si nums[i] es divisible por nums[j] y agregar nums[i] aumenta el tamaño del subconjunto
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            # Actualizamos el índice del elemento con el mayor subconjunto
            if dp[i] > dp[max_index]:
                max_index = i
        
        # Reconstruimos el subconjunto
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        # Invertimos para obtener el orden correcto
        return result[::-1]