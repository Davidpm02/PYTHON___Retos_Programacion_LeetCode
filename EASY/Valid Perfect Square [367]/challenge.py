"""
DESCRIPTION:

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

  Input: num = 16
  Output: true
  Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:

  Input: num = 14
  Output: false
  Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

 

Constraints:

    1 <= num <= 231 - 1

"""

from math import sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    
        """
        Summary:
            Método de la clase Solution encargado de comprobar si
            un entero dado es un cuadrado perfecto.
            Se define como cuadrado perfecto a aquel entero que es
            cuadrado de otro entero.
        Args:
            num -- Entero a evaluar como cuadrado perfecto.
        Returns:
            bool
        """

        try:
            primitive_num = sqrt(num)
            assert str(primitive_num)[-1] == "0"
            return True
        except:
            return False
