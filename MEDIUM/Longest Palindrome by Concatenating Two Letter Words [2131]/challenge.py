"""
DESCRIPTION:

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.

"""

from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        """
        Se encarga de validar la longitud máxima de todos los palíndromos
        que puedan formarse a partir del listado de palabras recibido
        como argumento.

        Las palabras contenidas en el listado recibido también se tienen
        en cuenta para el resultado final.

        params:
            words (List[str])

        returns:
            int

        """

        count = Counter(words)
        max_len = 0
        central_used = False  # Indica si ya usamos un palíndromo como centro

        for word in list(count.keys()):
            rev = word[::-1]
            if word == rev:
                # Si la palabra es palíndroma (ej: "aa", "bb"), podemos usar pares
                pairs = count[word] // 2
                max_len += pairs * 4  # cada par aporta 4 caracteres
                count[word] -= pairs * 2
                # Si queda una, la podemos usar en el centro
                if not central_used and count[word] > 0:
                    max_len += 2
                    central_used = True
            elif rev in count:
                # Si existe su reverso, usamos los pares mínimos entre ambas
                pairs = min(count[word], count[rev])
                max_len += pairs * 4
                count[word] -= pairs
                count[rev] -= pairs

        return max_len