"""
DESCRIPTION:

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

 

Constraints:

    3 <= s.length <= 105
    s consists of only lowercase English letters.

"""

from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        """
        Procesa el número de subcadenas de longitud = 3 que pueden
        considerarse palíndromos dentro de la cadena recibida como
        parámetro.

        params:
            s (str)
        
        returns:
            int
        """

        # Diccionario de mapeo de apariciones de cada caracter
        chars_counter = Counter(s)
  
        # Contador de palíndromos inicializado a 0.
        palindromes_counter = 0
        
        # Conjunto de caracteres que ya hemos evaluado.
        parsed_chars = set()

        for char, reps in chars_counter.items():
            # Conjunto de caracteres intermedios que ya hemos evaluado.
            parsed_letters_in_mid = set()
            try:
                assert (char not in parsed_chars)
                if (reps >= 3):
                    # Primer caso de palíndromo; 3 caracteres iguales.
                    palindromes_counter += 1
                
                if (reps >= 2):
                    # Segundo caso de palíndromo; incrementamos el valor
                    # por cada caracter diferente intermedio.
                    indexes_of_char_in_s = [idx for idx, c in enumerate(s) if (c == char)]
                    chars_in_substring = set(s[indexes_of_char_in_s[0] + 1: indexes_of_char_in_s[-1]])
                    if (char in chars_in_substring):
                        palindromes_counter += (len(chars_in_substring) - 1)
                    else:
                        palindromes_counter += len(chars_in_substring)
                parsed_chars.add(char)
            except AssertionError:
                continue
        return palindromes_counter