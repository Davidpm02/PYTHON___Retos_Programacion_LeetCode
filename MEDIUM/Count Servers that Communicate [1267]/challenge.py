"""
DESCRIPTION:

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1

"""

from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        """
        Se encarga de contabilizar todos los servidores que se encuentran
        comunicados dentro de una matriz binaria.

        Un 1 en una posición de la matriz indica la presencia de un servidor,
        mientras que un 0 representa la ausencia del mismo.

        params:
            grid (List[List[int]])
        
        returns:
            int
        """

        # Filas y columnas dentro de la matriz
        n, m = len(grid), len(grid[0])

        # Mapeo el número de servidores por fila y columna
        servers_in_rows = [sum(row) for row in grid]
        servers_in_columns = [sum([grid[r][i] for r in range(n)]) for i in range(m)]    

        communicated_servers = 0
        for r in range(n):
            for c in range(m):
                if ((grid[r][c] == 1) and ((servers_in_rows[r] > 1) or (servers_in_columns[c] > 1))):
                    communicated_servers += 1
        return communicated_servers