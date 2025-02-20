"""
DESCRIPTION:

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

 

Constraints:

    n == nums.length
    1 <= n <= 16
    nums[i].length == n
    nums[i] is either '0' or '1'.
    All the strings of nums are unique.

"""

from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        """
        Se encarga de hallar una representación binaria cualquiera
        de longitud 'n' que no aparezca en el parámetro 'nums'.

        Si exiten varias opciones disponibles, la función retornará
        una cualquiera.

        params:
            nums (List[str])

        returns:
            str        
        """

        # Longitud de cada número en nums
        length_num = len(nums[0])

        if ((len(nums) == 1) and (len(nums[0]) == 1)):     # Valido la longitud de nums y devuelvo el resultado
            return "1" if (nums[0] == "0") else "0"        # si se cumplen las condiciones.

        # Verifico primero si se encuentra el 0 dentro del listado
        # de nums
        if (("0" * length_num) not in nums):
            return "0" * length_num
        else:
            # Contador de iteraciones completadas
            fully_iterated = 0
            while (fully_iterated != length_num):
                # Inicializo un array con length_num elementos == 0
                initial_array = ["0"] * length_num

                if (fully_iterated > 0):
                    for _ in range(0, fully_iterated + 1):
                        initial_array[_] = "1"
                    if ("".join(initial_array) not in nums):
                        return "".join(initial_array)

                # Itero sobre el total de la longitud de cada número
                for i in range(length_num - 1, 0 , -1):
                    initial_array[i] = "1"
                    if ("".join(initial_array) not in nums):
                        return "".join(initial_array)
                    else:
                        initial_array[i] = "0"
                        continue
                # Incremento el contador de iteraciones completadas
                fully_iterated += 1