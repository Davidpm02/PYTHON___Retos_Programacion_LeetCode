"""
DESCRIPTION:

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

 

Constraints:

    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.

"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        """
        Retorna el total de joyas que se tienen con respecto a un
        inventario de piedras dado.

        params:
            jewels (str) -- Joyas de referencia a examinar.
            stones (str) -- Inventario de piedras disponible.
        
        returns:
            int -- Total de joyas dentro del inventario de piedras
            disponible.
        """

        # Lista con las joyas que tenemos de referencia
        jewels_list = [jewel for jewel in jewels]

        # Contador de joyas con respecto al total de piedras
        jewels_counter = 0
        for jewel in jewels_list:
            if (jewel in stones):
                jewels_counter += stones.count(jewel)
        return jewels_counter