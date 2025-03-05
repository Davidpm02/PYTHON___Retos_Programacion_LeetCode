"""
DESCRIPTION:

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.


Return the number of colored cells at the end of n minutes.

 

Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
 

Constraints:

1 <= n <= 105

"""

class Solution:
    def coloredCells(self, n: int) -> int:

        """
        Se encarga de contar el número de celdas coloreadas de una
        matriz tras 'n' minutos, en un espacio bidimensional de
        tamaño infinito.

        La función tiene en cuenta que:
         - Al primer minuto se colorea una única celda, situada
           en cualquier punto del espacio infinito.
         - Tras cada minuto, se colorea cualquier celda sin color
           que esté en contacto con alguna celda coloreada.

        params:
            n (int)
        
        returns:
            int
        """
        
        # Inicializo una variable contadora de las celdas coloreadas
        colored_cells = 1

        if (n == 2):
            colored_cells = 5
        elif (n == 3):
            colored_cells = 13
        elif (n > 3):
            colored_cells = n**2 + (n-1)**2

        return colored_cells