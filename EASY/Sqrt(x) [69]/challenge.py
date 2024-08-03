"""
DESCRIPTION

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

Example 1:

  Input: x = 4
  Output: 2
  Explanation: The square root of 4 is 2, so we return 2.

Example 2:

  Input: x = 8
  Output: 2
  Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:   

    0 <= x <= 231 - 1
    
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        """
            Summary:
                Método de la clase Solution encargado de llevar a cabo la operación de raíz cuadrada
                del entero 'x' recibido como parámetro.    
            Args:
                x (int) -- Entero sobre el que se quiere obtener la raíz cuadrada.
            
            Returns:
                sqrt_x (int) -- Entero que representa la raíz cuadrada del parámetro 'x'.
            
        """

        # Hallo la raíz de 'x' mediante la resta consecutiva de números impares
        sqrt_x = 0
        operando = 1
        for _ in range(0, x):
            if x == 0:
                return sqrt_x
            elif x < operando:
                return sqrt_x
            x -= operando
            operando += 2  # Actualizo el operando al siguiente número impar
            sqrt_x += 1
        return sqrt_x
    
    
if __name__ == "__main__":
    
    # Ejemplo de interacción con el método '.mySqrt()'
    x = 4

    sol = Solution()
    sqrt_x = sol.mySqrt(x)