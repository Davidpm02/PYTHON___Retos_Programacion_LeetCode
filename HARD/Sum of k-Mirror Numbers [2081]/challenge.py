"""
DESCRIPTION:

A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

 

Example 1:

Input: k = 2, n = 5
Output: 25
Explanation:
The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
  base-10    base-2
    1          1
    3          11
    5          101
    7          111
    9          1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
Example 2:

Input: k = 3, n = 7
Output: 499
Explanation:
The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
  base-10    base-3
    1          1
    2          2
    4          11
    8          22
    121        11111
    151        12121
    212        21212
Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
Example 3:

Input: k = 7, n = 17
Output: 20379000
Explanation: The 17 smallest 7-mirror numbers are:
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
 

Constraints:

2 <= k <= 9
1 <= n <= 30

"""

from typing import List

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """
        Devuelve la suma de los n primeros números que son palíndromos
        en base-10 y en base-k.
        """
        def to_base_k(num: int) -> str:
            # Convierto el número entero `num` a su representación en base `k`
            if num == 0:
                return "0"
            digits = []
            temp = num
            while temp > 0:
                digits.append(str(temp % k))
                temp //= k
            return ''.join(reversed(digits))

        def is_palindrome(s: str) -> bool:
            # Compruebo si la cadena `s` es igual a su reverso
            return s == s[::-1]

        def generate_palindromes(length: int) -> List[int]:
            """
            Genera todos los palíndromos de longitud exacta `length` en base-10.
            """
            pals: List[int] = []
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for half in range(start, end):
                half_str = str(half)
                if length % 2 == 0:
                    pal_str = half_str + half_str[::-1]
                else:
                    pal_str = half_str + half_str[-2::-1]
                pals.append(int(pal_str))
            return pals

        found = []  # Almaceno los k-mirror encontrados
        length = 1
        # Genero palíndromos de longitud creciente hasta tener n
        while len(found) < n:
            for pal in generate_palindromes(length):
                base_k_repr = to_base_k(pal)
                if is_palindrome(base_k_repr):
                    found.append(pal)
                    if len(found) == n:
                        break
            length += 1

        # Retorno la suma de los n primeros k-mirror
        return sum(found)
