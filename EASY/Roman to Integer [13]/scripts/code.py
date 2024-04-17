"""
DESCRIPTION:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

 - I can be placed before V (5) and X (10) to make 4 and 9. 
 - X can be placed before L (50) and C (100) to make 40 and 90. 
 - C can be placed before D (500) and M (1000) to make 400 and 900.


## TODO ==> Given a roman numeral, convert it to an integer.

 

Example 1:

  Input: s = "III"
  Output: 3
  Explanation: III = 3.


Example 2:

  Input: s = "LVIII"
  Output: 58
  Explanation: L = 50, V= 5, III = 3.


Example 3:

  Input: s = "MCMXCIV"
  Output: 1994
  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

## Constraints:

  1 <= s.length <= 15
  s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
  It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        """Método de la clase Solution encargado de convertir en número entero una cadena de texto escrita en romano.
        
           Args:
               s -- Cadena de texto escrita en romano.
           
           Returns:
               int -- Entero con el valor del número escrito en romano.
        """
        
        # Defino un diccionario que mapee cada valor entero con su número en romano
        roman_array = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        integer_array = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        
        roman_integer_dict = {roman:integer for roman, integer in zip(roman_array, integer_array)}
        
        # Proceso el número recibido
        # Diccionario que mapea cada encuentro de letras
        roman_count_dict = {roman:0 for roman in roman_array}
        
        s_restante = s
        while (len(s_restante) > 0):
          # Defino una lista con los caracteres de s_restante
          s_restante_array = [roman for roman in str(s_restante)]
            
          for index, roman in enumerate(s_restante_array):
            try:
              if roman == "I" and (s_restante_array[index + 1] == "V" or s_restante_array[index + 1] == "X") or roman == "X" and (s_restante_array[index + 1] == "L" or s_restante_array[index + 1] == "C") or roman == "C" and (s_restante_array[index + 1] == "D" or s_restante_array[index + 1] == "M"):
                composed_value = str(roman) + str(s_restante_array[index + 1])
                roman_count_dict[composed_value] +=1
                
                # Elimino los caracteres iterados de la lista
                s_restante_array.pop(index + 1)
                s_restante_array.pop(index)
                
                # Actualizo s_restante
                s_restante = "".join(s_restante_array)
                break

              else:
                roman_count_dict[roman] +=1
                # Elimino el caracter iterado de la lista
                s_restante_array.pop(index)
                # Actualizo s_restante
                s_restante = "".join(s_restante_array)
                break
            except IndexError:
              roman_count_dict[roman] +=1
              # Elimino el caracter iterado de la lista
              s_restante_array.pop(index)
              # Actualizo s_restante
              s_restante = "".join(s_restante_array)
              break
                  
        # Conformo el entero final
        final_integer = 0
        for key, value in roman_count_dict.items():
          roman_to_integer = roman_integer_dict[key]
          final_integer += (roman_to_integer*value)
          
        return final_integer
      
      
if __name__ == "__main__":
  
  s = "MCMXCIV"
  solution = Solution()
  sol = solution.romanToInt(s=s)
  print(sol)
          