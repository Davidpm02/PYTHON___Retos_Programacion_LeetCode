"""
DESCRIPTION:

You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
Multiply your score by x.
Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [8,3,9,3,8], k = 2
Output: 81
Explanation: To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.
Example 2:

Input: nums = [19,12,14,6,10,18], k = 3
Output: 4788
Explanation: To get a score of 4788, we can apply the following operations: 
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.
 

Constraints:

1 <= nums.length == n <= 105
1 <= nums[i] <= 105
1 <= k <= min(n * (n + 1) / 2, 109)

"""

from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        """
        Se encarga de hallar la máxima puntuación posible (valor inicial
        = 0) tras llevar a cabo un número 'k' de operaciones con los enteros
        del array 'nums'.

        params:
            nums (List[int])
            k (int)

        returns:
            int
        """

        mod = 10**9 + 7
        
        # Paso 1: Precalcular el menor factor primo para cada número hasta max_val
        max_val = max(nums)
        spf = list(range(max_val + 1))  # spf[x] = x inicialmente
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:  # i es primo
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # Función para calcular el prime score de un número (cantidad de factores primos distintos)
        def prime_score(x: int) -> int:
            score = 0
            last = -1
            while x > 1:
                p = spf[x]
                if p != last:
                    score += 1
                    last = p
                x //= p
            return score
        
        n = len(nums)
        ps = [prime_score(x) for x in nums]  # Lista de prime scores
        
        # Paso 2: Para cada índice, calcular cuántos subarreglos tienen a nums[i] como el elegido.
        # Para ello, usaré dos pasadas con pilas.
        
        # Para el lado izquierdo: encontrar el índice previo con ps >= ps[i].
        left = [-1] * n
        stack = []  # almacenar índices
        for i in range(n):
            while stack and ps[stack[-1]] < ps[i]:
                # Si el elemento en la pila tiene menor prime score, sigue siendo válido
                stack.pop()
            # Si la pila no está vacía, el tope es el índice previo donde ps >= ps[i]
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Para el lado derecho: encontrar el índice siguiente con ps > ps[i]
        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and ps[stack[-1]] <= ps[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Calcular la cantidad de subarreglos en los que nums[i] es elegido
        contrib = []  # lista de tuplas (valor, frecuencia)
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            contrib.append((nums[i], count))
        
        # Paso 3: Ordenar en orden descendente por el valor, ya que queremos multiplicar por los mayores primero.
        contrib.sort(key=lambda x: x[0], reverse=True)
        
        # Paso 4: Calcular el producto final utilizando las operaciones disponibles (k)
        result = 1
        for value, count in contrib:
            if k <= 0:
                break
            use = min(k, count)
            # Multiplico result por value^use mod mod
            result = (result * pow(value, use, mod)) % mod
            k -= use
        
        return result