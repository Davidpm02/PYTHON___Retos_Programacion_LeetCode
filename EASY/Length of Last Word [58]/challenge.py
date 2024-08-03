"""
DESCRIPTION

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

  Input: s = "Hello World"
  Output: 5
  Explanation: The last word is "World" with length 5.

Example 2:

  Input: s = "   fly me   to   the moon  "
  Output: 4
  Explanation: The last word is "moon" with length 4.

Example 3:

  Input: s = "luffy is still joyboy"
  Output: 6
  Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.


"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        """
            Summary:
                Método de la clase Solution encargado de procesar una cadena de texto y retornar la longitud
                (int) de la última palabra presente en la cadena.
                Este método no toma en cuenta los caracteres ' ', por lo que el resultado retornado corresponde
                a una palabra real.

            Args:
                s -- Cadena de texto a procesar por el método.
            Returns:
                s_length -- Entero que representa la longitud de la última palabra presente en la cadena de texto.
        """

        # Comienzo invirtiendo la cadena de texto
        reversed_s = s[::-1]

        # Inicializo un contador, y lo actualizo por cada elemento distinto de ' ' al comienzo de la cadena
        s_length = 0
        for char in reversed_s:
            if char == ' ':
                if s_length > 0:
                    return s_length
                else:
                    continue
            else:
                s_length +=1
        
        return s_length
    
if __name__ == "__main__":
    
    # Ejemplo de interacción con el método '.lengthOfLastWord()'
    s = "Hello World"

    sol = Solution()
    s_length = sol.searchInsert(s)