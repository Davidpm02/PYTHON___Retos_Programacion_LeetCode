"""
DESCRIPTION:

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

  Input: ransomNote = "a", magazine = "b"
  Output: false

Example 2:

  Input: ransomNote = "aa", magazine = "ab"
  Output: false

Example 3:

  Input: ransomNote = "aa", magazine = "aab"
  Output: true

 

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

"""

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        """
        Summary:
            Método de la clase Solution encargado de verificar que una
            cadena puede ser formada con los caracteres contenidos en
            una segunda cadena.
            Para ofrecer un resultado, la función toma dos parámetros,
            'ransomNote' (cadena a validar) y 'magazine' (cadena que 
            debe tener los caracteres necesarios para formar 
            'ransomNote').
        Args:
            ransomNote (str) --
            magazine (str) -- 
        Returns:
            bool
        """

        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        try:
            for key, value in ransomNote_counter.items():
                assert value <= magazine_counter[key]
        except AssertionError:
            return False
        return True