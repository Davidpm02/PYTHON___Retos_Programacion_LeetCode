"""
DESCRIPTION:

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

 

Constraints:

    1 <= s.length, goal.length <= 2 * 104
    s and goal consist of lowercase letters.

"""

from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        """
        Se encarga de verificar si dos cadenas de texto recibidas como
        parámetro se consideran 'buddy strings'.

        Según su definición, dos cadenas reciben esta cualidad si, al
        intercambiar dos caracteres en una de ellas, ambas mantienen
        el mismo contenido.

        params:
            s (str)
            goal (str)
        
        returns:
            bool
        """

        # Listas de caracteres diferentes en la cadena principal y sus
        # índices con respecto a la cadena objetivo.
        different_chars_in_s = []
        idxs_of_different_chars_in_s = []

        if (len(s) != len(goal)):
            return False

        # Actualizo el contador en función del contenido de la cadena.
        for idx, char in enumerate(s):
            try:
                assert (char == goal[idx])
            except AssertionError:
                different_chars_in_s.append(char)
                idxs_of_different_chars_in_s.append(idx)
        
        if (len(different_chars_in_s) == 2):
            # Analizamos si al intercambiar los caracteres, la cadena es
            # igual a la cadena objetivo.
            chars_in_s = [char for char in s]
            chars_in_s[idxs_of_different_chars_in_s[0]] = different_chars_in_s[1]
            chars_in_s[idxs_of_different_chars_in_s[1]] = different_chars_in_s[0]

            return True if ("".join(chars_in_s) == goal) else False
        if (len(different_chars_in_s) == 0):
            # Defino un contador para los caracteres de ambas cadenas
            chars_in_s_counter = Counter(s)
            chars_in_goal_counter = Counter(goal)

            # Busco entre los caracteres de las cadenas y reviso si alguno
            # se repite, al menos, en dos ocasiones
            for char, reps in chars_in_s_counter.items():
                if ((reps >= 2) and (chars_in_goal_counter[char] == reps)):
                    return True
        return False
        