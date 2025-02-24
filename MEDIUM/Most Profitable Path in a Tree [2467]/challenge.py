"""
DESCRIPTION:

There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

    the price needed to open the gate at node i, if amount[i] is negative, or,
    the cash reward obtained on opening the gate at node i, otherwise.

The game goes on as follows:

    Initially, Alice is at node 0 and Bob is at node bob.
    At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
    For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
        If the gate is already open, no price will be required, nor will there be any cash reward.
        If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
    If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.

Return the maximum net income Alice can have if she travels towards the optimal leaf node.

 

Example 1:

Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
Output: 6
Explanation: 
The above diagram represents the given tree. The game goes as follows:
- Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
  Alice's net income is now -2.
- Both Alice and Bob move to node 1. 
  Since they reach here simultaneously, they open the gate together and share the reward.
  Alice's net income becomes -2 + (4 / 2) = 0.
- Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
  Bob moves on to node 0, and stops moving.
- Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
Now, neither Alice nor Bob can make any further moves, and the game ends.
It is not possible for Alice to get a higher net income.

Example 2:

Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
Output: -7280
Explanation: 
Alice follows the path 0->1 whereas Bob follows the path 1->0.
Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280. 

 

Constraints:

    2 <= n <= 105
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    edges represents a valid tree.
    1 <= bob < n
    amount.length == n
    amount[i] is an even integer in the range [-104, 104].

"""

from typing import List
from collections import defaultdict
import sys

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Aumento el límite de recursión para asegurarme de poder recorrer árboles con hasta 10^5 nodos.
        sys.setrecursionlimit(10**6)
        n = len(amount)
        
        # Construyo el grafo (lista de adyacencia) a partir de los bordes
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Utilizo un DFS/BFS desde la raíz (nodo 0) para calcular el padre y la profundidad (tiempo de llegada de Alice) de cada nodo
        parent = [-1] * n   # Almaceno el padre de cada nodo
        depth = [0] * n     # Almaceno la profundidad (distancia desde la raíz) de cada nodo
        
        # Uso una pila para el DFS
        stack = [0]
        visited = {0}
        while stack:
            node = stack.pop()
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    parent[neigh] = node
                    depth[neigh] = depth[node] + 1
                    stack.append(neigh)
        
        # Calculo los tiempos de llegada de Bob a los nodos a lo largo de su camino desde 'bob' hasta la raíz
        # Inicializo todos los tiempos de Bob como infinito (Bob no visita esos nodos)
        bob_time = [float('inf')] * n
        t = 0
        node = bob
        # Mientras no se llegue a la raíz (parent = -1), asigno el tiempo en el que Bob llega a cada nodo
        while node != -1:
            bob_time[node] = t
            t += 1
            node = parent[node]
        
        # Ahora realizo un DFS desde la raíz para explorar todas las rutas raíz-hoja y calcular la ganancia neta de Alice.
        max_profit = -float('inf')
        
        def dfs(node: int, curr_time: int, curr_profit: int, parent_node: int):
            nonlocal max_profit
            
            # Calculo la ganancia para el nodo actual según el tiempo de llegada de Alice (curr_time)
            # y el tiempo en que Bob llega a este nodo (bob_time[node]).
            if curr_time < bob_time[node]:
                # Si Alice llega antes, obtengo el monto completo (positivo o negativo)
                curr_profit += amount[node]
            elif curr_time == bob_time[node]:
                # Si llegan al mismo tiempo, comparto el monto (mitad para Alice)
                curr_profit += amount[node] // 2
            # Si curr_time > bob_time[node], Bob ya abrió la puerta y Alice no obtiene ni paga nada.
            
            # Si el nodo actual es hoja (exceptuando la raíz), actualizo la ganancia máxima.
            if node != 0 and len(graph[node]) == 1:
                max_profit = max(max_profit, curr_profit)
                return
            
            # Recorro los nodos vecinos, evitando volver al nodo padre para no retroceder
            for neigh in graph[node]:
                if neigh != parent_node:
                    dfs(neigh, curr_time + 1, curr_profit, node)
        
        # Inicio el DFS desde la raíz (nodo 0) con tiempo 0 y ganancia 0
        dfs(0, 0, 0, -1)
        return max_profit
