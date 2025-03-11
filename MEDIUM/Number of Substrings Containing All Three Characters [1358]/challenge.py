"""
DESCRIPTION:

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

 

Constraints:

    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.

"""

from itertools import permutations
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        """
        Se encarga de hallar el número de subcadenas que pueden
        formarse a partir de los caracteres de 's'.
        Para que una subcadena sea considerada válida, debe contener,
        al menos, una repetición de cada uno de los caracteres que 
        conforman 's'.

        params:
            s (str)
        
        returns:
            int
        """

        count = {'a': 0, 'b': 0, 'c': 0}  # Contador de caracteres
        left = 0  # Puntero izquierdo
        result = 0  # Contador de substrings válidas

        for right in range(len(s)):
            count[s[right]] += 1  # Agrego el nuevo carácter a la ventana

            # Verifico si la ventana es válida (tiene al menos un a, b y c)
            while all(count[char] > 0 for char in "abc"):
                result += len(s) - right  # Todas las substrings desde left hasta el final son válidas
                count[s[left]] -= 1  # Reduzco el conteo del carácter en left
                left += 1  # Muevo el puntero izquierdo

        return result