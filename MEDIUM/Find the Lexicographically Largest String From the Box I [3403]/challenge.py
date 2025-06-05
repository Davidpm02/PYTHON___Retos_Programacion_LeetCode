"""
DESCRIPTION:

You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.

 

Example 1:

Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation: 

All possible splits are:

"d" and "bca".
"db" and "ca".
"dbc" and "a".
Example 2:

Input: word = "gggg", numFriends = 4

Output: "g"

Explanation: 

The only possible split is: "g", "g", "g", and "g".

 

Constraints:

1 <= word.length <= 5 * 103
word consists only of lowercase English letters.
1 <= numFriends <= word.length

"""

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        Dado un string 'word' y un entero 'numFriends', encuentra la cadena
        lexicográficamente mayor que pueda aparecer como una de las partes
        al dividir 'word' en 'numFriends' subcadenas no vacías en cualquier
        ronda posible.
        """
        n = len(word)
        
        # Si solo hay un amigo, la única división es el string completo.
        if numFriends == 1:
            return word
        
        # Yo calculo la longitud máxima de cualquier subcadena válida.
        max_len = n - numFriends + 1
        
        mejor = ""  # Yo mantengo la mejor cadena lexicográfica encontrada.
        # Recorro cada índice de inicio posible.
        for i in range(n):
            # Yo determino cuánto puedo extraer desde i sin exceder max_len
            longitud_actual = min(max_len, n - i)
            candidato = word[i : i + longitud_actual]
            # Yo comparo y actualizo si encuentro algo mayor lexicográficamente.
            if candidato > mejor:
                mejor = candidato
        
        return mejor
