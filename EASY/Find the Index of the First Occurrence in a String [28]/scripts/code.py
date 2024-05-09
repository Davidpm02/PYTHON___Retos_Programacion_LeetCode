"""
DESCRIPTION:

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

 

Example 1:

  Input: haystack = "sadbutsad", needle = "sad"
  Output: 0
  Explanation: "sad" occurs at index 0 and 6.
               The first occurrence is at index 0, so we return 0.
               

Example 2:

  Input: haystack = "leetcode", needle = "leeto"
  Output: -1
  Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

## Constraints:

  1 <= haystack.length, needle.length <= 104
  haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        """Método de la clase Solution que simula el funcionamiento de búsqueda de 'una aguja en un pajar'.
           El método recibe dos parámetros, para los cuales se deberá de buscar si 'needle' se encuentra
           en 'haystack', y retornar el índice donde comienza la aparición.
           
           Args:
               haystack -- Cadena que actúa de pajar.
               needle -- Cadena que actúa de aguja.
           
           Returns:
               int -- Índice de la primera aparición del parámetro 'neddle'  dentro de 'haystack'.
        """
        
        # Me aseguro de que needle sea de longitud menor a haystack
        if len(needle) > len(haystack):
          return -1
        
        length_needle = len(needle)  #  <-- Referencia de la longitud de needle
        for index, char in enumerate(haystack):
          substring = haystack[index: index + length_needle]
          if substring == needle:
            return index
          continue
        
        # Si no se ha encontrado needle dentro de haystack, retorno -1.
        return -1
          
        
if __name__ == "__main__":
  
  solution = Solution()
  index = solution.strStr("hello", "ll")
  print("El índice es:", index)