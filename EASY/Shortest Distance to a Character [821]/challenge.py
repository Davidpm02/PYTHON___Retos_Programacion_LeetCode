"""
DESCRIPTION:

Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

 

Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]

 

Constraints:

    1 <= s.length <= 104
    s[i] and c are lowercase English letters.
    It is guaranteed that c occurs at least once in s.

"""

from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        """
        Se encarga de hallar la distancia más cercana a un caracter
        dado ('c'), para cada uno de los caracteres que componen 's'.
        
        La función retorna una lista de enteros, cuya longitud es igual
        a la longitud de la cadena 's', y dónde cada entero representa
        la distancia entre el carácter y 'c'.
        
        params:
            s (str)
            c (str)

        returns:
            List[int]
        """

        # Lista vacía para almacenar las distancias entre caracteres.
        distances_to_c = []

        # Lista de índices donde se encuentra 'c' en 's'
        idxs_of_c_in_s = [idx for idx, char in enumerate(s) if (char == c)]        
   
        # Recorro la cadena 's' y actualizo la lista de distancias.
        for idx, char in enumerate(s):
            idx_closest_c = sorted([abs(num - idx) for num in idxs_of_c_in_s])[0]
            distances_to_c.append(idx_closest_c)
       
        return distances_to_c
