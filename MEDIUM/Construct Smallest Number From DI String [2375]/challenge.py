"""
DESCRIPTION:

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

    num consists of the digits '1' to '9', where each digit is used at most once.
    If pattern[i] == 'I', then num[i] < num[i + 1].
    If pattern[i] == 'D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.

Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

 

Constraints:

    1 <= pattern.length <= 8
    pattern consists of only the letters 'I' and 'D'.

"""

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        """
        Se encarga de hallar la cadena de texto lexicográficamente más
        pequeña posible que cumpla las condiciones:
         - La cadena está compuesta por los dígitos comprendidos en el
           rango [1, 9], donde cada dígito solo puede ser utilizado
           una vez.
         - Si pattern[i] == 'I' ===> num[i] < num[i + 1]
         - Si pattern[i] == 'D' ===> num[i] > num[i + 1]

        params:
            pattern (str)
        
        returns:
            str
        """

        result = []                     # Lista para almacenar el resultado final
        stack = []                      # Lista que usaré como pila para manejar secuencias de 'D'
        
        # Recorro desde 0 hasta len(pattern) para cubrir el último dígito
        for i in range(len(pattern) + 1):
            # Agrego el dígito (i + 1) a la pila; lo hago en forma de string para facilitar la unión final
            stack.append(str(i + 1))
            
            # Si llego al final del patrón o el carácter actual es 'I'
            if i == len(pattern) or pattern[i] == 'I':
                # Desapilo todos los elementos para formar la secuencia correcta
                while stack:
                    result.append(stack.pop())
        
        return ''.join(result)

       