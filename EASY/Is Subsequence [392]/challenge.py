"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

  Input: s = "abc", t = "ahbgdc"
  Output: true

Example 2:

  Input: s = "axc", t = "ahbgdc"
  Output: false

 

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        """
        Summary:
            Método de la clase Solution encargado de verificar que
            una cadena representa una subsecuencia de una cadena original.
        Args:
            s (str) -- Cadena original.
            t (str) -- Subsecuencia a validar por el método.
        Returns:
            bool

        """

        chars_in_s = [char for char in t if char in s]
        for idx, char in enumerate(chars_in_s):
            try:
                if chars_in_s[idx] != s[idx]:
                    chars_in_s.remove(char)
                    assert chars_in_s[idx + 1] == s[idx + 1]
            except AssertionError:
                continue
            except Exception:
                break
        return True if ("".join(chars_in_s) == s) else False