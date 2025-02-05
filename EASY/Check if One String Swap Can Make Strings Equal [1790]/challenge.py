"""
DESCRIPTION:

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

 

Constraints:

    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.

"""

from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        """
        Se encarga de verificar si dos cadenas de texto pueden ser
        idénticas si aplicamos un cambio entre los caracteres de 
        dos índices (pueden ser el mismo índice) de una de las cadenas
        recibidas como parámetro.

        params:
            s1 (str)
            s2 (str)
        
        returns:
            bool
        """

        try:
            assert (Counter(s1) == Counter(s2))

            diff_chars = 0
            for idx, char in enumerate(s1):
                if (char != s2[idx]):
                    diff_chars += 1
            assert (diff_chars in [0, 2]) # 0 --> cadenas iguales
                                          # 2 --> dos caracteres distintos
            return True
        except AssertionError:
            return False
