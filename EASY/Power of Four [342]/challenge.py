"""
DESCRIPTION:

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

  Input: n = 16
  Output: true

Example 2:

  Input: n = 5
  Output: false

Example 3:

  Input: n = 1
  Output: true

 

Constraints:

    -231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        """
        Summary:
            Método de la clase Solution encargado de validar un entero
            como potencia en base 4.
        Args:
            n (int) -- Entero a validar como potencia en base 4.
        Returns:
            bool
        """

        while True:
            try:
                if n == 1 or n == 4:
                    return True
                elif n < 4:
                    raise AssertionError
                n = n / 4
        
            except AssertionError as e:
                return False
        return False
