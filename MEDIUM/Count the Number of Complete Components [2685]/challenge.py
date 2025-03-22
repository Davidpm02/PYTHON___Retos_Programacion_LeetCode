"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.

Example 2:

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

 

Constraints:

    1 <= n <= 50
    0 <= edges.length <= n * (n - 1) / 2
    edges[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
    There are no repeated edges.

"""

from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        """
        Se encarga de contar el número de componentes completos dentro
        de un grafo adireccionado.

        params:
            n (int)
            edges (List[List[int]])
            
        returns:
            int
        """

        # Paso 1: Crear la lista de adyacencia para el grafo
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Paso 2: DFS para encontrar todas las componentes conectadas
        visited = [False] * n
        
        def dfs(v, component):
            visited[v] = True
            component.append(v)
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        components = []
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                components.append(component)
        
        # Paso 3: Verificar si una componente es completa
        def is_complete(component):
            num_vertices = len(component)
            num_edges = 0
            for v in component:
                num_edges += len([neighbor for neighbor in adj[v] if neighbor in component])
            # Cada arista se cuenta dos veces, una por cada vértice, por eso dividimos entre 2
            num_edges //= 2
            # Para ser completa, debe haber exactamente num_vertices * (num_vertices - 1) / 2 aristas
            return num_edges == num_vertices * (num_vertices - 1) // 2
        
        # Paso 4: Contar las componentes completas
        complete_count = 0
        for component in components:
            if is_complete(component):
                complete_count += 1
        
        return complete_count