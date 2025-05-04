"""
DESCRIPTION:

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 10^4
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9

"""

from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        """
        Se encarga de hallar el número de parejas de domino
        equivalentes dentro de un array de fichas.

        Se tiene en cuenta que una ficha puede ser igual a otra
        si y solo si (a == c y b == d) o (a == d y b == c), en
        fichas dominoes[i] = [a, b], dominoes[j] = [c, d]

        params:
            dominoes (List[List[int]])
        
        returns:
            int
        """

        # Creo un diccionario para contar el número de apariciones de 
        # cada ficha normalizada
        count = defaultdict(int)

        # Inicializo una variable resultado
        result = 0

        # Itero sobre las fichas del array 'dominoes'
        for a, b in dominoes:
            # Genero una tupla con los elementos de la ficha ordenados
            key = tuple(sorted((a, b)))
            result += count[key]

            # Incremento el contador de apariciones para la ficha iterada
            count[key] += 1
        
        # Devolvemos el mayor número de parejas en 'dominoes'
        return result