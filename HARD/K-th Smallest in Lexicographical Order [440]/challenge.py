"""
DESCRIPTION:

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 10^9

"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        """
        Se encarga de hallar el enésimo entero más pequeño en términos
        lexicográficos comprendido en el rango [1, n].

        params:
            n (int)
            k (int)

        returns:
            int
        """

        curr = 1
        # Decremento k porque '1' es el primer número en orden lexicográfico
        k -= 1

        # Mientras no hayamos encontrado el k-ésimo elemento
        while k > 0:
            # Cuento cuántos números hay entre curr y curr+1 (rango de prefijos)
            count = self._count_nodes(curr, curr + 1, n)
            if count <= k:
                # Si todo este bloque de prefijos queda antes del que busco,
                # salto al siguiente hermano y reduzco k en la cantidad de nodos saltados
                curr += 1
                k -= count
            else:
                # Si el bloque contiene mi objetivo, desciendo un nivel en el trie (añadiendo un 0)
                curr *= 10
                k -= 1
        return curr

    def _count_nodes(self, prefix: int, next_prefix: int, n: int) -> int:
        """
        Calculo el número de enteros entre 'prefix' y 'next_prefix' (excluyendo este último),
        acotados por n. Este conteo se hace sumando la cantidad de números de cada nivel
        de profundidad del prefijo sin iterar uno a uno.
        """
        total = 0
        # Mientras el prefijo esté dentro del rango válido
        while prefix <= n:
            # En este nivel, todos los números desde prefix hasta min(n+1, next_prefix)-1
            total += min(n + 1, next_prefix) - prefix
            # Bajo un nivel más agregando un dígito (10x)
            prefix *= 10
            next_prefix *= 10
        return total