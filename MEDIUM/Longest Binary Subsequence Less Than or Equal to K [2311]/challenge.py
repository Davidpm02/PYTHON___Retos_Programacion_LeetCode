"""
DESCRIPTION:

You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= k <= 10^9

"""

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        # Construyo la subsecuencia en forma de lista de caracteres
        subseq = []
        # Valor decimal actual de la subsecuencia
        value = 0
        
        for c in s:
            # 1) Añado el dígito (equivale a no borrarlo)
            subseq.append(c)
            # 2) Actualizo el valor: shift left + int(c)
            value = (value << 1) + (c == '1')
            
            # 3) Si ya me paso de k, tengo que "borrar" un dígito:
            #    siempre quito el primer '1' de subseq (mayor peso)
            if value > k:
                # Busco el índice del primer '1'
                idx = next((i for i, ch in enumerate(subseq) if ch == '1'), None)
                if idx is None:
                    # Si no hay '1', significa que solo llevo ceros y aun así
                    # value > k (imposible si k>=0), pero por seguridad:
                    subseq.pop(0)  
                    # recalcúlo entero value desde cero (aunque en práctica
                    # esto no debería ocurrir cuando k>=0)
                    value = 0
                else:
                    # Quito ese '1'
                    subseq.pop(idx)
                    # Resto su peso: como subseq ya fue shift-ado N bits,
                    # cada posición i vale 2^(len(subseq_after) - i)
                    bits_after = len(subseq)
                    # El peso en el momento de añadirlo era 2^(bits_after)
                    # pero como ya shift-e todo, ajusto:
                    weight = 1 << (bits_after - idx)
                    value -= weight

        # Al final, subseq es la subsecuencia más larga con valor <= k
        return len(subseq)