"""
DESCRIPTION:

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000

"""

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        """
        Determina si una lista de enteros contiene, al menos, tres
        números impares consecutivos.

        params:
            arr  (List[int])
            
        returns
            bool
        """

        # Inicializo una variable contadora
        consecutive_odds = 0

        # Variable para conservar el último índice con dígito impar
        last_odd_index = 0

        # Itero entre todos los números y actualizo el contador
        for idx, num in enumerate(arr):
            if (num % 2 != 0):
                # Reviso si el último dígito era impar
                if ((consecutive_odds != 0) and (abs(idx - last_odd_index) == 1)):
                    last_odd_index = idx
                    consecutive_odds += 1
                else:
                    last_odd_index = idx
                    consecutive_odds += 1

                if (consecutive_odds == 3):
                    return True
            else:
                # Reinicio el contador
                consecutive_odds = 0

        return False