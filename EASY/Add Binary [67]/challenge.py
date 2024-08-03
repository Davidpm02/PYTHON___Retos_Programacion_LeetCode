"""
DESCRIPTION

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

  Input: a = "11", b = "1"
  Output: "100"

Example 2:

  Input: a = "1010", b = "1011"
  Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.


"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        """
            Summary:
                Método de la clase Solution encargado de procesar dos cadenas de texto que representan 
                números en binario.
                Tras el procesamiento, el método se encarga de hallar la suma de estos números, y retornarla
                en forma de cadena en código binario.    
            Args:
                a, b -- Cadenas de texto que contienen un valor numérico en código binario
            Returns:
                binary_sum -- Cadena de texto que contiene la suma de los parámetros a, b en código binario.
        """

        # Comienzo casteando las cadenas de texto a enteros
        int_a = int(a, 2)  # Base 2 para procesamiento como binario
        int_b = int(b, 2)

        # Opero la suma de los parámetros a, b
        binary_sum = bin(int_a + int_b)[2:]
        return binary_sum


if __name__ == "__main__":
    
    # Ejemplo de interacción con el método '.addBinary()'
    a = "11"
    b = "1"

    sol = Solution()
    binary_sum = sol.addBinary(a, b) 