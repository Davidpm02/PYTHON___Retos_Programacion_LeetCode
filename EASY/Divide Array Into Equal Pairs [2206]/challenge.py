"""
DESCRIPTION:

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

    Each element belongs to exactly one pair.
    The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

 

Constraints:

    nums.length == 2 * n
    1 <= n <= 500
    1 <= nums[i] <= 500

"""

from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        

        """
        Se encarga de verificar si es posible dividir el array 'nums'
        en un conjunto de n parejas, donde:
         - Cada elemento pertenece únicamente a una pareja.
         - Los elementos presentes en una pareja deben ser iguales.

        params:
            nums (List[int])
        
        returns:
            bool
        """

        # Me aseguro primero de que 'nums' contiene un número par
        # de elementos
        n = len(nums)
        if (n % 2 != 0):
            return False

        # Contador de apariciones de cada entero en 'nums'
        reps_per_num = Counter(nums)

        # Inicializo una variable booleana que refleje la posibilidad
        # de crear un conjunto de n parejas con los mismos elementos
        isValid = True
        for num, reps in reps_per_num.items():
            if (isValid == False):
                break
            
            if (reps % 2 != 0):
                isValid = False
        return isValid