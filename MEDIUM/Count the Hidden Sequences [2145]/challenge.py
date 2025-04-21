"""
DESCRIPTION:

You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].

You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.

For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
[5, 6, 3, 7] is not possible since it contains an element greater than 6.
[1, 2, 3, 4] is not possible since the differences are not correct.
Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.

 

Example 1:

Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2
Explanation: The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.
Example 2:

Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
Output: 4
Explanation: The possible hidden sequences are:
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
Thus, we return 4.
Example 3:

Input: differences = [4,-7,2], lower = 3, upper = 6
Output: 0
Explanation: There are no possible hidden sequences. Thus, we return 0.
 

Constraints:

n == differences.length
1 <= n <= 105
-105 <= differences[i] <= 105
-105 <= lower <= upper <= 105

"""

from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        """
        Se encarga de hallar el número de posibles secuencias que pueden
        formarse. El método trata de validar las posibles opciones para
        el comienzo de cada array, hidden[0], a fin de poder hacer uso
        de los enteros contenidos en el array 'differences' para formar
        el array final.

        params:
            differences (List[int])
            lower (int)
            upper (int)
        
        returns:
            int
        """

        # Inicializo una variable para llevar el acumulado de diferencias
        prefix_sum = 0
        
        # Inicializo los valores mínimo y máximo del acumulado
        min_prefix = 0
        max_prefix = 0
        
        # Recorro la lista de diferencias para construir los extremos del rango de acumulados
        for diff in differences:
            prefix_sum += diff
            # Mantengo el mínimo y máximo acumulado para definir el rango de variación
            min_prefix = min(min_prefix, prefix_sum)
            max_prefix = max(max_prefix, prefix_sum)
        
        # El valor inicial `x` debe ser tal que `x + min_prefix >= lower` y `x + max_prefix <= upper`
        # Despejo las inequaciones para obtener el rango válido para x:
        min_x = lower - min_prefix
        max_x = upper - max_prefix
        
        # Si no hay valores posibles para `x`, retorno 0
        if min_x > max_x:
            return 0
        
        # El número de valores enteros posibles para x es (max_x - min_x + 1)
        return max_x - min_x + 1