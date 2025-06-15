"""
DESCRIPTION:

You are given an integer num. You will apply the following steps to num two separate times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). Note y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
 

Constraints:

1 <= num <= 10^8

"""

class Solution:
    def maxDiff(self, num: int) -> int:
        
        s = str(num)

        # Genero el número máximo reemplazando el primer dígito que no sea 9 por 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # todos los dígitos son 9, no hay cambio

        # Genero el número mínimo
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))  # cambio el primer dígito por 1
        else:
            # Si el primer dígito ya es 1, busco otro dígito != 0 y != 1 para cambiarlo por 0
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num  # todos los dígitos son 0 o 1, no hay cambio

        return max_num - min_num