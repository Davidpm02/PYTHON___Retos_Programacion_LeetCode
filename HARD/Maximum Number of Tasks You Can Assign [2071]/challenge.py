"""
DESCRIPTION:

You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

 

Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)
Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)
Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.
 

Constraints:

n == tasks.length
m == workers.length
1 <= n, m <= 5 * 10^4
0 <= pills <= m
0 <= tasks[i], workers[j], strength <= 10^9

"""

from typing import List
import bisect
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
        """
        Determina el número máximo de tareas que pueden completarse dadas
        las fuerzas de los trabajadores y píldoras mágicas.
           
        params:
            tasks (List[int])
            workers (List[int])
            pills (int)
            strength (int)
            
        returns:
            El número máximo de tareas que pueden completarse.
        """

        # Ordenar tareas en orden ascendente según la fuerza requerida
        tasks.sort()
        # Ordenar trabajadores en orden ascendente según su fuerza
        workers.sort()
        
        def canAssignTasks(k: int) -> bool:
            """
            Verifica si k tareas pueden completarse con los trabajadores y píldoras dados.
            
            Args:
                k: El número de tareas a asignar.
                
            Returns:
                True si es posible asignar k tareas, False en caso contrario.
            """
            if k == 0:
                return True
                
            # Si no tenemos suficientes trabajadores, es imposible
            if k > len(workers):
                return False
            
            # Considerar solo las k tareas más fáciles (con menor requerimiento de fuerza)
            selected_tasks = tasks[:k]
            # Considerar los k trabajadores más fuertes
            selected_workers = workers[-k:]
            
            # Usar una estructura multiset para trabajadores disponibles
            available_workers = deque(sorted(selected_workers))
            pills_remaining = pills
            
            # Procesar tareas de la más difícil a la más fácil
            for i in range(k-1, -1, -1):
                task = selected_tasks[i]
                
                # Si el trabajador más fuerte puede realizar la tarea sin píldora
                if available_workers and available_workers[-1] >= task:
                    available_workers.pop()
                    continue
                
                # Si no hay píldoras restantes, la asignación es imposible
                if pills_remaining == 0:
                    return False
                
                # Buscar el trabajador más débil que puede realizar la tarea con una píldora
                # Usar búsqueda binaria para encontrarlo eficientemente
                target = task - strength
                left, right = 0, len(available_workers) - 1
                found = False
                
                while left <= right:
                    mid = (left + right) // 2
                    if available_workers[mid] >= target:
                        found = True
                        right = mid - 1
                    else:
                        left = mid + 1
                
                # Si no hay ningún trabajador que pueda realizar la tarea con píldora
                if not found or left >= len(available_workers):
                    return False
                
                # Eliminar el trabajador usado
                del available_workers[left]
                pills_remaining -= 1
            
            return True
        
        # Búsqueda binaria para encontrar el máximo valor posible de k
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if canAssignTasks(mid):
                left = mid
            else:
                right = mid - 1
                
        return left