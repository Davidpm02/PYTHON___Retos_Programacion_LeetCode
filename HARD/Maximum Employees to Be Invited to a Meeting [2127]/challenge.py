"""
DESCRIPTION:

A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

 

Example 1:

Input: favorite = [2,2,1,2]
Output: 3
Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3. 

Example 2:

Input: favorite = [1,2,0]
Output: 3
Explanation: 
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.

Example 3:

Input: favorite = [3,0,1,4,1]
Output: 4
Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.

 

Constraints:

    n == favorite.length
    2 <= n <= 105
    0 <= favorite[i] <= n - 1
    favorite[i] != i

"""

from typing import List

from collections import deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:

        """
        Se encarga de calcular el número de empleados que acudirán 
        a una reunión en una mesa redonda.

        La función trata de maximizar el número de empleados que 
        acudirán, teniendo en cuenta que un empleado solo acudirá
        si acude su empleado favorito, y que cada empleado solo puede
        tener a dos empleados sentados a sus lados en la mesa.

        params:
            favorite (List[int])

        returns:
            int        
        """

        n = len(favorite)
        
        def max_cycle(fa: List[int]) -> int:
            vis = [False] * n
            max_cycle_len = 0
            for i in range(n):
                if vis[i]:
                    continue
                cycle = []
                j = i
                while not vis[j]:
                    cycle.append(j)
                    vis[j] = True
                    j = fa[j]
                for k, v in enumerate(cycle):
                    if v == j:
                        max_cycle_len = max(max_cycle_len, len(cycle) - k)
                        break
            return max_cycle_len
        
        def longest_chain(fa: List[int]) -> int:
            indegree = [0] * n
            for v in fa:
                indegree[v] += 1
            
            q = deque(i for i in range(n) if indegree[i] == 0)
            dist = [1] * n
            
            while q:
                i = q.popleft()
                dist[fa[i]] = max(dist[fa[i]], dist[i] + 1)
                indegree[fa[i]] -= 1
                if indegree[fa[i]] == 0:
                    q.append(fa[i])
            
            return sum(dist[i] for i in range(n) if i == fa[fa[i]])
        
        return max(max_cycle(favorite), longest_chain(favorite))
