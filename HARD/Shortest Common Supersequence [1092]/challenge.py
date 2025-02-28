"""
DESCRIPTION:

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of lowercase English letters.

"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        """
        Se encarga de hallar la subcadena común más corta posible,
        a partir de las cadenas 'str1' y 'str2' recibidas como 
        parámetro.

        params:
            str1 (str)
            str2 (str)
        
        returns:
            str
        """

        # Paso 1: Encontrar la subsecuencia común más larga (LCS)
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Construimos la matriz de LCS usando programación dinámica
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Paso 2: Construir la supersecuencia más corta usando la LCS
        i, j = m, n
        scs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # Coincidencia en el LCS
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Nos movemos hacia arriba
                scs.append(str1[i - 1])
                i -= 1
            else:  # Nos movemos hacia la izquierda
                scs.append(str2[j - 1])
                j -= 1

        # Agregar caracteres restantes de str1 o str2
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        # La respuesta está en orden inverso
        return ''.join(reversed(scs))