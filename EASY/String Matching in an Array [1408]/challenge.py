"""
DESCRIPTION:

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 30
    words[i] contains only lowercase English letters.
    All the strings of words are unique.

"""

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        """
        Se encarga de hallar todas aquellas cadenas contenidas en una
        lista que pueden encontrarse como subcadenas de otras palabras
        en la misma lista.
        La función retorna una nueva lista con todas las cadenas
        consideradas también subcadenas de otras.

        params:
            words (List[str])
        
        returns:
            List[str]
        """

        # Conjunto con palabras que son subcadenas de otras.
        substrings_set = set()

        # Recorro la lista 'words' y busco las posibles
        # subcadenas.
        n = len(words)
        for i in range(n):
            for idx, word in enumerate(words):
                if (words[i] == word):
                    continue
                else:
                    if (word in words[i]):
                        substrings_set.add(word)
        return list(substrings_set)