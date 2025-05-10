"""
DESCRIPTION:

There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 7

Explanation:

The minimum time required is 7 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
Example 2:

Input: moveTime = [[0,0,0,0],[0,0,0,0]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 4

 

Constraints:

2 <= n == moveTime.length <= 750
2 <= m == moveTime[i].length <= 750
0 <= moveTime[i][j] <= 109

"""

from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Calcula el tiempo mínimo para alcanzar la habitación inferior
        derecha en una cuadrícula de mazmorras.

        Cada celda tiene una restricción moveTime[i][j] que especifica
        el tiempo mínimo en el que puedes comenzar a moverte hacia esa 
        celda. 
        El coste de cada movimiento entre celdas adyacentes alterna 
        entre 1 segundo y 2 segundos, empezando por 1 segundo en el 
        primer movimiento.

       
        params:
            moveTime (List[List[int]])
        
        returns: 
            int
        """

        n, m = len(moveTime), len(moveTime[0])
        INF = 10**30

        # Defino dist[i][j][p] como el tiempo más temprano para llegar a (i,j) con paridad p
        dist = [[[INF, INF] for _ in range(m)] for __ in range(n)]
        
        # Comienzo en (0,0) en t=0, con el siguiente movimiento costando 1 segundo (paridad=0)
        dist[0][0][0] = 0

        # Cola de prioridad que almacena tuplas (tiempo, x, y, paridad)
        pq = [(0, 0, 0, 0)]
        
        # Direcciones de movimiento: abajo, arriba, derecha, izquierda
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            cur_t, x, y, p = heapq.heappop(pq)
            # Si ya encontramos un tiempo mejor, lo ignoramos
            if cur_t > dist[x][y][p]:
                continue
            # Si llegamos al destino, devolvemos el tiempo actual
            if x == n-1 and y == m-1:
                return cur_t

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    # Debo esperar al tiempo mínimo permitido para entrar en (nx,ny)
                    start_move_t = max(cur_t, moveTime[nx][ny])
                    # Coste del paso: 1 segundo si p=0, sino 2 segundos
                    step_cost = 1 if p == 0 else 2
                    new_t = start_move_t + step_cost
                    new_p = 1 - p
                    # Actualizo si encuentro un tiempo mejor
                    if new_t < dist[nx][ny][new_p]:
                        dist[nx][ny][new_p] = new_t
                        heapq.heappush(pq, (new_t, nx, ny, new_p))

        return -1

        