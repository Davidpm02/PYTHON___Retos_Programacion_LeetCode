"""
Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

  Input: num = 26
  Output: "1a"

Example 2:

  Input: num = -1
  Output: "ffffffff"

 

Constraints:

    -231 <= num <= 231 - 1

"""

class Solution:
    def toHex(self, num: int) -> str:
        
        """
        Summary:
            Método de la clase Solution encargado de retornar una
            cadena que represente un entero dado en 32-bits en formato
            hexadecimal.
        Args:
            num (int) -- Entero de 32-bits.
        Returns:
            str
        """

        # Arrays de referencia para conversión decimal-hexadecimal
        decimals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                    11, 12, 13, 14, 15, 16, 17, 18, 19,
                    20, 21, 22, 23, 24, 25, 26, 27, 28,
                    29, 30, 40, 50, 60, 70, 80, 90, 100,
                    200, 1000, 2000]

        hexadecimals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13',
                        '14', '15', '16', '17', '18', '19', '1A', '1B', '1C',
                        '1D', '1E', '28', '32', '3C', '46', '50', '5A', '64',
                        'C8', '3E8', '7D0']
        inversed_hex_values = ['F', 'E', 'D', 'C', 'B', 'A', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

        # Último cociente
        last_quotient = None

        # Restos
        remainders = []

        if (num < 0):
            try:
                return 'fffffff' + inversed_hex_values[int(str(num)[1:]) - 1].lower()
            except ValueError:
                return 'fffffff' + inversed_hex_values[int(str(num)[1:]) - 1]
            except IndexError:
                try:
                    return 'fffffff' + inversed_hex_values[int(str(num)[-1]) - 1].lower()
                except ValueError:
                    return 'fffffff' + inversed_hex_values[int(str(num)[-1]) - 1]

        while True:
            if last_quotient == 0:
                break
            last_quotient = num // 16
            remainders.append((num % 16))
            num = last_quotient
        
        # Construyendo la representación hexadecimal de 'num'
        hexadecimal_repr_content = []
        for r in remainders[::-1]:
            index_in_decimals_array = decimals.index(r)
            hexadecimal_repr_content.append(hexadecimals[index_in_decimals_array])

        return "".join(hexadecimal_repr_content).lower()