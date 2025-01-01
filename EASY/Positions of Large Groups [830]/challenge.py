"""
DESCRIPTION:

In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

 

Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.

Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.

Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".

 

Constraints:

    1 <= s.length <= 1000
    s contains lowercase English letters only.

"""

from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        """
        Se encarga de obtener los índices que primer y último
        carácter que contiene cada uno de los grupos de letras
        contenido en la cadena recibida como parámetro.

        La solución entregada por la función tiene en cuenta
        únicamente los grupos considerados grandes (3 caracteres
        o más en el mismo grupo).

        params:
            s (str)
        
        returns:
            List[List[int]]
        """

        # Lista con cada carácter en 's'
        chars_on_string = [char for char in s]
        starting_indexes_for_groups = []


        # Actualizo el contenido de 'starting_indexes_for_groups'
        for idx, char in enumerate(chars_on_string):
            if (idx == 0):
                starting_indexes_for_groups.append(idx)
                continue
            else:
                if (char != chars_on_string[idx - 1]):
                    starting_indexes_for_groups.append(idx)


        # Proceso la lista para formar los grupos de caracteres
        while True:
            for idx, char in enumerate(chars_on_string):
                if (idx == 0):
                    continue
                else:
                    if (char == chars_on_string[idx - 1]):
                        chars_on_string[idx - 1] += char
                        chars_on_string.pop(idx)
                        break
            else:
                # Segunda pasada para reafinar los grupos creados
                for idx, char in enumerate(chars_on_string):
                    if (idx == 0):
                        continue
                    else:
                        if (char in chars_on_string[idx - 1]):
                            chars_on_string[idx - 1] += char
                            chars_on_string.pop(idx)
                            break
                else:
                    break
        
        # Lista para almacenar el rango de índices de cada grupo
        # considerado grande.
        large_groups_indexes = [
            [starting_indexes_for_groups[idx], (starting_indexes_for_groups[idx] + (len(group) - 1))]
            for idx, group in enumerate(chars_on_string)
            if (len(group) >= 3)
        ]
        return large_groups_indexes
