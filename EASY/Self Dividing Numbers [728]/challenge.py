"""
DESCRIPTION:

A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

 

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]

 

Constraints:

    1 <= left <= right <= 104

"""

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        """
        Halla todos los números consideros divisibles entre sí dentro de un
        rango cerrado de números, contenidos dentro de los límites marcados por 
        los parámetros de entrada.

        params:
            left (int)
            right (int)

        returns:
            List[int]
        """

        # Lista de referencia para 'self-dividing numbers'
        self_dividing_array = []
        for number in range(left, right + 1):
            digits_in_number = [int(digit) for digit in str(number)]
            if (0 in digits_in_number):
                continue

            valid_dividing_numbers = all(number % digit == 0 for digit in digits_in_number)
            if valid_dividing_numbers:
                self_dividing_array.append(number)
        
        return self_dividing_array