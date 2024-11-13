"""
DESCRIPTION:

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.


Example 1:

  Input: num = 28
  Output: true
  Explanation: 28 = 1 + 2 + 4 + 7 + 14
  1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:

  Input: num = 7
  Output: false

 

Constraints:

    1 <= num <= 108

"""

from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        """
        Summary:
            Método de la clase Solution encargado de comprobar
            si un entero dado se considera como un 'número perfecto'.

            Un número se considera 'perfecto' si este es igual a la suma
            de todos sus divisores (excepto él mismo).
        Args:
            num (int) -- Entero a validar como 'número perfecto'.
        Returns:
            bool
        """

        # Lista con todos los divisores de 'num'
        if (num > 10e3):
            possible_num_divisors = [_ for _ in range(1, int(sqrt(num))) if ((num % _) == 0)]
            num_divisors = [num//_ for _ in possible_num_divisors if (_ != 1)]
            num_divisors.extend(possible_num_divisors)
        else:
            num_divisors = [_ for _ in range(1, num//2 + 1) if ((num % _) == 0)]
        return True if (sum(num_divisors) == num) else False