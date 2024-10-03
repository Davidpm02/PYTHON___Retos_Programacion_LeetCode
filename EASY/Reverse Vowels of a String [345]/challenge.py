"""
DESCRIPTION:

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

  Input: s = "IceCreAm"
  Output: "AceCreIm
  Explanation:
    The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

  Input: s = "leetcode"
  Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        """
        Summary:
            Método de la clase Solution encargado de procesar
            una cadena de texto, y retornar una nueva cadena 
            con todas las vocales invertidas.
        Args:
            s (str) -- Cadena de texto a procesar por el
            método.
        Returns:
            str -- Nueva cadena de texto con las vocales 
            invertidas.
        """

        # Arrays de referencia
        vowels = ['a', 'e', 'i', 'o', 'u']
        upper_vowels = [vowel.upper() for vowel in vowels]

        vowels_in_s = []
        for char in s:
            if (char in vowels) or (char in upper_vowels):
                vowels_in_s.append(char)
        reversed_vowels_in_s = vowels_in_s[::-1]

        # Diccionario de mapeo de vocales en s
        vowels_dict = dict()
        vowels_parsed = 0
        for idx, char in enumerate(s):
            if (char in vowels) or (char in upper_vowels):
                vowels_dict[str(idx)] = (vowels_in_s[vowels_parsed],
                                         reversed_vowels_in_s[vowels_parsed])
                vowels_parsed += 1
            else:
                continue
        
        new_s_array = []  # Array con la nueva palabra
        for idx, value in enumerate(s):
            if (value not in vowels_in_s):
                new_s_array.append(value)
            else:
                new_s_array.append(vowels_dict[str(idx)][-1])
        return "".join(new_s_array)