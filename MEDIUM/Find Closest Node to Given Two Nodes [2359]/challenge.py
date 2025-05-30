"""
DESCRIPTION:

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

 

Example 1:


Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:


Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
 

Constraints:

n == edges.length
2 <= n <= 10^5
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n

"""

from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        """
        Dado un grafo dirigido donde cada nodo tiene a lo sumo una arista saliente,
        este método encuentra el índice del nodo alcanzable tanto desde node1 como
        node2, de modo que el máximo entre las distancias desde node1 y node2 a ese
        nodo sea mínimo. Si hay múltiples nodos que cumplen, se devuelve el de índice
        más pequeño. Si no existe ningún nodo común alcanzable, se devuelve -1.

        params:
            edges (List[int])
            node1 (int)
            node2 (int)
        returns:
            int
        """

        n = len(edges)
        
        def obtener_distancias(inicio: int) -> List[int]:
            # Inicializo todas las distancias con infinito para marcar nodos no visitados
            dist = [float('inf')] * n
            actual = inicio
            pasos = 0
            # Recorro la trayectoria hasta encontrar -1 o un nodo ya visitado
            while actual != -1 and dist[actual] == float('inf'):
                dist[actual] = pasos
                actual = edges[actual]
                pasos += 1
            return dist

        # Calculo distancias desde ambos nodos de inicio
        dist1 = obtener_distancias(node1)
        dist2 = obtener_distancias(node2)

        # Busco el nodo que minimiza el máximo entre ambas distancias
        respuesta = -1
        mejor_max_dist = float('inf')
        for i in range(n):
            d1 = dist1[i]
            d2 = dist2[i]
            # Considero solo nodos alcanzables desde node1 y node2
            if d1 < float('inf') and d2 < float('inf'):
                max_dist = max(d1, d2)
                # Actualizo si encuentro un máximo menor o un empate con índice más pequeño
                if max_dist < mejor_max_dist or (max_dist == mejor_max_dist and (respuesta == -1 or i < respuesta)):
                    mejor_max_dist = max_dist
                    respuesta = i

        return respuesta
