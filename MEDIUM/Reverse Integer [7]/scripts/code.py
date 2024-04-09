"""
DESCRIPTION:

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2e31, 2e31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

  Input: x = 123
  Output: 321


Example 2:

  Input: x = -123
  Output: -321


Example 3:

  Input: x = 120
  Output: 21
 

## Constraints:

  -231 <= x <= 231 - 1
"""

# IMPORTS ----

import unittest
from ..tests.tests import TestReverseFunction

class Solution:
    def reverse(self, x: int) -> int:
        
        """
          Summary:
              Método de la clase Solution encargado de 'invertir' la disposición de dígitos de un entero recibido
              como parámetro dentro del método.
           
          Args:
              x -- Entero que recibe la función.
              
          Returns:
              int -- Entero de 32 bits, que mantiene los dígitos del parámetro 'x', pero en disposición invertida.
        """
        # CONSTANTES
        MIN_VAL = -2**31
        MAX_VAL = 2**31 - 1
        

  
        if x not in range(MIN_VAL + 1, MAX_VAL + 1):
          return 0
        
        ## LÓGICA
        digits_array = [digit for digit in str(x) if digit != 0]
        if '-' in digits_array:
            reserved_integer = "".join(digits_array[:0:-1])
            reserved_integer = 0 - int(reserved_integer)
        else:
            reserved_integer = int("".join(digits_array[::-1]))
        
        # Me aseguro de que 'reserved_integer' sea un entero válido
        return reserved_integer if reserved_integer in range(MIN_VAL, MAX_VAL + 1) else 0
        
if __name__ == "__main__":
  
  unittest.TestReverseFunction()