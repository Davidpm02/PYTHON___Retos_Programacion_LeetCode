"""
DESCRIPTION:

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

    'a' maps to ".-",
    'b' maps to "-...",
    'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.

Return the number of different transformations among all words we have.

 

Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Example 2:

Input: words = ["a"]
Output: 1

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 12
    words[i] consists of lowercase English letters.

"""

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        """
        Retorna el total de transformaciones de cada palabra
        dentro de la lista 'words', obtenidas al traducir cada
        una de estas a código morse.

        params:
            words (List[str])
        
        returns:
            int
        """

        english_abc_array = [chr(_) for _ in range(97, 97 + 26)]
        morse_code_array = [".-","-...","-.-.","-..",".","..-.","--.",
                            "....","..",".---","-.-",".-..","--","-.",
                            "---",".--.","--.-",".-.","...","-","..-",
                            "...-",".--","-..-","-.--","--.."]

        # Diccionario que mapee cada letra con su representación
        # en código morse.
        abc_to_morse_dict = dict(zip(english_abc_array, morse_code_array))

        # Conjunto vacío para contener todas las transformaciones formadas
        morse_transformations_set = set()
        for word in words:
            morse_transformations_set.add("".join([abc_to_morse_dict[char] for char in word]))
        return len(morse_transformations_set)