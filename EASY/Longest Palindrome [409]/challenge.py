"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

  Input: s = "abccccdd"
  Output: 7
  Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

  Input: s = "a"
  Output: 1
  Explanation: The longest palindrome that can be built is "a", whose length is 1.

 

Constraints:

    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

"""

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de obtener la
            máxima longitud del palíndromo que pueda ser formado
            con los caracteres que componen el parámetro 's'.
        Args:
            s -- Cadena con los caracteres a utilizar para la
            formación de palíndromos.
        Returns:
            int -- Longitud del palíndromo más grande a formar
            con los caracteres de 's'.
        """

        chars_counter = Counter(s)
        max_length_palindrome = 0

        print(chars_counter)

        if len(chars_counter.keys()) > 1:
            for key, value in chars_counter.items():
                if (value % 2) == 0:
                    max_length_palindrome += value
                elif (value % 3) == 0:
                    max_length_palindrome += (value - 1)
        
        else:
            for key, value in chars_counter.items():
                if (value % 2) == 0:
                    max_length_palindrome += value
                elif (value % 3) == 0:
                    max_length_palindrome += value

        if 1 in chars_counter.values():
            max_length_palindrome += 1

        return max_length_palindrome