"""
DESCRIPTION:

You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.

 

Example 1:

Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.

Example 2:

Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.

Example 3:

Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.

 

Constraints:

    grid.length == 2
    n == grid[r].length
    1 <= n <= 5 * 104
    1 <= grid[r][c] <= 105

"""

from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        """
        Calcula los puntos recolectados por el segundo robot dado un grid 2xN.
        Ambos robots juegan de manera óptima.
        
        params:
            grid List[List[int]] - matriz de puntos de tamaño 2xN
        
        returns:
            int
        """
        
        n = len(grid[0])
        
        # Crear acumulados para cada fila (filas 0 y 1)
        top_prefix_sum = [0] * n
        bottom_prefix_sum = [0] * n
        
        # Llenar los acumulados de la fila superior (0) y la inferior (1)
        for i in range(n):
            top_prefix_sum[i] = top_prefix_sum[i - 1] + grid[0][i] if i > 0 else grid[0][i]
            bottom_prefix_sum[i] = bottom_prefix_sum[i - 1] + grid[1][i] if i > 0 else grid[1][i]

        # Inicializar el mínimo del máximo de puntos que el segundo robot puede tomar
        min_points = float('inf')

        for i in range(n):
            # Puntos disponibles si el primer robot corta en la columna i
            points_top = top_prefix_sum[n - 1] - top_prefix_sum[i]
            points_bottom = bottom_prefix_sum[i - 1] if i > 0 else 0
            
            # El segundo robot tomará el máximo de los dos caminos disponibles
            second_robot_points = max(points_top, points_bottom)
            
            # Actualizar el mínimo
            min_points = min(min_points, second_robot_points)

        return min_points