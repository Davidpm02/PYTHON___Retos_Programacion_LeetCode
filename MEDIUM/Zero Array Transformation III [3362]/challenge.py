"""
DESCRIPTION:

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1

Explanation:

After removing queries[2], nums can still be converted to a zero array.

Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Example 2:

Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

Output: 2

Explanation:

We can remove queries[2] and queries[3].

Example 3:

Input: nums = [1,2,3,4], queries = [[0,3]]

Output: -1

Explanation:

nums cannot be converted to a zero array even after using all the queries.

 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= li <= ri < nums.length

"""

from typing import List

import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        """
        Se encarga de eliminar el mayor número posible de consultas
        (queries) tal que aún se pueda convertir el array `nums` 
        en un array de ceros.

        params:
          nums (List[int])
          queries (List[List[int]])

        returns:
          int
        """

        n = len(nums)
        
        # Agrupar queries por posición de inicio
        start_at = [[] for _ in range(n)]
        for i, (l, r) in enumerate(queries):
            start_at[l].append((r, i))
        
        # Heap de queries disponibles (max-heap por end position)
        available = []  # (-end_pos, query_index)
        used = set()
        
        # Array de diferencias para tracking de decrementos aplicados
        diff = [0] * (n + 1)
        current_decrement = 0
        
        for i in range(n):
            # Actualizar decremento actual usando diferencia
            current_decrement += diff[i]
            
            # Agregar queries que empiezan en posición i
            for end_pos, query_idx in start_at[i]:
                heapq.heappush(available, (-end_pos, query_idx))
            
            # Remover queries que ya no son válidas
            while available and -available[0][0] < i:
                heapq.heappop(available)
            
            # Determinar cuántos decrementos más necesitamos
            needed = nums[i] - current_decrement
            
            # Usar queries disponibles si es necesario
            while needed > 0 and available:
                end_pos_neg, query_idx = heapq.heappop(available)
                end_pos = -end_pos_neg
                
                # Verificar si la query realmente cubre la posición actual
                if end_pos >= i:
                    # Marcar query como usada
                    used.add(query_idx)
                    
                    # Aplicar decremento usando diferencia de arrays
                    current_decrement += 1
                    diff[end_pos + 1] -= 1
                    
                    needed -= 1
                # Si no cubre la posición actual, la descartamos (no la devolvemos al heap)
            
            # Si aún necesitamos más decrementos, es imposible
            if needed > 0:
                return -1
        
        return len(queries) - len(used)