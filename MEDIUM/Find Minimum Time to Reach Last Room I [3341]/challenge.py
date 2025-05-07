"""
DESCRIPTION:

There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3

 

Constraints:

2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 10^9

"""

from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Calcula el tiempo mínimo para llegar a la sala inferior derecha
        en una dungeon.

        Cada celda (i, j) tiene una restricción moveTime[i][j],
        que es el tiempo mínimo en segundos en el que se puede empezar a
        moverse hacia esa sala. Moverse entre salas adyacentes siempre
        toma exactamente un segundo.

        params:
            moveTime (List[List[int]])

        returns:
            int
        """

        # Inicializo dimensiones y estructuras
        n = len(moveTime)
        m = len(moveTime[0]) if n > 0 else 0

        # Inicializo matriz dist para almacenar el tiempo mínimo
        # conocido a cada celda
        dist = [[float('inf')] * m for _ in range(n)]
        
        # Defino los posibles movimientos: abajo, arriba, derecha, izquierda
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Uso un min-heap (cola de prioridad) con tuplas (tiempo, x, y)
        heap = []
        
        # Comienzo en (0,0) a tiempo 0
        dist[0][0] = 0
        heapq.heappush(heap, (0, 0, 0))

        # Proceso nodos en orden creciente de tiempo actual
        while heap:
            current_time, x, y = heapq.heappop(heap)
            # Omite entradas obsoletas
            if current_time > dist[x][y]:
                continue
            # Si llego a la celda destino, retorno el resultado
            if x == n - 1 and y == m - 1:
                return current_time
            # Exploro vecinos
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Verifico que el vecino esté dentro de los límites
                if 0 <= nx < n and 0 <= ny < m:
                    # Calculo el tiempo mínimo para comenzar a moverse al vecino
                    start_move = max(current_time, moveTime[nx][ny])
                    # La llegada se produce un segundo después
                    arrival = start_move + 1
                    # Si esta ruta mejora la distancia conocida, actualizo y agrego al heap
                    if arrival < dist[nx][ny]:
                        dist[nx][ny] = arrival
                        heapq.heappush(heap, (arrival, nx, ny))
    
        return -1
