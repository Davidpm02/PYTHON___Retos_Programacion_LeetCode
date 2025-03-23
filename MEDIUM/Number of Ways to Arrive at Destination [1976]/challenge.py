"""
DESCRIPTION:

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

 

Constraints:

    1 <= n <= 200
    n - 1 <= roads.length <= n * (n - 1) / 2
    roads[i].length == 3
    0 <= ui, vi <= n - 1
    1 <= timei <= 109
    ui != vi
    There is at most one road connecting any two intersections.
    You can reach any intersection from any other intersection.

"""

from typing import List
from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        """
        Se encarga de hallar el total de rutas posibles para llegar
        a nuestro destino, dado una estructura de grafos de una ciudad.

        params:
            n (int)
            roads (List[List[int]])
        
        returns:
            int
        """
        
        MOD = 10**9 + 7

        # Paso 1: Construcción del grafo usando una lista de adyacencia
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))  # Grafo no dirigido
        
        # Paso 2: Inicialización para Dijkstra
        min_time = [float('inf')] * n  # Tiempo mínimo para llegar a cada nodo
        min_time[0] = 0  # El nodo inicial tiene un tiempo de llegada de 0
        ways = [0] * n  # Número de formas de llegar a cada nodo en el tiempo óptimo
        ways[0] = 1  # Solo hay una forma de estar en el nodo inicial
        
        # Cola de prioridad con (tiempo_acumulado, nodo_actual)
        heap = [(0, 0)]
        
        while heap:
            curr_time, node = heappop(heap)
            
            # Si encontramos un tiempo mayor al registrado, no continuamos
            if curr_time > min_time[node]:
                continue
            
            # Explorar vecinos
            for neighbor, travel_time in graph[node]:
                new_time = curr_time + travel_time
                
                if new_time < min_time[neighbor]:  # Encontramos un camino más corto
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]  # Se heredan las formas de llegar
                    heappush(heap, (new_time, neighbor))
                
                elif new_time == min_time[neighbor]:  # Otro camino con igual tiempo mínimo
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n - 1]