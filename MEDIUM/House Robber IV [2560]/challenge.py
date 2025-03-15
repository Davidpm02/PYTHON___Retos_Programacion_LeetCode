"""
DESCRIPTION:

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.

Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= (nums.length + 1)/2

"""

from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        """
        Se encargan de hallar la capacidad mínima del ladrón
        de entre todas las formas posibles de robar al menos 'k' casas.

        params:
            nums (List[int])
            k (int)

        returns:
            int 
        """

        # Función para verificar si con una capacidad dada podemos robar al menos k casas
        def can_steal(capability):
            # Contador de casas robadas
            count = 0
            i = 0
            
            while i < len(nums):
                # Si podemos robar esta casa (el dinero es <= que nuestra capacidad)
                if nums[i] <= capability:
                    count += 1
                    i += 2  # Saltamos a la siguiente casa no adyacente
                else:
                    i += 1  # No robamos esta casa, revisamos la siguiente
            
            # Retornamos True si podemos robar k o más casas
            return count >= k
        
        # Búsqueda binaria para encontrar la capacidad mínima
        left = min(nums)  # La capacidad mínima posible es el mínimo valor en nums
        right = max(nums)  # La capacidad máxima posible es el máximo valor en nums
        
        while left < right:
            mid = left + (right - left) // 2
            
            if can_steal(mid):
                # Si podemos robar k casas con esta capacidad, intentamos con una menor
                right = mid
            else:
                # Si no podemos, necesitamos aumentar la capacidad
                left = mid + 1
        
        return left
