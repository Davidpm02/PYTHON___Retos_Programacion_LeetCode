"""
DESCRIPTION:

You are given three integers n, m, k. A good array arr of size n is defined as follows:

Each element in arr is in the inclusive range [1, m].
Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, m = 2, k = 1

Output: 4

Explanation:

There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
Hence, the answer is 4.
Example 2:

Input: n = 4, m = 2, k = 2

Output: 6

Explanation:

The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
Hence, the answer is 6.
Example 3:

Input: n = 5, m = 2, k = 0

Output: 2

Explanation:

The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
 

Constraints:

1 <= n <= 10^5
1 <= m <= 10^5
0 <= k <= n - 1

"""

class Solution:
    MOD = 10**9 + 7

    @staticmethod
    def mod_pow(a: int, e: int, mod: int) -> int:
        """Calculo rápido de a^e % mod usando exponenciación binaria."""
        result = 1
        base = a % mod
        # Itero sobre los bits de e
        while e > 0:
            if e & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            e >>= 1
        return result

    @classmethod
    def precompute_factorials(cls, n: int, mod: int):
        """
        Precomputo factoriales e inversos factoriales hasta n.
        Me servirá para calcular combinaciones en O(1).
        """
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        # Construyo factorizaciones crecientes
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        # Calculo inverso de fact[n] con exponenciación modular
        inv_fact[n] = cls.mod_pow(fact[n], mod - 2, mod)
        # Genero inversos factoriales decrecientes
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod
        return fact, inv_fact

    @staticmethod
    def comb(n: int, k: int, fact, inv_fact, mod: int) -> int:
        """C(n, k) = fact[n] * inv_fact[k] * inv_fact[n-k] % mod"""
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Devuelvo el número de arrays 'buenos' de longitud n,
        valores en [1, m] y con exactamente k repeticiones consecutivas.
        """
        # Caso rápido: si solo hay un valor posible
        if m == 1:
            # Solo válido cuando todas las transiciones son iguales
            return 1 if k == n - 1 else 0

        # Precomputo factoriales hasta n-1
        fact, inv_fact = self.precompute_factorials(n - 1, self.MOD)

        # Elección del primer elemento
        ways = m
        # Selección de posiciones de repeticiones
        ways = ways * self.comb(n - 1, k, fact, inv_fact, self.MOD) % self.MOD
        # Asigno los cambios de valor restantes
        ways = ways * self.mod_pow(m - 1, (n - 1) - k, self.MOD) % self.MOD
        return ways
