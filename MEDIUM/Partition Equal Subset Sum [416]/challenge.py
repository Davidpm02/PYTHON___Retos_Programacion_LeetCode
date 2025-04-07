"""
DESCRIPTION:

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)
        
        # Si la suma total es impar, no es posible dividir en dos subconjuntos iguales
        if total_sum % 2 != 0:
            return False
        
        # El objetivo es encontrar un subconjunto cuya suma sea la mitad del total
        target = total_sum // 2
        
        # Inicializo una lista DP donde dp[i] indica si se puede formar la suma i
        dp = [False] * (target + 1)
        dp[0] = True  # Siempre puedo formar suma 0 sin usar ningún elemento
        
        # Itero sobre cada número en el array
        for num in nums:
            # Recorro el array dp de atrás hacia adelante
            for i in range(target, num - 1, -1):
                # Para cada posición i, verifico si i se puede formar incluyendo num
                dp[i] = dp[i] or dp[i - num]
        
        # Devuelvo si es posible formar la suma objetivo
        return dp[target]