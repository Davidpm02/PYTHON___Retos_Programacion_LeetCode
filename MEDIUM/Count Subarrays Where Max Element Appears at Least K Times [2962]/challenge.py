"""
DESCRIPTION:

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5

"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        """
        Cuenta el número de subarrays contiguos en los que el valor máximo del array 'nums'
        aparece al menos 'k' veces.

        params:
          nums (List[int])
          k (int)

        returns:
          int
        """

        max_val = max(nums)  # Identifico el valor máximo en el array
        count = 0            # Contador de ocurrencias del valor máximo
        res = 0              # Resultado final
        left = 0             # Límite izquierdo de la ventana

        # Recorro el array con una ventana deslizante
        for right in range(len(nums)):
            # Si el elemento actual es el máximo, incremento el contador
            if nums[right] == max_val:
                count += 1

            # Si ya tengo al menos 'k' apariciones del valor máximo en la ventana,
            # puedo contar todos los subarrays posibles desde 'left' hasta el final actual
            while count >= k:
                # Sumo todos los subarrays que terminan en 'right' y comienzan entre 'left' y 'right'
                res += len(nums) - right
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return res