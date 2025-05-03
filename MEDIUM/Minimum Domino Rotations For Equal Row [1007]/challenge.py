"""
DESCRIPTION:

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6

"""

from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        """
        Encuentra el número mínimo de rotaciones necesarias para que
        todos los valores en tops sean iguales o todos los valores
        en bottoms sean iguales.
        
        params:
            tops (List[int])
            bottoms (List[int])
            
        returns:
            int

        """

        n = len(tops)
        
        # Comprobamos los dos valores posibles: 
        # 1. todos los tops iguales al primer top
        # 2. todos los tops iguales al primer bottom
        
        def check_rotations(target):
            # Intentamos hacer que todos los tops sean igual a target
            top_rotations = 0
            bottom_rotations = 0
            
            for i in range(n):
                # Si ninguno de los valores del dominó es igual al objetivo, no es posible
                if tops[i] != target and bottoms[i] != target:
                    return -1
                
                # Si el top no es igual al objetivo pero el bottom sí, rotamos
                if tops[i] != target:
                    top_rotations += 1
                
                # Si el bottom no es igual al objetivo pero el top sí, rotamos
                if bottoms[i] != target:
                    bottom_rotations += 1
            
            # Devolvemos el mínimo entre hacer todas las tops igual a target
            # o hacer todas las bottoms igual a target
            return min(top_rotations, bottom_rotations)
        
        # Probamos con el valor del primer top
        result1 = check_rotations(tops[0])
        
        # Probamos con el valor del primer bottom si es diferente
        if tops[0] == bottoms[0]:
            return result1
        
        result2 = check_rotations(bottoms[0])
        
        # Si ambos son -1, no hay solución
        if result1 == -1 and result2 == -1:
            return -1
        
        # Si uno es -1, devolvemos el otro
        if result1 == -1:
            return result2
        if result2 == -1:
            return result1
        
        # De lo contrario, devolvemos el mínimo
        return min(result1, result2)