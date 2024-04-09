"""
DESCRIPTION:

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"      
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

import string
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Función parametrizada que se encarga de buscar el palíndromo más largo dentro de una cadena
           recibida como parámetro, y retornarlo ámbito global del programa.
           
        Args:
            s -- Cadena a ser procesada por la función.
        
        Returns:
            str -- Palíndromo más largo encontrado dentro de la cadena "s". Si no se encuentra ningún palíndromo,
                   la respuesta es una cadena vacía.
        """
        
        # Normalizo el string recibido como parámetro  (mantengo letras mayúsculas)
        s_processed = s.translate(str.maketrans("", "", string.punctuation))
        
        # Defino una referencia del string procesado, pero invertido
        reference = s_processed[::-1]
        
        # Si ambas cadenas son iguales, retorno la cadena recibida (procesada)
        if s_processed == reference:
            return s_processed
        
        # Defino listas con los tokens de cada cadena
        tokens = s_processed.split(" ")
            
        # Compruebo la existencia de palíndromos dentro de cada subcadena de la cadena principal
        longest_palindromic_substring = ""
        for token in tokens:
            for i in range(len(token)):
                for j in range(i+1, len(token)+1):
                    substring = token[i:j]
                    if substring == substring[::-1] and len(substring) > len(longest_palindromic_substring):
                        longest_palindromic_substring = substring
        
        # Retorno la subcadena más larga encontrada (retorna "" si no se encuentra ningún palíndromo)
        return longest_palindromic_substring
                    
                    
                
            
        
        
if __name__ == "__main__":
    
    cadena = "cbbd"
    solution = Solution()
    sol = solution.longestPalindrome(s=cadena)
    print(sol)                    

            
        