"""
DESCRIPTION:

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 105
    -109 <= matrix[i][j] <= 109

"""

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        """
        Retorna la traspuesta de una matriz recibida como parámetro.

        params:
            matrix (List[List[int]])
        
        returns:
            List[List[int]]
        """

        transposed_matrix = []
        rows_in_transposed_matrix = 0

        if (len(matrix) == 3):
            if (len(matrix[0]) == 1):
                row_transposed_matrix = [matrix[idx][0] for idx, item in enumerate(matrix)]
                transposed_matrix.append(row_transposed_matrix)
            elif (len(matrix[0]) == 2):
                for row in range(0, len(matrix[0])):
                    row_transposed_matrix = [matrix[idx][rows_in_transposed_matrix] for idx, item in enumerate(matrix)]
                    rows_in_transposed_matrix += 1
                    transposed_matrix.append(row_transposed_matrix)
            elif (len(matrix[0]) == 3):
                for row in range(0, len(matrix)):
                    row_transposed_matrix = [matrix[idx][rows_in_transposed_matrix] for idx, item in enumerate(matrix)]
                    rows_in_transposed_matrix += 1
                    transposed_matrix.append(row_transposed_matrix)
            else:
                for row in range(0, len(matrix[0])):
                    row_transposed_matrix = [matrix[idx][rows_in_transposed_matrix] for idx, item in enumerate(matrix)]
                    rows_in_transposed_matrix += 1
                    transposed_matrix.append(row_transposed_matrix)
        elif (len(matrix) == 1):
            for col in matrix[0]:
                row_transposed_matrix = [col]
                rows_in_transposed_matrix += 1
                transposed_matrix.append(row_transposed_matrix)
        elif (len(matrix) == 2):
            if (len(matrix[0]) == 1):
                row_transposed_matrix = [matrix[idx][0] for idx, item in enumerate(matrix)]
                transposed_matrix.append(row_transposed_matrix)
            elif (len(matrix[0]) == 2):
                for row in range(0, len(matrix)):
                    row_transposed_matrix = [matrix[idx][rows_in_transposed_matrix] for idx, item in enumerate(matrix)]
                    rows_in_transposed_matrix += 1
                    transposed_matrix.append(row_transposed_matrix)
            else:
                for row in range(0, len(matrix[0])):
                    row_transposed_matrix = [matrix[idx][rows_in_transposed_matrix] for idx, item in enumerate(matrix)]
                    rows_in_transposed_matrix += 1
                    transposed_matrix.append(row_transposed_matrix)
        else:
            if (len(matrix[0]) == 1):
                row_transposed_matrix = [matrix[idx][0] for idx, item in enumerate(matrix)]
                transposed_matrix.append(row_transposed_matrix)
            elif (len(matrix[0]) == 2):
                for row in range(0, 2):
                    row_transposed_matrix = [matrix[idx][rows_in_transposed_matrix] for idx, item in enumerate(matrix)]
                    rows_in_transposed_matrix += 1
                    transposed_matrix.append(row_transposed_matrix)
            else:
                for row in range(0, len(matrix[0])):
                    row_transposed_matrix = [matrix[idx][rows_in_transposed_matrix] for idx, item in enumerate(matrix)]
                    rows_in_transposed_matrix += 1
                    transposed_matrix.append(row_transposed_matrix)
        return transposed_matrix
