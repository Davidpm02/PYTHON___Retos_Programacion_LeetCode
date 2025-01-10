"""
DESCRIPTION:

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

 

Constraints:

    1 <= words1.length, words2.length <= 104
    1 <= words1[i].length, words2[i].length <= 10
    words1[i] and words2[i] consist only of lowercase English letters.
    All the strings of words1 are unique.

"""

from typing import List

from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        """
        Se encarga de analizar el total de cadenas que pueden formarse
        a partir de las subcadenas del parámetro 'words2'.

        La función retorna una lista con el total de palabras que cumplen
        esta condición.

        params:
            words1 (List[str])
            words2 (List[str])

        returns:
            List[str]
        """

        def isSubset(word:str) -> bool:

            """
            Se encarga de verificar si una cadena es subcadena de otra
            dada, teniendo en cuenta el número de repeticiones de cada
            uno de los caracteres que la componen.

            params:
                word (str)
            
            returns:
                bool
            """

            chars_in_word_counter = Counter(word)

            try:
                for char, reps in chars_in_universal_string.items():
                    assert (chars_in_word_counter[char] >= reps)
                return True
            except AssertionError:
                return False
        
        # Defino un contador que mapee el número de apariciones de cada
        # caracter en una cadena universal
        for idx, string in enumerate(words2):
            if (idx == 0):
                chars_in_universal_string = Counter(string)
            else:
                chars_in_new_substring = Counter(string)
                chars_in_universal_string = chars_in_universal_string | chars_in_new_substring
        
        # Valido las cadenas universales de la lista 'words1'
        results = list(map(isSubset, words1))
        return [words1[idx] for idx, result in enumerate(results) if (result == True)]