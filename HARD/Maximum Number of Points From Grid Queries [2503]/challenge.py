"""
DESCRIPTION:

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

    If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
    Otherwise, you do not get any points, and you end this process.

After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:

Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.

Example 2:

Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.

 

Constraints:

    m == grid.length
    n == grid[i].length
    2 <= m, n <= 1000
    4 <= m * n <= 105
    k == queries.length
    1 <= k <= 104
    1 <= grid[i][j], queries[i] <= 106

"""

from typing import List
from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        

        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
        
        # Ordenamos las queries con su índice original
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])
        answer = [0] * len(queries)
        
        # Min-Heap para procesar las celdas en orden creciente
        heap = [(grid[0][0], 0, 0)]  # (valor de la celda, fila, columna)
        visited = set()
        visited.add((0, 0))
        
        # Contador de puntos
        points = 0
        processed_value = 0  # Último valor de celda procesado

        for index, q in queries_sorted:
            # Expandimos el heap hasta que la celda mínima sea >= query actual
            while heap and heap[0][0] < q:
                val, r, c = heappop(heap)  # Sacamos la celda con el menor valor
                processed_value = val  # Actualizamos el valor procesado
                points += 1  # Ganamos un punto
                
                # Exploramos celdas vecinas
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        heappush(heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))

            # Guardamos la cantidad de puntos obtenidos para la query actual
            answer[index] = points
        
        return answer