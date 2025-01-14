"""
DESCRIPTION:

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

Example 2:

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

 

Constraints:

    1 <= A.length == B.length == n <= 50
    1 <= A[i], B[i] <= n
    It is guaranteed that A and B are both a permutation of n integers.

"""

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        """
        Se encarga de generar una lista de longitud n == len(A) == len(B)
        cuyos elementos representen el conjunto de enteros comunes en
        'A' y 'B' en función del índice del entero dentro de la lista
        resultado.

        params:
            A (List[int])
            B (List[int])
        
        returns:
            List[int]
        """

        # Longitud de las listas de enteros.
        n = len(A)

        # Lista con el número de elementos por índice comunes en
        # 'A' y 'B'.
        common_integers_prefix = []

        # Actualizo la lista con la suma de elementos de la intersección de los
        # conjuntos "A[:i + 1]" y "B[:i + 1]".
        for i in range(n):
            common_integers_prefix.append(len(set(A[:i + 1]) & set(B[:i + 1])))
        return common_integers_prefix