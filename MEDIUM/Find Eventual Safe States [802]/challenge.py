"""
DESCRIPTION:

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

Example 1:
Illustration of graph

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

 

Constraints:

    n == graph.length
    1 <= n <= 104
    0 <= graph[i].length <= n
    0 <= graph[i][j] <= n - 1
    graph[i] is sorted in a strictly increasing order.
    The graph may contain self-loops.
    The number of edges in the graph will be in the range [1, 4 * 104].

"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        """
        Se encarga de verificar todos los nodos seguros de un grafo
        recibido como parámetro, y retornar una lista ordenada con
        estos nodos.

        params:
            graph (List[List[int]])
        returns:
            List[int]
        """
        
        n = len(graph)
        
        # Paso 1: Construir el grafo invertido
        reverse_graph = defaultdict(list)
        out_degree = [0] * n  # Conteo de grados de salida de cada nodo
        
        for src, neighbors in enumerate(graph):
            out_degree[src] = len(neighbors)
            for dest in neighbors:
                reverse_graph[dest].append(src)
        
        # Paso 2: Cola con nodos terminales (sin conexiones de salida)
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n  # Marcar nodos seguros
        
        while queue:
            current = queue.popleft()
            safe[current] = True  # Marcar el nodo actual como seguro
            # Reducir el grado de salida de sus padres en el grafo invertido
            for parent in reverse_graph[current]:
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    queue.append(parent)
        
        return sorted([i for i in range(n) if safe[i]])