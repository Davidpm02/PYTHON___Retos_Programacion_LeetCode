"""
DESCRIPTION:

You are given a

nums.

You can do the following operation on the array any number of times (possibly zero):

    Choose any 3 consecutive elements from the array and flip all of them.

Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

Example 1:

Input: nums = [0,1,1,1,0,0]

Output: 3

Explanation:
We can do the following operations:

    Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
    Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
    Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

Example 2:

Input: nums = [0,1,1,1]

Output: -1

Explanation:
It is impossible to make all elements equal to 1.

 

Constraints:

    3 <= nums.length <= 105
    0 <= nums[i] <= 1

"""

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        """
        Se encarga de hallar el número mínimo de operaciones
        a llevar a cabo dentro del array 'nums' para convertir todos
        los elementos a 1.

        Los movimientos se aplican en tripletes de números consecutivos.

        params:
            nums (List[int])
        
        returns:
            int
        """    

        n = len(nums)
        flips = 0  # Contador de operaciones
        flip_effect = [0] * (n + 1)  # Array auxiliar para rastrear los flips
        curr_flips = 0  # Contador de flips en la ventana
        
        for i in range(n - 2): 
            curr_flips += flip_effect[i]  # Aplicamos los flips previos
            
            if (nums[i] + curr_flips) % 2 == 0:  # Si el bit sigue siendo 0 después de los flips previos
                flips += 1
                curr_flips += 1  # Aplicamos un flip
                flip_effect[i + 3] -= 1  # Revertimos el flip después de la ventana
        
        # Verificamos si los últimos dos elementos quedaron en 1
        for i in range(n - 2, n):
            curr_flips += flip_effect[i]
            if (nums[i] + curr_flips) % 2 == 0:
                return -1
        
        return flips