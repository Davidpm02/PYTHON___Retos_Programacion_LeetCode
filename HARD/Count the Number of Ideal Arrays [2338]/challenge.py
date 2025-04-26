"""
DESCRIPTION:

You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays): 
   - With no other distinct values (1 array): [1,1,1,1,1] 
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
 

Constraints:

2 <= n <= 104
1 <= maxValue <= 104

"""

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        
        """
        Devuelve el número de arrays ideales distintos de longitud n con
        valores de 1 a maxValue.
        Un array es ideal si cada elemento es divisible por el anterior.
        
        params: 
            n (int)
            maxValue (int)
        
        returns:
            Número de arrays ideales distintos módulo 10^9 + 7
        """
        
        MOD = 10**9 + 7
        MAX_N = n + 1
        MAX_L = 15  # Como 2^14 > 10^4, no hay secuencias de más de 14 elementos únicos

        # Precalcular combinaciones C(n-1, k) hasta k = MAX_L
        fact = [1] * (MAX_N + MAX_L)
        inv_fact = [1] * (MAX_N + MAX_L)
        for i in range(1, len(fact)):
            fact[i] = (fact[i - 1] * i) % MOD
        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
        for i in reversed(range(len(inv_fact) - 1)):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        def comb(a, b):
            if a < b or b < 0:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        # dp[i][l] = cuántas secuencias multiplicativas de longitud l terminan en i
        dp = [[0] * MAX_L for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][0] = 1  # longitud 1 (una sola elección)

        for l in range(1, MAX_L):
            for i in range(1, maxValue + 1):
                for j in range(2 * i, maxValue + 1, i):
                    dp[j][l] = (dp[j][l] + dp[i][l - 1]) % MOD

        # Combinar cada secuencia multiplicativa válida con las combinaciones posibles
        res = 0
        for i in range(1, maxValue + 1):
            for l in range(MAX_L):
                if dp[i][l] == 0:
                    continue
                # Número de formas de colocar l "aumentos" en n posiciones (estrellas y barras)
                res = (res + dp[i][l] * comb(n - 1, l)) % MOD

        return res