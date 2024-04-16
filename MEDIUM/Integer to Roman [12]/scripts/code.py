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
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

 - I can be placed before V (5) and X (10) to make 4 and 9. 
 - X can be placed before L (50) and C (100) to make 40 and 90. 
 - C can be placed before D (500) and M (1000) to make 400 and 900.


## TODO ==> Given an integer, convert it to a roman numeral.

 

Example 1:

  Input: num = 3
  Output: "III"
  Explanation: 3 is represented as 3 ones.


Example 2:

  Input: num = 58
  Output: "LVIII"
  Explanation: L = 50, V = 5, III = 3.


Example 3:

  Input: num = 1994
  Output: "MCMXCIV"
  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

## Constraints:

1 <= num <= 3999"""

class Solution:
    def intToRoman(self, num: int) -> str:
      """Método de la clase Solution encargado de convertir un parámetro entero en una cadena con el mismo número expresado en romano.
      
         Args:
             num -- Entero a convertir en romano.
             
         Returns:
             str -- Cadena con el número recibido como parámetro expresado en romano.
      """
      
      # Defino un diccionario donde mapeo las opciones disponibles
      int_array = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
      roman_array = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
      
      int_roman_dict = {integer:roman for integer, roman in zip(int_array, roman_array)}
      
      # Defino un diccionario donde registro un conteo de las "letras" de la cadena final en romano
      int_count_dict = {integer:0 for integer in int_array}
      
      ## CONVERSIÓN A ROMANO
      num_restante = num
      while True:
        for integer in int_array[::-1]:
          if num_restante >= integer:
            int_count_dict[integer] += (num_restante//integer)
            num_restante = num_restante%integer
            continue
          else:
            continue
        break
        
      # Genero la cadena final
      string_array = []
      for key, value in int_count_dict.items():
        roman_value = int_roman_dict[key]
        string_array.append(roman_value*value)  # roman_value es una cadena, y la "multiplico" tantas veces como valores tenga 
      
      string_ = "".join(string_array[::-1])
      return string_
        
        
        
        
        
if __name__ == "__main__":
  
  num = 58
  solution = Solution()
  sol = solution.intToRoman(num=num)
  print(sol)
      
      