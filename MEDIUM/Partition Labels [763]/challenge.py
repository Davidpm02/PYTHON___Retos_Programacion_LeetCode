"""
DESCRIPTION:

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

"""

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        """
        Se encarga de dividir una cadena de texto en tantas subcadenas
        como sea posible, de forma que cada letra aparezca, como máximo,
        en una única subcadena.

        El método retorna un array de enteros, donde cada entero
        representa la longitud de las subcadenas obtenidas.

        params:
            s (str)
        returns:
            List[int]
        """
       
        # Paso 1: Obtener la última posición de cada carácter en el string
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Paso 2: Iterar sobre la cadena y definir los cortes de las particiones
        partitions = []
        start, end = 0, 0
        
        for idx, char in enumerate(s):
            # Expandimos el final del segmento al máximo índice donde aparece este carácter
            end = max(end, last_occurrence[char])
            
            # Si alcanzamos el final del segmento actual, hacemos un corte
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1  # Actualizamos el inicio del próximo segmento
        
        return partitions