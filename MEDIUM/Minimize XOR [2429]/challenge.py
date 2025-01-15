"""
DESCRIPTION:

Given two positive integers num1 and num2, find the positive integer x such that:

    x has the same number of set bits as num2, and
    The value x XOR num1 is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

 

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

 

Constraints:

    1 <= num1, num2 <= 109

"""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        """
        Se encarga de obtener el número que minimice la función
        XOR con respecto al parámetro 'num1', siempre y cuando
        el número en cuestión mantenga el mismo número de bits
        fijados que el parámetro 'num2'.

        params:
            num1 (int)
            num2 (int)
        
        returns:
            int
        """

        # Paso 1: Contamos el número de bits fijados (1's) en num2
        ones_num2 = bin(num2).count('1')
        
        # Paso 2: Crear el número x con el mismo número de bits fijados que num2
        x = 0
        ones_added = 0
        
        # Paso 3: Intentamos agregar bits fijados en las posiciones más cercanas a num1
        for i in range(31, -1, -1):  # Iteramos sobre los 32 bits (suponiendo números de 32 bits)
            if (num1 >> i) & 1:  # Si el bit i de num1 está fijado
                x |= (1 << i)  # Fijamos ese bit en x
                ones_added += 1
            
            if ones_added == ones_num2:
                break
        
        # Si aún necesitamos agregar más bits fijados, lo hacemos en los bits más bajos posibles
        if ones_added < ones_num2:
            for i in range(32):
                if (x >> i) & 1 == 0:  # Si el bit i no está fijado
                    x |= (1 << i)  # Fijamos el bit i
                    ones_added += 1
                if ones_added == ones_num2:
                    break
        
        return x