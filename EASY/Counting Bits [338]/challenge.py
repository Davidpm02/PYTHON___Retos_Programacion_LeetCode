"""
DESCRIPTION:

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

  Input: n = 2
  Output: [0,1,1]
  Explanation:
  0 --> 0
  1 --> 1
  2 --> 10

Example 2:

  Input: n = 5
  Output: [0,1,1,2,1,2]
  Explanation:
  0 --> 0
  1 --> 1
  2 --> 10
  3 --> 11
  4 --> 100
  5 --> 101

 

Constraints:

    0 <= n <= 105

 

Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

"""
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        """
        Summary:
            Método de la clase Solution encargado de generar un array
            cuyos elementos corresponden cada uno a la cantidad de 1s
            que contiene la representación binaria de i.

            i corresponde a un índice cualquiera de una lista creada
            en el ámbito de la función a partir del parámetro de 
            entrada 'n'.
        Args:
            n (int) -- Entero a partir del cual se desea obtener la
            lista final.
        Returns:
            List[int]
        """

        n_array = [format(_, 'b') for _ in range(0, n + 1)]
        result_array = []
        for binary_representation in n_array:
            result_array.append(len(binary_representation.replace('0', '')))
        return result_array
