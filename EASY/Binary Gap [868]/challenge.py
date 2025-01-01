"""
DESCRIPTION:

Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 

Example 1:

Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

Example 2:

Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

Example 3:

Input: n = 5
Output: 2
Explanation: 5 in binary is "101".

 

Constraints:

    1 <= n <= 109

"""

class Solution:
    def binaryGap(self, n: int) -> int:
        
        """
        Halla la máxima distancia entre bits 1 adyacentes en la 
        representación binaria del número recibido como parámetro.

        params:
            n (int)

        returns:
            int
        """

        # Comprobación inicial del número de bits 1 en la 
        # representación binaria de 'n'.
        binary_repr_of_n = bin(n)[2:]
        if (binary_repr_of_n.count('1') <= 1):
            return 0
        
        # Lista de bits en la representación binario.
        bits_on_binary_repr = [int(bit) for bit in binary_repr_of_n]

        # Contador de distancia máxima entre 1.
        maximum_distance_gap = 0
        distance_between_ones = 0
        try:
            index_first_bit = bits_on_binary_repr.index(1)
            for bit in bits_on_binary_repr[index_first_bit + 1:]:
                if (bit == 0):
                    distance_between_ones += 1
                    continue
                elif (bit == 1):
                    distance_between_ones += 1
                    if (distance_between_ones > maximum_distance_gap):
                        maximum_distance_gap = distance_between_ones
                    # Reinicio del contador de distancia
                    distance_between_ones = 0
                    continue
            return maximum_distance_gap
        except:
            return 0
