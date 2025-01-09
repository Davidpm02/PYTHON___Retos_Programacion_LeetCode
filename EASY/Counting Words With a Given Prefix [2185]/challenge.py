"""
DESCRIPTION:

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length, pref.length <= 100
    words[i] and pref consist of lowercase English letters.

"""

from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        """
        Verifica el número de palabras en una lista recibida como 
        parámetro que tienen como prefijo a la cadena 'pref', también
        recibida como parámetro.

        params:
            words (List[str])
            pref (str)
        
        returns.
            int
        """

        def isPrefix(word: str) -> bool:

            """
            Se encarga de verificar si la cadena global 'pref' es
            prefijo de la cadena recibida como parámetro.

            params:
                word (str)

            returns:
                bool
            """

            try:
                assert (word.startswith(pref))
                return True
            except AssertionError:
                return False
        
        return sum(map(isPrefix, words))