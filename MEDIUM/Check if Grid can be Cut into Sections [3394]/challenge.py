"""
DESCRIPTION:

You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

    (startx, starty): The bottom-left corner of the rectangle.
    (endx, endy): The top-right corner of the rectangle.

Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

    Each of the three resulting sections formed by the cuts contains at least one rectangle.
    Every rectangle belongs to exactly one section.

Return true if such cuts can be made; otherwise, return false.

 

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Explanation:

The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:

Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

Output: true

Explanation:

We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:

Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

Output: false

Explanation:

We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

 

Constraints:

    3 <= n <= 109
    3 <= rectangles.length <= 105
    0 <= rectangles[i][0] < rectangles[i][2] <= n
    0 <= rectangles[i][1] < rectangles[i][3] <= n
    No two rectangles overlap.

"""

from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        """
        Se encarga de verificar si es posible establecer un corte que
        separe los rectángulos (cuyas coordenadas se definen en el
        parámetro 'rectangles').

        Para validar un corte correcto, no se tienen en cuenta el número
        de rectángulos que contiene cada una de las partes finales.
        Sin embargo:
         - Cada partición debe contener al menos un rectángulo.
         - Cada rectángulo debe pertenecer a una única partición.

        params:
            n (int)
            rectangles (List[List[int]])
        
        returns:
            bool
        """

        # Intento la partición en la dirección vertical (usando coordenadas x)
        if self.valid_partition(rectangles, axis=0):
            return True
        # Intento la partición en la dirección horizontal (usando coordenadas y)
        if self.valid_partition(rectangles, axis=1):
            return True
        return False

    def valid_partition(self, rectangles: List[List[int]], axis: int) -> bool:
        """
        Verifica si es posible particionar los intervalos de los rectángulos en tres grupos
        disjuntos en el eje indicado.
        
        params:
          rectangles: (List[List[int]])
          axis (int)
        
        returns:
          bool
        """

        # Para axis 0, usamos start_x y end_x; para axis 1, usamos start_y y end_y.
        if axis == 0:
            intervals = [(rect[0], rect[2]) for rect in rectangles]
        else:
            intervals = [(rect[1], rect[3]) for rect in rectangles]
        
        # Ordeno los intervalos por el valor de inicio.
        intervals.sort(key=lambda x: x[0])
        n_rect = len(intervals)
        if n_rect < 3:
            return False  # se requieren al menos 3 rectángulos para tres secciones
        
        # Calculo el arreglo prefix_max: prefix_max[i] es el máximo de end en [0, i].
        prefix_max = [0] * n_rect
        prefix_max[0] = intervals[0][1]
        for i in range(1, n_rect):
            prefix_max[i] = max(prefix_max[i - 1], intervals[i][1])
        
        # Determino en qué posiciones es posible un corte:
        # Un corte entre i y i+1 es válido si prefix_max[i] <= intervals[i+1][0].
        cut_possible = [False] * (n_rect - 1)
        for i in range(n_rect - 1):
            if prefix_max[i] <= intervals[i + 1][0]:
                cut_possible[i] = True
        
        # Buscamos índices i y j (i < j) tales que:
        #   cut_possible[i] y cut_possible[j] sean True.
        # Nota: i corresponde al final del grupo1 y j al final del grupo2.
        count_cuts = sum(cut_possible)
        if count_cuts < 2:
            return False

        # Verifico que los cortes no estén en posiciones consecutivas de forma que
        # algún grupo quede vacío.
        valid_cut_indices = [i for i, valid in enumerate(cut_possible) if valid]
        for k in range(len(valid_cut_indices) - 1):
            if valid_cut_indices[k+1] - valid_cut_indices[k] >= 1:  # porque el grupo intermedio será [i+1, j]
                # Verifico que no se esté tomando el primer o el último elemento para no dejar grupo vacío.
                if valid_cut_indices[k] >= 0 and valid_cut_indices[k+1] < n_rect - 1:
                    return True
        return False