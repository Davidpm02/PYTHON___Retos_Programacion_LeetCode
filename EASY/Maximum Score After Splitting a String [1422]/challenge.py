"""
DESCRIPTION:

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:

Input: s = "1111"
Output: 3

 

Constraints:

    2 <= s.length <= 500
    The string s consists of characters '0' and '1' only.


"""

class Solution:
    def maxScore(self, s: str) -> int:
        
        """
        Retorna la máxima puntuación obtenible tras dividir la 
        cadena de entrada en dos subcadenas.

        La puntuación final se obtiene de la suma de bits 0 en la
        subcadena de la izquierda, más el número de bits 1 en la 
        subcadena de la derecha.

        params:
            s (str)

        returns:
            int
        """

        # Lista con las puntuaciones obtenidas
        scores_obtained_after_split = []

        for idx in range(1, len(s)):
            # Definición de las subcadenas y cálculo de la puntuación.
            left_substring_score = s[:idx].count("0")
            right_substring_score = s[idx:].count("1")
            score = left_substring_score + right_substring_score
            scores_obtained_after_split.append(score)
        return max(scores_obtained_after_split)
            
            
