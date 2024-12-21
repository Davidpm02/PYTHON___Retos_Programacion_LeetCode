"""
DESCRIPTION:

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

 

Constraints:

    2 <= nums.length <= 50
    0 <= nums[i] <= 100
    The largest element in nums is unique.

"""

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        """
        Halla el mayor elemento dentro de una lista de enteros, y retorna el
        índice de dicho elemento en la lista si este es, al menos, el doble de
        cualquier otro número dentro de la lista.

        params:
            nums (List[int])
        
        returns:
            int
        """

        # Referencia a la lista original
        original_nums = nums.copy()

        # Obtengo el mayor número de la lista
        biggest_num = max(nums)

        # Elimino el mayor número de la lista, y verifico si este es, al menos,
        # el doble del resto de números
        nums.remove(biggest_num)
        are_numbers_twice = all(biggest_num / num >= 2 for num in nums if (num != 0))
        if are_numbers_twice:
            return original_nums.index(biggest_num)
        return -1

        # return original_nums.index(biggest_num) if all(biggest_num / num >= 2 for num in nums if (num != 0)) else -1