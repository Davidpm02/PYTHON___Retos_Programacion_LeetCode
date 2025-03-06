"""
DESCRIPTION:

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107

"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        """
        Se encarga de verificar si un número dado puede
        conformarse únicamente mediante sumas de las
        potencias de 3.

        params:
            n (int)
        
        returns:
            bool
        """

        # Valido si 'n' puede ser formado por potencias de 3,
        # basándome en la representación ternaria de 'n'.
        rests_of_divisions = []
        result = None
        while (result != 0):
            # Opero la division
            result = n // 3

            # Obtengo el resto
            rest = n % 3
            rests_of_divisions.insert(0, rest)

            # Actualizo el valor de 'n'
            n = result
        
        return True if (2 not in rests_of_divisions) else False