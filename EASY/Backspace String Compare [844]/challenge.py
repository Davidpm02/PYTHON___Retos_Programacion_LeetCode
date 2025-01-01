"""
DESCRIPTION:

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

 

Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        """
        Se encarga de verificar si dos cadenas de texto mantienen
        el mismo contenido tras ser escritas desde cero en editores
        de texto vacíos.

        Las cadenas de texto contienen unicamente caracteres del
        alfabeto Inglés, en mayúsculas o minúsculas, y pueden 
        contener el carácter '#', el cual se procesa como un
        retroceso (Backspace) en el teclado.
        
        params:
            s (str)
            t (str)
        
        returns:
            bool
        """

        # Convierto a listas las dos cadenas de texto recibidas
        # como parámetro.
        chars_in_s = [char for char in s]
        chars_in_t = [char for char in t]

        # Procesamos el contenido de las listas, y las comparamos entre
        # ellas para retornar un resultado.
        while True:
            for idx, char in enumerate(chars_in_s):
                if ((idx == 0) and (char == "#")):
                    chars_in_s.pop(idx)
                    break
                if (char == "#"):
                    chars_in_s.pop(idx - 1)
                    chars_in_s.pop(idx - 1)
                    break
            else:
                break
        
        while True:
            for idx, char in enumerate(chars_in_t):
                if ((idx == 0) and (char == "#")):
                    chars_in_t.pop(idx)
                    break
                if (char == "#"):
                    chars_in_t.pop(idx - 1)
                    chars_in_t.pop(idx - 1)
                    break
            else:
                break

        print("Contenido final chars_in_s:", chars_in_s)
        print("Contenido final chars_in_t:", chars_in_t)
        return True if ("".join(chars_in_s) == ("".join(chars_in_t))) else False