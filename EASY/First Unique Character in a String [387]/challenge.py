"""
DESCRIPTION:

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

  Input: s = "leetcode"
  Output: 0
  Explanation:

   The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

  Input: s = "loveleetcode"
  Output: 2

Example 3:

  Input: s = "aabb"
  Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.

"""

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de obtener
            el índice que ocupa el primer carácter único dentro
            del parámetro 's'.
        Args:
            s (str) -- Cadena de texto a evaluar por el método.
        Returns:
            int -- Índice que ocupa el primer carácter único en
            's'.
        """

        s_counter = Counter(s)
        unique_chars_array = [key for key, value in s_counter.items() if value == 1]

        if len(unique_chars_array) == 0:
            return -1
        else:
            return min([s.index(unique_char) for unique_char in unique_chars_array])