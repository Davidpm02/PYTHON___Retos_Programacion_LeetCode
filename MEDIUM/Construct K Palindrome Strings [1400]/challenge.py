"""
DESCRIPTION:

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105

"""

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        """
        Se encarga de verificar si es posible construir un número
        'k' de subcadenas palíndromas que utilicen todos los 
        caracteres de la cadena 's'.

        params:
            s (str)
            k (int)
        
        returns:
            bool
        """

        # Comprobación inicial de la posibilidad de crear palíndromos.
        if (len(s) == k):
            return True
        elif (len(s) < k):
            return False
        else:
            chars_in_s_counter = Counter(s)
            try:
                odds_chars = 0
                for char, reps in chars_in_s_counter.items():
                    if ((reps % 2) != 0):
                        odds_chars += 1
                assert (odds_chars <= k)
                return True
            except AssertionError:
                return False