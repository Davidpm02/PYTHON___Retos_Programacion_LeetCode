"""
DESCRIPTION:

There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

Output: [9,7,9,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 0 from the second tree.
For i = 2, connect node 2 from the first tree to node 4 from the second tree.
For i = 3, connect node 3 from the first tree to node 4 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

Output: [6,3,3,3,3]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.


 

Constraints:

2 <= n, m <= 1000
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
0 <= k <= 1000

"""

from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        El método calcula, para cada nodo i en el primer árbol, el número
        máximo de nodos alcanzables dentro de distancia k tras conectar
        i con un nodo óptimamente elegido en el segundo árbol.
        
        params:
            edges1 (List[List[int]])
            edges2 (List[List[int]])
            k (int)

        returns:
            List[int]
        """

        # Construyo las listas de adyacencia para ambos árboles.
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

        # Función auxiliar para calcular cuántos nodos hay dentro de un
        # límite de distancia para cada nodo en un árbol.
        def compute_within_radius(adj: List[List[int]], limit: int) -> List[int]:
            counts = []
            # Si el límite es negativo, no hay nodos alcanzables.
            if limit < 0:
                return [0] * len(adj)
            for start in range(len(adj)):
                visited = [False] * len(adj)
                dist = [0] * len(adj)
                queue = deque([start])
                visited[start] = True
                reachable = 1  # incluyo el nodo inicial.

                # Realizo BFS hasta el límite dado.
                while queue:
                    node = queue.popleft()
                    if dist[node] == limit:
                        continue
                    for nei in adj[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            dist[nei] = dist[node] + 1
                            if dist[nei] <= limit:
                                reachable += 1
                                queue.append(nei)
                counts.append(reachable)
            return counts

        # Calculo los recuentos de nodos alcanzables en el primer árbol
        # dentro de k.
        counts1 = compute_within_radius(adj1, k)
        # Calculo los recuentos de nodos alcanzables en el segundo árbol
        # dentro de k-1 (uno de esos bordes lo uso para la conexión).
        counts2 = compute_within_radius(adj2, k - 1)

        # La mejor opción en el árbol2 es conectar al nodo con más nodos
        # alcanzables.
        max2 = max(counts2) if counts2 else 0

        # Para cada nodo del árbol1, sumo su propio recuento con el mejor
        # recuento del árbol2.
        result = [c1 + max2 for c1 in counts1]
        return result