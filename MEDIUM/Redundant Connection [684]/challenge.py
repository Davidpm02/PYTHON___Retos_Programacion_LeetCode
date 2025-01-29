"""
DESCRIPTION:

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

 

Constraints:

    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected.

"""

from typing import List

class Solution:
    class DSU:
        def __init__(self, n):
            # Inicializo cada nodo como su propio representante (padre).
            self.parent = list(range(n + 1))
            self.rank = [1] * (n + 1)  # Optimizamos con unión por rango.

        def find(self, x):
            # Aplico compresión de ruta para optimizar futuras búsquedas.
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Compresión de ruta.
            return self.parent[x]

        def union(self, x, y):
            # Encuentro los líderes de cada conjunto.
            root_x = self.find(x)
            root_y = self.find(y)

            if root_x == root_y:
                return False  # Si ya estaban conectados, esta arista forma un ciclo.

            # Unión por rango: Conecto el árbol más pequeño debajo del mayor.
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1  # Incremento el rango del nuevo raíz.

            return True  # La unión fue exitosa.

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = self.DSU(n)

        # Procesamos cada arista en orden
        for edge in edges:
            u, v = edge
            if not dsu.union(u, v):  # Si la unión falla, encontramos la arista redundante
                return edge

        return []