"""
DESCRIPTION:

Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= num1 < num2 <= right .
    Both num1 and num2 are 

    .
    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

 

Constraints:

    1 <= left <= right <= 106

"""

from typing import List
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """
        Encuentra el par de números primos en el rango [left, right]
        con la menor diferencia.

        params:
            left (int): Límite inferior del rango.
            right (int): Límite superior del rango.

        returns:
            List[int]
        """

        # 1. Genero números primos hasta `right` usando la Criba de Eratóstenes
        LIMIT = right + 1
        is_prime = [True] * LIMIT
        is_prime[0] = is_prime[1] = False  # 0 y 1 no son primos

        for num in range(2, int(math.sqrt(LIMIT)) + 1):
            if is_prime[num]:  
                for multiple in range(num * num, LIMIT, num):
                    is_prime[multiple] = False

        # 2. Extraigo los primos en el rango [left, right]
        primes = [num for num in range(left, right + 1) if is_prime[num]]

        if len(primes) < 2:
            return [-1, -1]

        # 3. Encuentro el par de primos más cercano
        min_gap = float('inf')
        best_pair = [-1, -1]

        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                best_pair = [primes[i], primes[i + 1]]

        return best_pair