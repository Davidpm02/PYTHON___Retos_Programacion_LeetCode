"""
DESCRIPTION:

There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

Output: [8,7,7,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 4 from the second tree.
For i = 2, connect node 2 from the first tree to node 7 from the second tree.
For i = 3, connect node 3 from the first tree to node 0 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]

Output: [3,6,6,6,6]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.


 

Constraints:

2 <= n, m <= 10^5
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.

"""

from typing import List, Tuple
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """
        Calcula, para cada nodo i en el primer árbol, el número máximo
        de nodos 'target' (distancia par) si se conecta i con el mejor
        nodo del segundo árbol.
        
        params:
            edges1 (List[List[int]])
            edges2 (List[List[int]]) 

        returns:
            List[int]

        """
        
        # Construyo listas de adyacencia
        n = len(edges1) + 1
        m = len(edges2) + 1
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Función para colorear por paridad de profundidad (0 o 1) y contar tamaño de cada color
        def bipartite_counts(adj: List[List[int]]) -> Tuple[List[int], int, int]:
            n = len(adj)
            color = [-1] * n
            count0 = count1 = 0
            queue = deque([0])
            color[0] = 0
            count0 += 1
            # BFS para colorear
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        # asigno color opuesto al padre
                        color[v] = 1 - color[u]
                        if color[v] == 0:
                            count0 += 1
                        else:
                            count1 += 1
                        queue.append(v)
            return color, count0, count1

        # Coloreo árbol1 y cuento colores
        color1, c10, c11 = bipartite_counts(adj1)
        # Coloreo árbol2 y cuento colores
        color2, c20, c21 = bipartite_counts(adj2)

        # Elijo en el segundo árbol el color de conexión que maximiza nodos 'target'
        # (nodos de color distinto al punto de conexión)
        # Si conecto a un nodo color 0, obtengo c21 nodos a distancia par (distancia=1+odd)
        # Si conecto a un nodo color 1, obtengo c20 nodos.
        best2 = max(c20, c21)

        # Para cada i, los nodos target en árbol1 son los de su mismo color
        result = []
        for i in range(n):
            if color1[i] == 0:
                # cuento todos los de color 0 en árbol1 y sumo best2
                result.append(c10 + best2)
            else:
                result.append(c11 + best2)
        return result
