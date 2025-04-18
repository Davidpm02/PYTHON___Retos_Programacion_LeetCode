"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30

"""

class Solution:
    def countAndSay(self, n: int) -> str:

        """
        Se encarga de retornar una cadena de texto generada a partir
        del algoritmo RLE, tomando como partida el entero 'n'.

        params:
            n (int)

        returns:
            str
        """
        
        if n == 1:
            return "1"
        
        # Inicializamos la secuencia con el primer elemento
        result = "1"
        
        # Generamos los siguientes elementos hasta llegar a n
        for _ in range(2, n + 1):
            current = ""
            count = 1  # Contador de caracteres consecutivos
            
            # Itero por la cadena actual desde el segundo carácter
            for j in range(1, len(result)):
                # Si el carácter actual es igual al anterior, incremento el contador
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    # Si cambia el carácter, añado al resultado el número de repeticiones
                    # seguido del carácter anterior
                    current += str(count) + result[j - 1]
                    count = 1  # Reinicio el contador
            
            # Después del bucle, agrego el último grupo de caracteres
            current += str(count) + result[-1]
            result = current  # Actualizo el resultado para la siguiente iteración
        
        return result