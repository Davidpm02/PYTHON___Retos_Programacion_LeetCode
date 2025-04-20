"""
DESCRIPTION:

There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11
 

Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000

"""

from typing import List
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Calcula el número mínimo posible de conejos que podría haber en el bosque
        a partir de las respuestas dadas por algunos de ellos. 

        params:
            answers (List[int])

        returns:
            (int)
        """
        
        count = Counter(answers)
        total = 0

        # Recorro cada respuesta única y su frecuencia
        for answer, freq in count.items():
            group_size = answer + 1  # Cada grupo necesita al menos answer + 1 conejos
            num_groups = (freq + group_size - 1) // group_size  # Redondeo hacia arriba
            total += num_groups * group_size  # Sumo el total de conejos estimados para ese grupo

        return total
