"""
DESCRIPTION:

You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109

"""

from typing import List
from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        

        """
        Se encarga de hallar el número de 'Bad pairs' dentro
        de un array recibido como parámetro.

        Se define a una 'Bad Pair' como una pareja de índices
        (i, j), tales que: j - i != nums[j] - nums[i].

        params:
            nums (List[int])

        returns:
            int 
        """

        # Podemos obtener el total de 'Bad Pairs' como 
        # Total Pairs - Good Pairs = Bad Pairs

        # Defino un contador para el número de parejas totales del array
        n = len(nums)
        total_pairs = int(n*(n - 1) / 2)

        # Obtengo el total de 'Good pairs' en el array
        # j−nums[j]=i−nums[i]
        freq = defaultdict(int)  # Hashmap para contar valores de (i - nums[i])
        good_pairs = 0

        for i, num in enumerate(nums):
            key = i - num
            good_pairs += freq[key]  # Si ya hemos visto este key antes, suma a good_pairs
            freq[key] += 1  # Aumentamos la frecuencia de este key
        
        return total_pairs - good_pairs