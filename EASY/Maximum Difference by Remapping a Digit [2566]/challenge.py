"""
DESCRIPTION:

You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 10^8

"""

class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        """
        Se encarga de calcular el valor máximo posible a obtener
        mediante la diferencia entre el número máximo y el mínimo
        posible.

        Para obtener los máximos y mínimos, el método puede
        transformar cualquier dígito de 'num' en otro distinto,
        y obtener así el máximo posible, y el mínimo.

        params:
            num (int)
        
        returns:
            int
        """

        # Paso 1: convierto el número a string para poder trabajar con sus dígitos
        s = str(num)

        # Paso 2: para obtener el máximo, busco el primer dígito que no sea '9'
        # y lo reemplazo por '9' en todas sus apariciones
        for d in s:
            if d != '9':
                max_candidate = d
                break
        else:
            max_candidate = None  # todos son 9, el número ya es máximo

        if max_candidate:
            s_max = s.replace(max_candidate, '9')
        else:
            s_max = s  # no hay nada que reemplazar

        # Paso 3: para el mínimo, busco el primer dígito distinto de '0'
        # que no sea el primero si fuera '1', para evitar ceros a la izquierda
        for d in s:
            if d != '0' and d != s[0]:
                min_candidate = d
                break
        else:
            min_candidate = s[0]  # por defecto, reemplazo el primero

        if s[0] != '0':
            s_min = s.replace(s[0], '0')  # cambio el primer dígito por '1' si es posible
        else:
            s_min = s.replace(min_candidate, '0') if min_candidate else s

        # Paso 4: convierto a enteros y calculo la diferencia
        return int(s_max) - int(s_min)