"""
DESCRIPTION:

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

 

Example 1:

  Input: pattern = "abba", s = "dog cat cat dog"
  Output: true
  Explanation:

    The bijection can be established as:

        'a' maps to "dog".
        'b' maps to "cat".

Example 2:

  Input: pattern = "abba", s = "dog cat cat fish"
  Output: false

Example 3:

  Input: pattern = "aaaa", s = "dog cat cat dog"
  Output: false

 

Constraints:

    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        """
        Summary:
            Método de la clase Solution encargado de verificar si,
            dados un patrón y una cadena de texto, la disposición
            de la cadena respeta el patrón establecido.
        Args:
            pattern (str) -- Patrón sobre el que se evalua 's'.
            s (str) -- Cadena de texto a evaluar.
        Returns:
            bool
        """

        patterns_dict = {letter:'' for letter in pattern}
        words_in_s = s.split(' ')

        if len(pattern) != len(words_in_s):
            return False


        for idx, word in enumerate(words_in_s):
            try:
                if patterns_dict[pattern[idx]] == '':
                    assert word not in patterns_dict.values()
                    patterns_dict[pattern[idx]] = word
                else:
                    assert patterns_dict[pattern[idx]] == word
            except AssertionError:
                return False
        return True