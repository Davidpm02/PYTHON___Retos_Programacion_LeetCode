"""
DESCRIPTION:

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.

 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false

 

Constraints:

    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.

"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        """
        Verifica si la cadena 's' puede llegar a convertirse en la
        cadena 'goal' tras aplicar un cierto numero de rotaciones.

        Cada rotación consiste en desplazar el caracter situado más
        a la derecha de la cadena, a su última posición.

        params:
            s (str) -- Cadena a evaluar.
            goal (str) -- Cadena objetivo.
        
        returns:
            bool
        """

        orig_s = s[:]
       
        while (s != goal):
            chars_in_s = [char for char in s]
            chars_in_s_after_shift = [char for char in chars_in_s[1:]]

            # Aplicamos el shift de los caracteres iniciales y finales
            chars_in_s_after_shift.append(chars_in_s[0])

            s = "".join(chars_in_s_after_shift)
            if (s == orig_s):
                return False
            continue
        return True