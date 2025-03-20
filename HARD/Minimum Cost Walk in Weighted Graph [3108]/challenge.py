"""
DESCRIPTION:

There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]

Explanation:

To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).

In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

Example 2:

Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]

Output: [0]

Explanation:

To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

 

Constraints:

    2 <= n <= 105
    0 <= edges.length <= 105
    edges[i].length == 3
    0 <= ui, vi <= n - 1
    ui != vi
    0 <= wi <= 105
    1 <= query.length <= 105
    query[i].length == 2
    0 <= si, ti <= n - 1
    si != ti

"""

from typing import List

class DSU:
    def __init__(self, n: int):
        # Inicializo cada vértice como su propio representante.
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        # Uso compresión de caminos para optimizar las búsquedas.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # Encuentro los representantes de x e y.
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            # Ya están en el mismo componente.
            return False
        # Hago union por rango para mantener el árbol equilibrado.
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        """
        Calcula el costo mínimo de un camino entre pares de vértices en
        un grafo no dirigido y ponderado, donde el costo se define como
        el AND bit a bit de los pesos de las aristas del camino.
        Se utiliza la estructura Disjoint Set Union (DSU) para determinar
        si dos vértices pertenecen al mismo componente conexo.

        params:
            n (int)
            edges (List[List[int]])
            query (List[List[int]])

        returns:
            List[int]
        """
        
        # Inicializo el DSU con n vértices.
        dsu = DSU(n)
        
        # Uno los vértices de acuerdo a cada arista.
        for u, v, w in edges:
            dsu.union(u, v)
        
        # Para cada componente, calcularé el AND de todos sus pesos.
        # Uso un diccionario donde la llave es el representante del componente.
        comp_and = {}
        for u, v, w in edges:
            # Encuentro el representante (líder) para el componente.
            root = dsu.find(u)
            if root in comp_and:
                # Actualizo el valor AND acumulado.
                comp_and[root] &= w
            else:
                # Primera arista encontrada para este componente.
                comp_and[root] = w

        # Resuelvo cada consulta.
        res = []
        for s, t in query:
            # Verifico si s y t están en el mismo componente.
            if dsu.find(s) != dsu.find(t):
                res.append(-1)
            else:
                # Si la componente no tiene aristas (vértice aislado), no hay camino.
                # Aunque s y t sean el mismo, según el enunciado s != t.
                root = dsu.find(s)
                res.append(comp_and.get(root, -1))
        return res