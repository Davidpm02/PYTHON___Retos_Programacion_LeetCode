"""
DESCRIPTION:

You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

    Each node in the graph belongs to exactly one group.
    For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.

Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

 

Example 1:

Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

Example 2:

Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.

 

Constraints:

    1 <= n <= 500
    1 <= edges.length <= 104
    edges[i].length == 2
    1 <= ai, bi <= n
    ai != bi
    There is at most one edge between any pair of vertices.

"""

from typing import List
from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        """
        Se encarga de contabilizar el número máximo de grupos
        en los que se pueden separar los diferentes nodos del array
        'edges' recibido como parámetro.

        params:
            n (int)
            edges (List[List[int]])

        returns:
            int
        """

        # Construimos la representación del grafo con listas de adyacencia
        graph = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Función para comprobar si un componente es bipartito y obtener su tamaño máximo de grupos
        def bfs(start):
            queue = deque([(start, 1)])  # (nodo, nivel del grupo)
            levels = {start: 1}
            max_depth = 1
            while queue:
                node, level = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in levels:
                        levels[neighbor] = level + 1
                        max_depth = max(max_depth, level + 1)
                        queue.append((neighbor, level + 1))
                    elif abs(levels[neighbor] - levels[node]) != 1:
                        return -1  # No es bipartito
            return max_depth
        
        # Detectar componentes conexos
        visited = set()
        components = []
        
        for node in range(1, n + 1):
            if node not in visited:
                component = []
                queue = deque([node])
                while queue:
                    v = queue.popleft()
                    if v not in visited:
                        visited.add(v)
                        component.append(v)
                        queue.extend(graph[v])
                components.append(component)
        
        # Para cada componente, verificar si es bipartito y calcular la máxima profundidad
        total_groups = 0
        for component in components:
            max_groups = 0
            for node in component:
                depth = bfs(node)
                if depth == -1:
                    return -1
                max_groups = max(max_groups, depth)
            total_groups += max_groups
        
        return total_groups