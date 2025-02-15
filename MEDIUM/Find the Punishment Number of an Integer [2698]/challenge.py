"""
DESCRIPTION:

Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

    1 <= i <= n
    The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

 

Example 1:

Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182

Example 2:

Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478

 

Constraints:

    1 <= n <= 1000

"""

class Solution:
    def punishmentNumber(self, n: int) -> int:
        

        """
        Se encarga de hallar el 'punishment number' de un entero dado.

        params:
            n (int)
        
        returns:
            int
        """

        def can_partition(num_str: str, target: int, current_sum=0, index=0) -> bool:
            """
            Función recursiva que verifica si el número `num_str` puede dividirse en partes cuya suma sea `target`.
            
            params:
                num_str (str): El número al cuadrado en formato de cadena.
                target (int): El número original que queremos verificar.
                current_sum (int): Suma actual de la partición en el proceso de backtracking.
                index (int): Índice actual en la cadena.
            
            returns:
                bool
            """
            
            if index == len(num_str):
                return current_sum == target  # Si llegamos al final de la cadena, verificamos la condición

            for j in range(index, len(num_str)):  # Intentamos todas las particiones posibles
                part = num_str[index:j + 1]  
                part_value = int(part)  

                if can_partition(num_str, target, current_sum + part_value, j + 1):
                    return True  # Si se cumple alguna partición, retornamos True
            
            return False  

        numbers_to_punishment = []                   

        # Recorro todos los números entre 1 y 'n'
        for num in range(2, n + 1):
            try:
                assert ((num % 9 == 0) or (num % 9 == 1))
                squared = str(num*num)
                
                # Compruebo que sea un número válido a tener en cuenta
                if (can_partition(squared, num)):
                    numbers_to_punishment.append(num)
            except AssertionError:
                continue
        
        punishment_number = 1
        for num in numbers_to_punishment:
            punishment_number += (num*num)
        return punishment_number