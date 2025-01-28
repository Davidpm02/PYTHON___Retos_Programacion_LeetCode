"""
DESCRIPTION:

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

    A land cell if grid[r][c] = 0, or
    A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

    Catch all the fish at cell (r, c), or
    Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:

Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

Example 2:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    0 <= grid[i][j] <= 10

"""

from typing import List

from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        # Obtener las dimensiones de la malla
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0

        max_fish = 0  # Almacenará el máximo número de peces encontrado
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Vecinos posibles (arriba, abajo, izquierda, derecha)

        def bfs(start_row: int, start_col: int) -> int:
            """
            Realiza una búsqueda en amplitud (BFS) desde la posición (start_row, start_col).
            Devuelve el número total de peces en la región conectada.
            """
            nonlocal grid  # Para modificar la variable 'grid' de manera no local

            queue = deque()
            queue.append((start_row, start_col))
            fish_count = grid[start_row][start_col]
            grid[start_row][start_col] = 0  # Marco como visitado

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # Verifico si las nuevas coordenadas están dentro de los límites y contienen peces
                    if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] != 0:
                        fish_count += grid[new_row][new_col]
                        grid[new_row][new_col] = 0  # Marco como visitado
                        queue.append((new_row, new_col))

            return fish_count

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    current_fish = bfs(i, j)
                    if current_fish > max_fish:
                        max_fish = current_fish

        return max_fish