"""
DESCRIPTION:

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

  Input: s = "race a car"
  Output: false
  Explanation: "raceacar" is not a palindrome.

Example 3:

  Input: s = " "
  Output: true
  Explanation: s is an empty string "" after removing non-alphanumeric characters.
  Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
            Summary: 
                Método de la clase Solution encargado de verificar si
                una cadena es un palíndromo o no.
                La función analiza el parámetro 's' recibido y retorna
                un booleano con el resultado correspondiente.
            Args:
                s (str) -- Cadena a procesar.
            Returns:
                bool -- Booleano cuyo valor lógico representa el 
                        resultado obtenido.
        """

        # Normalizo todos los caracteres de la cadena
        s_array = [char.lower() for char in s if char.isalnum()]
        s_normalized = "".join(s_array)

        # Valido que la cadena sea un palíndromo
        s_normalized_reversed = s_normalized[::-1]
        if s_normalized_reversed == s_normalized:
            return True
        else:
            return False

        