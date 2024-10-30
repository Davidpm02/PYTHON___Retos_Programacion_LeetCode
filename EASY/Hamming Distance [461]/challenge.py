"""
DESCRIPTION:

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

  Input: x = 1, y = 4
  Output: 2
  Explanation:
  1   (0 0 0 1)
  4   (0 1 0 0)
         ↑   ↑
  The above arrows point to positions where the corresponding bits are different.

Example 2:

  Input: x = 3, y = 1
  Output: 1

 

Constraints:

    0 <= x, y <= 231 - 1

"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        """
        Summary:
            Método de la clase Solution encargado de hallar la
            distancia de Hamming entre dos enteros dados.
            
            La distancia de Hamming entre dos números corresponde
            al número de posiciones en los que los bits de las
            representaciones binarias de ambos números son diferentes.
        Args:
            x (int)
            y (int) 
        Returns:
            hamming_distance (int) -- Distancia de Hamming entre los
            enteros recibidos como parámetros. 
        """

        # Obtengo las representaciones en binario para ambos enteros
        binary_x = format(x, 'b')
        binary_y = format(y, 'b')

        if int(binary_x) < int(binary_y):
            zeros_to_insert = len(binary_y)
            binary_x = binary_x.rjust(zeros_to_insert, '0')
        else:
            zeros_to_insert = len(binary_x)
            binary_y = binary_y.rjust(zeros_to_insert, '0')
    
        zipped_values = zip(binary_x, binary_y)
        hamming_distance = 0
        for item in zipped_values:
            if item[0] != item[1]:
                hamming_distance += 1
        
        return hamming_distance
