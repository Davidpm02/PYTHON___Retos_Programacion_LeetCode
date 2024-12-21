"""
DESCRIPTION:

Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

 

Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.

 

Constraints:

    1 <= licensePlate.length <= 7
    licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
    1 <= words.length <= 1000
    1 <= words[i].length <= 15
    words[i] consists of lower case English letters.

"""

from collections import Counter
from typing	import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        """
        Encuentra la palabra completa más corta en una lista de palabras basada en un conjunto 
        de restricciones definidas por una cadena de caracteres (licensePlate).

        Una palabra completa contiene todas las letras del `licensePlate` (ignorando números, 
        espacios y mayúsculas/minúsculas), y cada letra debe aparecer al menos tantas veces 
        como se encuentra en `licensePlate`.

        Si existen múltiples palabras completas con la misma longitud, devuelve la primera 
        palabra completa que aparece en la lista de entrada.

        params:
        - licensePlate (str): Una cadena que contiene letras, números y/o espacios. 
        Los números y espacios se ignoran al determinar las letras requeridas.
        - words (list[str]): Una lista de palabras (cadenas) entre las que se buscará 
        la palabra completa más corta.

        returns:
        - str: La palabra completa más corta que satisface las condiciones del 
        `licensePlate`.
        """

        # Defino una lista con los caracteres válidos de 'licensePlate'
        valid_chars = [char.lower() for char in licensePlate if (char.isalpha() and (char != " "))]
        valid_chars_counter = Counter(valid_chars)

        # Lista con las palabras de words que contienen todas las letras de 'licensePlate'
        licensePlate_words = sorted([word for word in words if all(char in word for char in valid_chars)], key=len)
        licensePlate_words_updates = [word for word in licensePlate_words if all(word.count(key) >= value for key, value in valid_chars_counter.items())]

        return licensePlate_words_updates[0]