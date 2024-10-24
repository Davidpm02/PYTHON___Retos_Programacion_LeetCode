"""
DESCRIPTION:

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:

  Input: n = 5
  Output: 2
  Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:

  Input: n = 8
  Output: 3
  Explanation: Because the 4th row is incomplete, we return 3.

 

Constraints:

    1 <= n <= 231 - 1

"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de calcular
            el número de escalones que se completan con 'n'
            monedas, asumiendo que el último escalón siempre
            debe estar incompleto.
        Args:
            n (int) -- Número de monedas de las que se disponen
            para construir la escalera.

        Returns:
            int -- Número de escalones completos con las monedas
            disponibles.
        """

        completed_rows = 0
        coins_in_stairs = []
        while True:
            if len(coins_in_stairs) == 0:
                coins_in_stairs.append(1)
                completed_rows += 1
                n -= 1
            
            try:
                # Aseguramos que tenemos suficientes monedas para
                # completar el siguiente escalon.
                assert coins_in_stairs[-1] < n
                coins_in_stairs.append(coins_in_stairs[-1] + 1)
                completed_rows += 1
                n -= coins_in_stairs[-1]
            except AssertionError:
                return completed_rows