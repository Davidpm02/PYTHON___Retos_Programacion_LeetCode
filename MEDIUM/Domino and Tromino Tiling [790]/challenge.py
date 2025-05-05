"""
DESCRIPTION:

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 1000

"""

class Solution:
    def numTilings(self, n: int) -> int:
        
        """
        Calcula el número de formas de embaldosar un tablero de 2×n usando fichas de dominó (2×1)
        y trominós en forma de L. Las fichas pueden ser rotadas.
        
        params:
            n (int)

        returns:
            int
        """

        MOD = 10**9 + 7
        
        # Casos base para n pequeños
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # Inicializo la matriz de programación dinámica
        dp = [[0, 0, 0] for _ in range(n + 1)]
        
        # Establecezco los casos base
        dp[0][0] = 1  # Tablero vacío: 1 forma (no hacer nada)
        dp[1][0] = 1  # Tablero 2×1: 1 forma (un dominó vertical)
        dp[1][1] = 0  # No hay forma de dejar solo la celda superior cubierta
        dp[1][2] = 0  # No hay forma de dejar solo la celda inferior cubierta
        
        # Calculo para cada tamaño de tablero
        for i in range(2, n + 1):
            # Para completar la columna i:
            # 1. La columna i-1 estaba completa y añadimos un dominó horizontal
            # 2. La columna i-2 estaba completa y añadimos dos dominós verticales
            # 3. La columna i-1 tenía la celda superior faltante y añadimos un trominó
            # 4. La columna i-1 tenía la celda inferior faltante y añadimos un trominó
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]) % MOD
            
            # Para dejar la celda inferior de la columna i sin cubrir:
            # La columna i-1 estaba completa y añadimos un trominó
            # La columna i-2 tenía la celda inferior sin cubrir y añadimos un dominó vertical
            dp[i][1] = (dp[i-1][2] + dp[i-2][0]) % MOD
            
            # Para dejar la celda superior de la columna i sin cubrir:
            # La columna i-1 estaba completa y añadimos un trominó
            # La columna i-2 tenía la celda superior sin cubrir y añadimos un dominó vertical
            dp[i][2] = (dp[i-1][1] + dp[i-2][0]) % MOD
            
        return dp[n][0]