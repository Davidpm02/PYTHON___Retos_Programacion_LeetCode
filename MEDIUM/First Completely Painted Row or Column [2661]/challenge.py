"""
DESCRIPTION:

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
 

Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.

"""

from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        """
        Se encarga de hallar el primer índice del parámetro 'arr'
        cuyo elemento en 'mat' es el primero el último en ser pintado,
        dentro de una fila o columna de la misma matriz.

        params:
            arr (List[int])
            mat (List[List[int]])
        returns:
            int
        """

        # Variables de referencia.
        m = len(mat)
        n = len(mat[0])

        # Defino un diccionario que mapee las posiciones de cada elemento
        # dentro de la matriz
        num_positions_in_mat = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}

        # Defino dos listas que mapeen el número de celdas pintadas,
        # por filas y columnas
        painted_rows_in_mat = [0] * m
        painted_columns_in_mat = [0] * n
        
        # Recorro 'arr' y actualizo la lista de pintados,
        # verificando si se ha pintado alguna fila/columna.
        for idx, num_to_paint in enumerate(arr):
            # Obtengo los registros mapeados del número.
            row, column = num_positions_in_mat[num_to_paint]

            # Actualizo el índice de pintados
            painted_rows_in_mat[row] += 1
            painted_columns_in_mat[column] += 1

            # Verifico si existe alguna línea o columna pintada
            if (painted_rows_in_mat[row] == n) or (painted_columns_in_mat[column] == m):
                return idx
            