"""
DESCRIPTION:

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

  Input: s = "abab"
  Output: true
  Explanation: It is the substring "ab" twice.

Example 2:

  Input: s = "aba"
  Output: false

Example 3:

  Input: s = "abcabcabcabc"
  Output: true
  Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

 

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.


"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        """
        Summary:
            Método de la clase Solution encargado de verificar
            si una cadena dada puede ser formada a partir de 
            la repetición de una subcadena presente en ella.
        Args:
            s (str) -- Cadena de texto a evaluar.
        Returns:
            bool
        """

        if len(s) == 1:
            return False

        substring_array = []

        for char in s:
            if char not in substring_array:
                substring_array.append(char)
            else:
                break
        
        # Formamos la subcadena
        substring = ''.join(substring_array)
        times_substring = len(s) // len(substring)

        if (substring * times_substring) == s:
            return True
        else:
            return False
