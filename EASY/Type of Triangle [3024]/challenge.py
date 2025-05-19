"""
DESCRIPTION:

You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

 

Example 1:

Input: nums = [3,3,3]
Output: "equilateral"
Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.
Example 2:

Input: nums = [3,4,5]
Output: "scalene"
Explanation: 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.
 

Constraints:

nums.length == 3
1 <= nums[i] <= 100

"""

from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        """
        Se encarga de comprobar qué tipo de triángulo se puede formar
        a partir de un array de enteros.

        Cada entero en el array representa la longitud de uno de sus
        lados.

        params:
            nums (List[int])
        
        returns:
            str
        """

        # Aplico la desigualdad triangular para validar la posibilidad
        # de crear un triángulo con las longitudes dadas
        ordered_nums = sorted(nums)
        if ((ordered_nums[0] + ordered_nums[1]) <= ordered_nums[2]):
            return "none"

        # Inicializo un contador igualado a 0
        diff_sides = 0

        # Defino un diccionario que mapee el número de lados diferentes
        # con el tipo de triángulo
        types_triangles = {
            "1" : "equilateral", # Todos los lados iguales
            "2" : "isosceles",   # 2 lados iguales
            "3" : "scalene"      # Tidos los lados diferentes
        }

        # Defino un conjunto a partir del array de longitudes
        set_nums = set(nums)
        
        # Retorno el tipo de triángulo que se puede formar
        return types_triangles[str(len(set_nums))]

