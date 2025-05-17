"""
DESCRIPTION:

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        El método implementa un algoritmo básico Bubble Sort para 
        ordenar los elementos de una array numérico.

        El método no retorna nada; actualiza el array recibido como
        argumento en tiempo de ejecución.

        params:
            nums (List[int])
        
        returns:
            None
        """
        
        n = len(nums)

        # Itero sobre todos los elementos para asegurar que se ordenen todos.
        for i in range(n):
            # La última i posiciones ya están ordenadas, así que voy reduciendo el rango.
            for j in range(0, n - i - 1):
                # Comparo elemento actual con el siguiente para intercambiarlos si están fuera de orden.
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Hago el swap de posiciones.