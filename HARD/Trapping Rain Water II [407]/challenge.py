"""
DESCRIPTION:

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:

Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:

Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

 

Constraints:

    m == heightMap.length
    n == heightMap[i].length
    1 <= m, n <= 200
    0 <= heightMap[i][j] <= 2 * 104

"""

import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        """
        Se encarga de calcular el total de bloques ocupados por el
        agua tras una lluvia.

        El parámetro 'heightMap' representa los bloques de tierra 
        del mapa sobre el que llueve.

        params:
            heightMap List[List[int]])
        returns:
            int
        """
        
        # Verifico las dimensiones de la matriz
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # Cola de prioridad
        
        # Agrego los bordes a la cola de prioridad
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(1, n - 1):
            for i in [0, m - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        # Proceso la cola de prioridad para calcular el agua atrapada
        trapped_water = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Vecinos (derecha, abajo, izquierda, arriba)

        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Calculamos el agua atrapada si la celda es más baja
                    trapped_water += max(0, height - heightMap[nx][ny])
                    # Agregamos el vecino a la cola con el nuevo límite de altura
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return trapped_water
