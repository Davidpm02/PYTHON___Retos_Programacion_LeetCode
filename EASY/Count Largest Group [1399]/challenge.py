"""
DESCRIPTION:

You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104

"""

from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        """
        Se encarga de obtener el número de grupos de mayor
        longitud que existen cuando agrupamos todos los números
        en el rango [1, n] en base a la suma total de sus dígitos.

        params:
            n (int)

        returns:
            int
        """

        # Defino un objeto Counter que registre el número de grupos de
        # cada tamaño
        length_groups = Counter()

        # Reviso todos los números en el rango [1, n] e incremento
        # el contador del grupo asociado
        for num in range(1, n + 1):
            # Obtengo la suma total de los dígitos del número iterado
            total_sum = sum(int(n) for n in str(num))
            length_groups[total_sum] += 1

        # Retorno el número de grupos con el mayor tamaño
        greatest_group = max(length_groups.values())
        return sum(1 for v in length_groups.values() if v == greatest_group)