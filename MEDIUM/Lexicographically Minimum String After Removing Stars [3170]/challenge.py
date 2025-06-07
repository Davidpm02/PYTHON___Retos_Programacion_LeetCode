"""
DESCRIPTION:

You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.

"""

class Solution:
    def clearStars(self, s: str) -> str:
        """
        Elimina todos los '*' de la cadena s, borrando para cada '*' el carácter más pequeño a su izquierda.
        """
        # Inicializo estructuras
        result = []  
        deleted = []

        # Listas de posiciones para cada letra
        positions = [[] for _ in range(26)]

        for ch in s:
            if ch != '*':
                # Añado el carácter y lo marco como no eliminado
                result.append(ch)
                deleted.append(False)
                # Registro su posición
                idx = len(result) - 1
                positions[ord(ch) - ord('a')].append(idx)
            else:
                # Elimino el carácter más pequeño disponible
                for i in range(26):
                    if positions[i]:
                        pos = positions[i].pop()  # Cojo la última (más cercana al '*')
                        deleted[pos] = True      # Marco como eliminado
                        break
        
        # Construyo la cadena final
        return ''.join(ch for ch, del_flag in zip(result, deleted) if not del_flag)