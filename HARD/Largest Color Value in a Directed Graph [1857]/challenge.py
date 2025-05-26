"""
DESCRIPTION:

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:

n == colors.length
m == edges.length
1 <= n <= 10^5
0 <= m <= 10^5
colors consists of lowercase English letters.
0 <= aj, bj < n

"""

from collections import deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        Se encarga de calcular el valor máximo de color en cualquier 
        camino válido dentro de un grafo dirigido.
        
        Si el grafo contiene un ciclo, el método devuelve -1.

        params:
            colors (str)
            edges (List[List[int]])
        
        returns:
            int
        """
        
        n = len(colors)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        processed = 0
        result = 0

        while queue:
            u = queue.popleft()
            processed += 1
            result = max(result, max(dp[u]))

            for v in adj[u]:
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0))
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        if processed < n:
            return -1

        return result
