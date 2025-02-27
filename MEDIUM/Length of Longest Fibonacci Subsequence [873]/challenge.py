"""
DESCRIPTION:

A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

 

Constraints:

    3 <= arr.length <= 1000
    1 <= arr[i] < arr[i + 1] <= 109

"""

from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        """
        Se encarga de hallar la longitud de la subsecuencia más larga
        a formar con los elementos del array 'arr' recibido como parámetro.

        Para que una subsecuencia sea considerada válida, deberá tener,
        al menos, 3 elementos dentro de ella (para que se cumpla la
        condición de similitud con Fibonacci). De lo contrario, se 
        retornará 0.

        params:
            arr (List[int])
        
        returns:
            int
        """

        # Creo un diccionario para mapear cada valor a su índice, lo que me permite búsquedas en O(1)
        index = {x: i for i, x in enumerate(arr)}
        # Inicializo un diccionario dp para almacenar la longitud de la subsecuencia Fibonacci-like 
        # que termina en el par (j, i). Por defecto, la longitud mínima es 2.
        dp = {}
        max_length = 0  # Variable para llevar la cuenta de la máxima longitud encontrada
        
        # Recorro todos los pares (j, i) donde j < i
        for i in range(len(arr)):
            for j in range(i):
                # Calculo el valor que debería tener el elemento anterior para cumplir la propiedad Fibonacci
                k_val = arr[i] - arr[j]
                # Verifico que k_val exista en el array y que su índice sea menor que j
                if k_val in index and index[k_val] < j:
                    k = index[k_val]
                    # Extiendo la subsecuencia existente; si no existe, asumo que la longitud previa es 2
                    dp[j, i] = dp.get((k, j), 2) + 1
                    # Actualizo la longitud máxima
                    max_length = max(max_length, dp[j, i])
                else:
                    # Si no se cumple la condición, inicializo la longitud para el par (j, i) en 2
                    dp[j, i] = 2
        
        # Retorno el máximo si se encontró una subsecuencia de longitud al menos 3, sino retorno 0
        return max_length if max_length >= 3 else 0