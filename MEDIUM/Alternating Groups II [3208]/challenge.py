"""
DESCRIPTION:

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

    colors[i] == 0 means that tile i is red.
    colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:

Alternating groups:

Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:

Alternating groups:

Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:

 

Constraints:

    3 <= colors.length <= 105
    0 <= colors[i] <= 1
    3 <= k <= colors.length

"""

from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        """
        Se encarga de hallar el total de grupos alternantes donde el
        número de fragmentos alternados sea igual a 'k'.

        params:
            colors (List[int])
            k (int)
        
        returns:
            int
        """

        n = len(colors)

        # Si el grupo completo es de longitud k=1, en teoría siempre sería alternante.
        diff = [1 if colors[i] != colors[(i+1) % n] else 0 for i in range(n)]
        
        # Extiendo el arreglo diff con los primeros (k-2) elementos.
        ext_diff = diff + diff[:k-2]
        
        # Calculo la suma de la primera ventana de tamaño (k-1), ya que un grupo alternante
        # debe tener (k-1) diferencias verdaderas.
        window_sum = sum(ext_diff[:k-1])
        count = 0
        # Si la suma es igual a k-1 --> todos los pares en la ventana son alternantes.
        if window_sum == k-1:
            count += 1

        # Recorro las ventanas deslizantes a partir de la posición 1 hasta n-1
        for i in range(1, n):
            # Resto el valor que sale de la ventana y sumo el nuevo valor que entra
            window_sum = window_sum - ext_diff[i-1] + ext_diff[i + k - 2]
            if window_sum == k-1:
                count += 1
        
        return count