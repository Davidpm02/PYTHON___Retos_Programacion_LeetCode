"""
DESCRIPTION:

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 10^4

"""

from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        result = []

        # Uso una función auxiliar para recorrer los números de forma lexicográfica
        def dfs(current: int):
            # Si el número actual excede el límite n, detengo la recursión
            if current > n:
                return
            # Añado el número actual al resultado
            result.append(current)
            # Recorro los hijos posibles (añadiendo dígitos del 0 al 9 al final)
            for i in range(10):
                next_num = current * 10 + i
                if next_num > n:
                    break  # Si me paso de n, dejo de explorar esta rama
                dfs(next_num)

        # Inicio el recorrido desde los números del 1 al 9 (no empiezo en 0)
        for i in range(1, 10):
            dfs(i)

        return result