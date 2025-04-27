"""
DESCRIPTION:

Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

 

Example 1:

Input: nums = [1,2,1,4,1]

Output: 1

Explanation:

Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:

Input: nums = [1,1,1]

Output: 0

Explanation:

[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

 

Constraints:

3 <= nums.length <= 100
-100 <= nums[i] <= 100

"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        """
        Se encarga de verificar el número de tripletes "validos"
        de enteros dentro de un array recibido como parámetro.

        Un triplete se considera válido siempre y cuando:
         - La suma del primer y último entero sea igual a la mitad
           del entero situado en la posición central del triplete.

        params:
            nums (List[int])

        returns:
            int
        """

        # Longitud del array
        n = len(nums)

        # Contador de tripletes válidos
        valid_subarrays = 0

        # Recorremos el array en busca de tripletes válidos
        for i in range(1, n - 1):
            # Validamos si el triplete es válido
            if ((nums[i - 1] + nums[i + 1]) == (nums[i] / 2)):
                valid_subarrays += 1
        
        return valid_subarrays