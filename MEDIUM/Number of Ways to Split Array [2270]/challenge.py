"""
DESCRIPTION:

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

    The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
    There is at least one element to the right of i. That is, 0 <= i < n - 1.

Return the number of valid splits in nums.

 

Example 1:

Input: nums = [10,4,-8,7]
Output: 2
Explanation: 
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.

Example 2:

Input: nums = [2,3,1,0]
Output: 2
Explanation: 
There are two valid splits in nums:
- Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split. 
- Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.

 

Constraints:

    2 <= nums.length <= 105
    -105 <= nums[i] <= 105

"""

from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        """
        Se encarga de obtener el número total de splits aplicables a
        una lista de enteros recibida como parámetro.

        Para que un split sea considerado válido:
         - La suma de los primeros i + 1 elementos de la lista debe
         ser mayor o igual a la suma de los últimos n - i - 1 elementos.
         - Debe haber, al menos, un elemento de la derecha de i.
         Esto es, 0 <= i < n - 1.
        
        params:
            nums (List[int])
        
        returns:
            int
        """

        # Calculo la suma total de nums
        total_sum = sum(nums)
        left_sum = 0
        valid_split_count = 0

        # Itero por los índices posibles para dividir
        for i in range(len(nums) - 1):  # Último índice no es válido
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            
            # Compruebo si la condición se cumple
            if left_sum >= right_sum:
                valid_split_count += 1

        return valid_split_count