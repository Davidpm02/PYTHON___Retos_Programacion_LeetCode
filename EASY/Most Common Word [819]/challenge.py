"""
DESCRIPTION:

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

 

Constraints:

    1 <= paragraph.length <= 1000
    paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
    0 <= banned.length <= 100
    1 <= banned[i].length <= 10
    banned[i] consists of only lowercase English letters.

"""

from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        """
        Se encarga de hallar la palabra más común dentro de una cadena
        recibida como parámetro. La función tiene en cuenta las palabras
        del parámetro 'banned' para ofrecer un resultado válido.

        params:
            paragraph (str)
            banned (List[str])
        
        returns:
            str
        """

        # Proceso 'paragraph' para eliminar caracteres no válidos
        non_valid_chars = [char for char in "!?',;."]
        for non_valid_char in non_valid_chars:
            paragraph = paragraph.replace(non_valid_char, "")
        print(paragraph)
        # Actualizo el contenido de 'paragraph' a minúsculas
        paragraph = paragraph.lower()

        # Elimino todos los elementos prohibidos
        for word in [_.lower() for _ in banned]:
            if word in [__.lower() for __ in paragraph.split()]:
                paragraph = paragraph.replace(word, "")
     
        print(paragraph)

        # Defino un objeto Contador de todos los elementos en 'paragraph'
        # y retorno el más común
        str_counter = Counter([word.lower() for word in paragraph.split()])
        print(str_counter)
        return str_counter.most_common()[0][0]
        