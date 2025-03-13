"""
DESCRIPTION:

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

    Decrement the value at each index in the range [li, ri] in nums by at most vali.
    The amount by which each value is decremented can be chosen independently for each index.

A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

    For i = 0 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [1, 0, 1].
    For i = 1 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

    For i = 0 (l = 1, r = 3, val = 2):
        Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
        The array will become [4, 1, 0, 0].
    For i = 1 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
        The array will become [3, 0, 0, 0], which is not a Zero Array.

 

Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 5 * 105
    1 <= queries.length <= 105
    queries[i].length == 3
    0 <= li <= ri < nums.length
    1 <= vali <= 5

"""

from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        """
        Se encarga de hallar el número mínimo de consultas necesarias
        para convertir nums en una 'matriz cero'. 
        
        Una 'matriz cero' es una matriz con todos los elementos iguales a 0.
        Cada consulta permite disminuir elementos en un rango especificado 
        como máximo en un valor dado.

        params:
            nums (List[int])
            queries (List[List[int]])
        
        returns:
            int
        """

        # Verificamos si nums ya es un Zero Array
        if all(num == 0 for num in nums):
            return 0
        
        n = len(nums)
        m = len(queries)
        
        # Función para verificar si podemos obtener un Zero Array con k consultas
        def can_make_zero_array(k):
            # Usamos un difference array para eficientemente aplicar las operaciones de rango
            diff = [0] * (n + 1)
            
            # Aplicamos las primeras k consultas
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val  # Añadimos val en la posición l
                diff[r + 1] -= val  # Restamos val en la posición r+1
            
            # Reconstruimos el array después de aplicar las consultas
            # y verificamos si podemos reducir todo a 0
            decrement = 0
            for i in range(n):
                decrement += diff[i]  # Acumulamos la diferencia
                if decrement < nums[i]:  # Si no podemos reducir este elemento a 0
                    return False
            
            return True
        
        # Búsqueda binaria para encontrar el mínimo k
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            if can_make_zero_array(mid):
                right = mid
            else:
                left = mid + 1
        
        # Si no podemos obtener un Zero Array incluso después de todas las consultas
        if left == m and not can_make_zero_array(m):
            return -1
        
        return left