"""
DESCRIPTION:

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

  Input: digits = "23"
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:

  Input: digits = ""
  Output: []


Example 3:

  Input: digits = "2"
  Output: ["a","b","c"]
 

## Constraints:

  0 <= digits.length <= 4
  digits[i] is a digit in the range ['2', '9'].
"""

from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Método de la clase Soluction que se encarga de buscar 
           todas las combinaciones de letras posibles dados una serie de números
           recibidos por la función.
           
           Args:
               digits -- Cadena que contiene los dígitos 'pulsados', para los que
                         de quieren encontrar todas las combinaciones de caracteres
                         posibles.
           
           Returns:
               list -- Array que contiene cadenas de texto con todas las combinaciones
                       posibles, dados el contenido del parámetro de entrada 'digits'.
        """
        
        def recurvise_search(index, built_combination):
          """Función auxiliar que permite ejecutar una estrategia de backtracking para construir
             todas las posibles combinaciones de letras para los dígitos del parámetro 'digits'.
             
             Args:
                 digits --
                 index --
                 built_combination -- 
             
             Returns:
          """
          
          if index == len(digits):
            letter_combinations_array.append("".join(built_combination))
            return
          elif index < len(digits):
            
            # Determino el digito correspondiente al indice recibido por la función
            actual_number = digits[index]
            
            # Busco las letras asociadas al dígito actual
            chars_for_number = chars_for_number_dict[actual_number]
            
            # Itero sobre cada una de estas letras
            for char in chars_for_number:
              built_combination.append(char)
              recurvise_search(index=index+1,
                               built_combination=built_combination)
              built_combination.pop() # Elimino la última letra añadida a la combinación
              
        
        # Comienzo inicializando un conjunto donde almacenar las posibles combinaciones
        letter_combinations_array = []
        
        # Valido el input recibido por la función
        if len(digits) == 0:
          return letter_combinations_array
        
        # Defino un diccionario que mapee cada uno de los dígitos del teclado, con los caracteres
        # que este puede representar.
        
        chars_for_number_dict = {
          "2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "pqrs",
          "8": "tuv",
          "9": "wxyz"
        }
        
        # Comienzo la búsqueda recursiva de combinaciones posibles
        recurvise_search(index=0,
                         built_combination=[])
        
        # Retorno el conjunto de combinaciones final
        return letter_combinations_array
      
      
if __name__ == "__main__":
  
  digits = "243"
  solution = Solution()
  sol = solution.letterCombinations(digits=digits)
  print(sol)
  