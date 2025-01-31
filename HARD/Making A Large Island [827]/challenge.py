"""
DESCRIPTION:

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.

"""

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        """
        Se encarga de hallar el tamaño de la isla más grande que puede
        construirse con los bits fijados de la matriz.

        La función toma en cuenta la posibilidad de cambiar un único
        bit 0 a 1 para incorporarlo a la isla de mayor tamaño. El bit
        0 a transformar debe esta conectado a los bits fijados que 
        conformen la isla.

        params:
            grid (List[List[int]])
        returns:
            int
        """

        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimientos en 4 direcciones
        island_size = {}  # Mapeo de id de isla -> tamaño
        island_id = 2  # Comenzamos desde 2 para evitar conflictos con 0 y 1

        # Función DFS para explorar y marcar la isla con un id
        def dfs(x, y, island_id):
            stack = [(x, y)]
            grid[x][y] = island_id
            size = 0

            while stack:
                i, j = stack.pop()
                size += 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = island_id
                        stack.append((ni, nj))

            return size

        # Paso 1: Identificar y etiquetar todas las islas
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[island_id] = dfs(i, j, island_id)
                    island_id += 1

        # Si no hay ceros, la isla más grande ya está en la matriz
        if not any(0 in row for row in grid):
            return n * n

        # Paso 2: Evaluar el impacto de cambiar cada 0 a 1
        max_island = max(island_size.values(), default=0)  # Tamaño máximo encontrado

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    new_size = 1  # Contamos la celda convertida en 1

                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            island_id = grid[ni][nj]
                            if island_id not in seen:
                                seen.add(island_id)
                                new_size += island_size[island_id]

                    max_island = max(max_island, new_size)

        return max_island