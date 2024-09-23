"""
DESCRIPTION:

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

  Input: n = 6
  Output: true
  Explanation: 6 = 2 × 3

Example 2:

  Input: n = 1
  Output: true
  Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:

  Input: n = 14
  Output: false
  Explanation: 14 is not ugly since it includes the prime factor 7.

 

Constraints:

    -231 <= n <= 231 - 1

"""

class Solution:
    def isUgly(self, n: int) -> bool:
        
        """
        Summary:
            Método de la clase Solution encargado de validar si
            un entero dado es un 'ugly number' o 'número feo'.

            La función se asegura de validar que el número recibido
            como argumento tenga únicamente como factores primos los
            números [2, 3, 5].
        Args:
            n (int) -- Entero a validar por el método.
        Returns:
            bool
        """

        if (n == 1):
            return True
        elif (n == 0):
            return False
 

        while True:

            if n % 2 == 0:
                n = n / 2
                continue
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                if n == 1:
                    return True
                else:
                    return False

