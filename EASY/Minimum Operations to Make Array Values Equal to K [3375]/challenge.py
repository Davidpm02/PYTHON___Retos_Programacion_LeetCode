"""
DESCRIPTION:

You are given an integer array nums and an integer k.

An integer h is called valid if all values in the array that are strictly greater than h are identical.

For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:

Select an integer h that is valid for the current values in nums.
For each index i where nums[i] > h, set nums[i] to h.
Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.

 

Example 1:

Input: nums = [5,2,5,4,5], k = 2

Output: 2

Explanation:

The operations can be performed in order using valid integers 4 and then 2.

Example 2:

Input: nums = [2,1,2], k = 2

Output: -1

Explanation:

It is impossible to make all the values equal to 2.

Example 3:

Input: nums = [9,7,5,3], k = 1

Output: 4

Explanation:

The operations can be performed using valid integers in the order 7, 5, 3, and 1.

 

Constraints:

1 <= nums.length <= 100 
1 <= nums[i] <= 100
1 <= k <= 100

"""

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        """
        Calcula el número mínimo de operaciones necesarias para convertir todos los 
        elementos del array `nums` en el valor `k`, utilizando operaciones válidas.

        Una operación válida consiste en seleccionar un entero `h` tal que todos los 
        elementos mayores que `h` sean iguales, y luego reemplazar esos elementos por `h`.

        params:
            nums (List[int])
            k (int)
        
        returns:
            int
        """
        
        # Si ya todos los elementos son iguales a k, no necesito hacer ninguna operación
        if all(num == k for num in nums):
            return 0

        # Si existe algún valor menor que k, no podré alcanzar k reduciendo valores mayores,
        # así que devuelvo -1 directamente
        if any(num < k for num in nums):
            return -1

        # Creo un conjunto con los valores únicos mayores a k
        # porque cada uno de ellos necesitará una operación para ser reducido
        unique_above_k = {num for num in nums if num > k}

        # Si no hay ninguno por encima de k, significa que solo tengo k y menores,
        # y ya verifiqué que no todos son k, así que no puedo llegar a k
        if not unique_above_k:
            return -1

        # Ahora ordeno esos valores únicos de mayor a menor para simular las operaciones
        sorted_above_k = sorted(unique_above_k, reverse=True)

        # Inicializo el contador de operaciones
        operations = 0

        # En cada operación selecciono el siguiente valor menor que el anterior
        # como nuevo "h", asegurándome de que todos los valores superiores a h sean iguales
        for h in sorted_above_k:
            operations += 1

        return operations