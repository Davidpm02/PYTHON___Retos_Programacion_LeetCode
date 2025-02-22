"""
DESCRIPTION:

A happy string is a string that:

    consists only of letters of the set ['a', 'b', 'c'].
    s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

 

Constraints:

    1 <= n <= 10
    1 <= k <= 100

"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        """
        Se encarga de hallar la k-gésima cadena considerada
        'Happy String' de entre todas las combinaciones posibles
        de cadenas con 'n' caracteres, ordenadas lexicográficamente.

        params:
            n (int)
            k (int)
        
        returns:
            str
        """

        # Calculo el total de cadenas happy posibles.
        total = 3 * (2 ** (n - 1)) if n > 0 else 0
        # Si k excede el número de cadenas posibles, retorno cadena vacía.
        if k > total:
            return ""
        
        result = []  # Aquí iré construyendo la cadena resultante.
        chars = ['a', 'b', 'c']  # Lista de caracteres en orden lexicográfico.
        
        # Recorro cada posición de la cadena.
        for i in range(n):
            # Para cada posición, pruebo cada carácter en orden lexicográfico.
            for c in chars:
                # Si no es la primera posición, me aseguro de no repetir el carácter anterior.
                if i > 0 and c == result[-1]:
                    continue
                
                # Calculo cuántas cadenas se pueden formar si escojo 'c' en la posición actual.
                # Para la última posición, solo hay 1 opción.
                count = 2 ** (n - i - 1) if i < n - 1 else 1
                
                # Si k es mayor que las combinaciones posibles con 'c' en esta posición,
                # entonces descarto esas combinaciones y resto ese conteo a k.
                if k > count:
                    k -= count
                else:
                    # Si k se encuentra dentro del rango de las combinaciones posibles,
                    # elijo 'c' para esta posición y avanzo a la siguiente.
                    result.append(c)
                    break
                    
        # Retorno la cadena construida.
        return "".join(result)