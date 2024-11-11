"""
DESCRIPTION:

Given an integer num, return a string of its base 7 representation.

Example 1:

  Input: num = 100
  Output: "202"

Example 2:

  Input: num = -7
  Output: "-10"

 

Constraints:

    -107 <= num <= 107

"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        
        """
        Summary:
            Método de la clase Solution encargado de obtener la representación
            en base 7 de un entero dado.
        Args:
            num (int) -- Número en base decimal.
        Returns:
            str -- Cadena con la representación en base 7 del entero recibido
            como parámetro.
        """

        # Validación inicial del parámetro 'num'
        if (num == 0):
            return '0'

        quotients_array = []
        original_num = num
        while True:
            num = abs(num)
            if num == 0:
                if (original_num < 0):
                    quotients_array.append('-') # El número original es negativo
                    return "".join(quotients_array[::-1])
                return "".join(quotients_array[::-1])
            quotient = num % 7
            num = num // 7
            quotients_array.append(str(quotient))