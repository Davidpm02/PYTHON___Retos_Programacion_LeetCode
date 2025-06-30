"""
DESCRIPTION:

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

 

Constraints:

1 <= nums.length <= 2 * 10^4
-109 <= nums[i] <= 10^9

"""

from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Paso 1: Contamos la frecuencia de cada número
        count = Counter(nums)
        
        # Paso 2: Inicializamos la variable para almacenar la longitud máxima
        max_len = 0

        # Paso 3: Recorremos cada número en el diccionario de frecuencias
        for num in count:
            # Si el número adyacente (num + 1) existe, evaluamos esta posible subsecuencia armoniosa
            if num + 1 in count:
                # La longitud de la subsecuencia sería la suma de las frecuencias de ambos
                current_len = count[num] + count[num + 1]
                # Actualizamos el valor máximo si esta subsecuencia es más larga
                max_len = max(max_len, current_len)
        
        # Paso 4: Devolvemos la longitud de la subsecuencia más larga encontrada
        return max_len