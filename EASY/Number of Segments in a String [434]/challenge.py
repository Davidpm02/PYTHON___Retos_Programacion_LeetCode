"""
DESCRIPTION:

Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:

  Input: s = "Hello, my name is John"
  Output: 5
  Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:

  Input: s = "Hello"
  Output: 1

 

Constraints:

    0 <= s.length <= 300
    s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
    The only space character in s is ' '.

"""

from collections import Counter

class Solution:
    def countSegments(self, s: str) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de retornar
            el número de 'segmentos' contenidos en una cadena de
            texto.
            Los segmentos se delimitan por espacios (' ') dentro
            de la cadena de texto.
        Args:
            s (str) -- Cadena de texto a evaluar.
        Returns:
            int -- Número de segmentos contenidos en 's'.
        """
        
        chars_counter = Counter(s.split())

        if (len(chars_counter.keys()) == 1) and (" " in chars_counter.keys()): 
            return 0
        else:
            segments_in_s = 0
            for key, value in chars_counter.items():
                if key != ' ':
                    segments_in_s += value
            return segments_in_s