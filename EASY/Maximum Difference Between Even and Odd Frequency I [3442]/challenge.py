"""
DESCRIPTION:

You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.

 

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 

Constraints:

3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.

"""

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        
        # Mapeo de las repeticiones de cada caracter
        rep_chars = Counter(s)
        sorted_by_values = dict(sorted(rep_chars.items(), key=lambda item: item[1]))

        # Hallo la máxima diferencia ------------
        # Encuentro el caracter par de menor número (se podría optimizar con un solo bucle)
        lowest_even_rep = sorted([reps for char, reps in sorted_by_values.items() if (reps % 2 == 0)])[0]
        highest_odd_rep = sorted([reps for char, reps in sorted_by_values.items() if (reps % 2 != 0)])[-1]

        # Si no hay pares, o no hay impares, no se puede calcular la diferencia
        if lowest_even_rep is None or highest_odd_rep is None:
            return -1
        
        return (highest_odd_rep - lowest_even_rep)