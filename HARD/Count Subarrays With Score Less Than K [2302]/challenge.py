"""
DESCRIPTION:

The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [2,1,4,3,5], k = 10
Output: 6
Explanation:
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.
Example 2:

Input: nums = [1,1,1], k = 5
Output: 5
Explanation:
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^15

"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        """
        Cuenta el número de subarrays no vacíos en 'nums' cuyo score es estrictamente menor que 'k'.

        params:
            nums (List[int])
            k (int)

        returns:
            int
        """

        # Inicializo el resultado que va a acumular el número de subarrays válidos
        result = 0
        
        # Inicializo dos punteros para la ventana: el inicio (left) y el final (right)
        left = 0
        
        # Inicializo la suma de los elementos de la ventana actual
        window_sum = 0

        # Recorro el array usando 'right' como extremo derecho de la ventana
        for right in range(len(nums)):
            # Añado el elemento actual a la suma de la ventana
            window_sum += nums[right]
            
            # Mientras el score de la ventana actual no cumpla la condición (score >= k)
            while window_sum * (right - left + 1) >= k:
                # Voy desplazando el inicio de la ventana hacia la derecha
                window_sum -= nums[left]
                left += 1
            
            # Todos los subarrays que terminan en 'right' y empiezan entre 'left' y 'right' son válidos
            result += (right - left + 1)
        
        # Devuelvo el total de subarrays encontrados
        return result