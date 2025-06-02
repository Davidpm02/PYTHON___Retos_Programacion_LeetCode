"""
DESCRIPTION:

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4

"""

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Método que calcula el número mínimo de caramelos necesarios.

        params:
            ratings (List[int])
        
        returns:
            int
        """
        # Verifico si la lista de valoraciones está vacía (aunque según
        # restricciones, n >= 1).
        if not ratings:
            return 0

        n = len(ratings)
        # Inicializo una lista de caramelos con 1 para cada niño, porque
        # cada uno debe recibir al menos uno.
        candies = [1] * n

        # Paso 1: recorrido de izquierda a derecha
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Paso 2: recorrido de derecha a izquierda
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Sumo todos los valores de caramelos para obtener el total mínimo necesario
        total_candies = sum(candies)
        return total_candies