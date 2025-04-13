"""
DESCRIPTION:

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303
 

Constraints:

1 <= n <= 1015

"""

class Solution:
    def countGoodNumbers(self, n: int) -> int:

        """
        Se encarga de hallar el total de 'números buenos' positivos
        que existen, con una longitud de 'n' dígitos.

        params:
            n (int)

        returns:
            int
        """
        
        MOD = 10**9 + 7
        
        # Calculamos cuántas posiciones pares e impares hay
        even_positions = (n + 1) // 2  # Posiciones pares
        odd_positions = n // 2         # Posiciones impares
  
        def power_mod(a, b, mod):
            if b == 0:
                return 1
            half = power_mod(a, b // 2, mod)
            result = (half * half) % mod
            if b % 2 == 1:
                result = (result * a) % mod
            return result
        
        even_count = power_mod(5, even_positions, MOD)
        odd_count = power_mod(4, odd_positions, MOD)
        
        # El resultado total es la multiplicación de ambos
        return (even_count * odd_count) % MOD
