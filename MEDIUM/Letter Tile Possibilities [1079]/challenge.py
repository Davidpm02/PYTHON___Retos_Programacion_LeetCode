"""
DESCRIPTION:

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

Input: tiles = "AAABBC"
Output: 188

Example 3:

Input: tiles = "V"
Output: 1

 

Constraints:

    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.

"""

from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        """
        Se encarga de hallar el número total de posibilidades que
        pueden formarse a partir de los caracteres de las baldosas
        en el parámetro 'tiles'.

        params:
            tiles (str)
        
        returns:
            int
        """

        # Conjunto de todas las permutaciones posibles con los
        # caracteres de la cadena.
        seen = set()

        # Se itera sobre las longitudes posibles de las permutaciones,
        # y se añaden todas las combinaciones posibles al conjunto.
        for i in range(1, len(tiles) + 1):
            for perm in permutations(tiles, i):
                seen.add(perm)
        return len(seen)

        # El uso de permutaciones es una de las mejores estrategias 
        # posibles si tenemos en cuenta las restricciones del ejercicio.